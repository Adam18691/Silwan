from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


class PaymentStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class PaymentOrder:
    id: str
    user_id: int
    plan_id: str
    amount_egp: int
    status: PaymentStatus
    payment_reference: str | None
    created_at: datetime


_orders: dict[str, PaymentOrder] = {}


def create_payment_order(
    user_id: int,
    plan_id: str,
    amount_egp: int,
) -> PaymentOrder:
    order = PaymentOrder(
        id=str(uuid4()),
        user_id=user_id,
        plan_id=plan_id,
        amount_egp=amount_egp,
        status=PaymentStatus.PENDING,
        payment_reference=None,
        created_at=datetime.now(timezone.utc),
    )

    _orders[order.id] = order
    return order


def get_payment_order(
    order_id: str,
) -> PaymentOrder | None:
    return _orders.get(order_id)


def submit_payment_reference(
    order_id: str,
    payment_reference: str,
) -> PaymentOrder | None:
    order = _orders.get(order_id)

    if order is None:
        return None

    order.payment_reference = payment_reference.strip()
    return order


def approve_payment(
    order_id: str,
) -> PaymentOrder | None:
    order = _orders.get(order_id)

    if order is None:
        return None

    order.status = PaymentStatus.APPROVED
    return order


def reject_payment(
    order_id: str,
) -> PaymentOrder | None:
    order = _orders.get(order_id)

    if order is None:
        return None

    order.status = PaymentStatus.REJECTED
    return order
