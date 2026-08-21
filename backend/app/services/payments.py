from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.api.auth import get_current_user_id
from app.config import settings
from app.services.payments import (
    create_payment_order,
    get_payment_order,
    submit_payment_reference,
)
from app.services.plans import get_plan


router = APIRouter(
    prefix="/api/v1/payments",
    tags=["Payments"],
)


class CreatePaymentRequest(BaseModel):
    plan_id: str = Field(
        min_length=1,
        max_length=50,
    )


class PaymentReferenceRequest(BaseModel):
    payment_reference: str = Field(
        min_length=3,
        max_length=100,
    )


@router.post("")
async def create_payment(
    request: CreatePaymentRequest,
    current_user_id: int = Depends(get_current_user_id),
):
    plan = get_plan(request.plan_id)

    if plan is None:
        raise HTTPException(
            status_code=404,
            detail="Plan not found",
        )

    if plan.price_egp_monthly <= 0:
        raise HTTPException(
            status_code=400,
            detail="The selected plan does not require payment.",
        )

    try:
        order = create_payment_order(
            user_id=current_user_id,
            plan_id=plan.id,
            amount_egp=plan.price_egp_monthly,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return {
        "id": order.id,
        "user_id": order.user_id,
        "plan_id": order.plan_id,
        "amount_egp": order.amount_egp,
        "currency": settings.payment_currency,
        "status": order.status.value,
        "payment_method": "instapay",
        "instapay_handle": settings.instapay_handle,
        "payment_reference": order.payment_reference,
        "created_at": order.created_at,
    }


@router.get("/{order_id}")
async def get_payment(
    order_id: str,
    current_user_id: int = Depends(get_current_user_id),
):
    order = get_payment_order(order_id)

    if order is None or order.user_id != current_user_id:
        raise HTTPException(
            status_code=404,
            detail="Payment order not found",
        )

    return {
        "id": order.id,
        "plan_id": order.plan_id,
        "amount_egp": order.amount_egp,
        "currency": settings.payment_currency,
        "status": order.status.value,
        "payment_reference": order.payment_reference,
        "created_at": order.created_at,
    }


@router.post("/{order_id}/reference")
async def add_payment_reference(
    order_id: str,
    request: PaymentReferenceRequest,
    current_user_id: int = Depends(get_current_user_id),
):
    order = get_payment_order(order_id)

    if order is None or order.user_id != current_user_id:
        raise HTTPException(
            status_code=404,
            detail="Payment order not found",
        )

    try:
        order = submit_payment_reference(
            order_id,
            request.payment_reference,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return {
        "id": order.id,
        "status": order.status.value,
        "payment_reference": order.payment_reference,
        "message": "Payment reference submitted for review.",
    }
