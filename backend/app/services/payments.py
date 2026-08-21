from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.payments import (
    approve_payment,
    create_payment_order,
    get_payment_order,
    reject_payment,
    submit_payment_reference,
)
from app.services.plans import get_plan


router = APIRouter(
    prefix="/api/v1/payments",
    tags=["Payments"],
)


class CreatePaymentRequest(BaseModel):
    user_id: int = Field(gt=0)
    plan_id: str = Field(min_length=1)


class PaymentReferenceRequest(BaseModel):
    payment_reference: str = Field(
        min_length=3,
        max_length=100,
    )


@router.post("")
async def create_payment(request: CreatePaymentRequest):
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

    order = create_payment_order(
        user_id=request.user_id,
        plan_id=plan.id,
        amount_egp=plan.price_egp_monthly,
    )

    return {
        "id": order.id,
        "user_id": order.user_id,
        "plan_id": order.plan_id,
        "amount_egp": order.amount_egp,
        "currency": "EGP",
        "status": order.status.value,
        "payment_method": "instapay",
        "instapay_handle": "waeldeban@instapay",
        "payment_reference": order.payment_reference,
        "created_at": order.created_at,
    }


@router.get("/{order_id}")
async def get_payment(order_id: str):
    order = get_payment_order(order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Payment order not found",
        )

    return {
        "id": order.id,
        "user_id": order.user_id,
        "plan_id": order.plan_id,
        "amount_egp": order.amount_egp,
        "currency": "EGP",
        "status": order.status.value,
        "payment_reference": order.payment_reference,
        "created_at": order.created_at,
    }


@router.post("/{order_id}/reference")
async def add_payment_reference(
    order_id: str,
    request: PaymentReferenceRequest,
):
    order = submit_payment_reference(
        order_id,
        request.payment_reference,
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Payment order not found",
        )

    return {
        "id": order.id,
        "status": order.status.value,
        "payment_reference": order.payment_reference,
        "message": "Payment reference submitted for review.",
    }


@router.post("/{order_id}/approve")
async def approve_payment_order(order_id: str):
    order = approve_payment(order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Payment order not found",
        )

    return {
        "id": order.id,
        "status": order.status.value,
        "message": "Payment approved.",
    }


@router.post("/{order_id}/reject")
async def reject_payment_order(order_id: str):
    order = reject_payment(order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Payment order not found",
        )

    return {
        "id": order.id,
        "status": order.status.value,
        "message": "Payment rejected.",
    }
