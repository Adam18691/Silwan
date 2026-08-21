from fastapi import APIRouter, HTTPException

from app.services.plans import get_all_plans, get_plan


router = APIRouter(
    prefix="/api/v1/plans",
    tags=["Plans"],
)


@router.get("")
async def list_plans():
    return {
        "currency": "EGP",
        "language": "ar",
        "direction": "rtl",
        "plans": [
            {
                "id": plan.id,
                "name": plan.name,
                "price_egp_monthly": plan.price_egp_monthly,
                "sessions": plan.sessions,
                "description": plan.description,
                "features": list(plan.features),
            }
            for plan in get_all_plans()
        ],
    }


@router.get("/{plan_id}")
async def get_plan_details(plan_id: str):
    plan = get_plan(plan_id)

    if plan is None:
        raise HTTPException(
            status_code=404,
            detail="Plan not found",
        )

    return {
        "id": plan.id,
        "name": plan.name,
        "price_egp_monthly": plan.price_egp_monthly,
        "sessions": plan.sessions,
        "description": plan.description,
        "features": list(plan.features),
    }
