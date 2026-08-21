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
    if user_id <= 0:
        raise ValueError("Invalid user ID.")

    if amount_egp <= 0:
        raise ValueError(
            "Payment amount must be greater than zero."
        )

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

    if order.status != PaymentStatus.PENDING:
        return order

    reference = payment_reference.strip()

    if not reference:
        raise ValueError(
            "Payment reference cannot be empty."
        )

    order.payment_reference = reference

    return order


def approve_payment(
    order_id: str,
) -> PaymentOrder | None:
    order = _orders.get(order_id)

    if order is None:
        return None

    if order.status != PaymentStatus.PENDING:
        return order

    order.status = PaymentStatus.APPROVED

    return order


def reject_payment(
    order_id: str,
) -> PaymentOrder | None:
    order = _orders.get(order_id)

    if order is None:
        return None

    if order.status != PaymentStatus.PENDING:
        return order

    order.status = PaymentStatus.REJECTED

    return order
