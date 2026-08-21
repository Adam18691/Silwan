from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Plan:
    id: str
    name: str
    price_egp_monthly: int
    sessions: Optional[int]
    description: str
    features: tuple[str, ...]


PLANS: tuple[Plan, ...] = (
    Plan(
        id="rayh",
        name="الريح",
        price_egp_monthly=0,
        sessions=2,
        description="الباقة المجانية الأساسية.",
        features=(
            "جلستان مجانيتان",
            "تمارين مقام النقلة",
            "المحتوى العربي",
            "الوصول إلى الطوارئ",
        ),
    ),
    Plan(
        id="nasim",
        name="النسيم",
        price_egp_monthly=960,
        sessions=10,
        description="للاستخدام المنتظم.",
        features=(
            "10 جلسات شهريًا",
            "مقام النقلة بدون حد",
            "مجتمع تفاعلي",
            "محتوى عربي",
        ),
    ),
    Plan(
        id="jin",
        name="الجن",
        price_egp_monthly=2400,
        sessions=None,
        description="للاستخدام المكثف.",
        features=(
            "جلسات غير محدودة",
            "تحليل صوت وفيديو",
            "تقارير أسبوعية",
            "أولوية الدعم",
        ),
    ),
    Plan(
        id="ruh",
        name="الروح",
        price_egp_monthly=2880,
        sessions=None,
        description="خطة متقدمة مع دعم بشري.",
        features=(
            "كل مزايا الجن",
            "جلسة صوتية أسبوعية",
            "تخصيص محدود",
        ),
    ),
    Plan(
        id="khatem",
        name="الخاتم",
        price_egp_monthly=3360,
        sessions=None,
        description="الخطة الأعلى.",
        features=(
            "كل مزايا الجن",
            "جلسة فيديو أسبوعية مع معالج بشري",
            "تخصيص كامل",
            "الإرث الحي",
            "الوعي المتوازي",
        ),
    ),
)


def get_all_plans() -> tuple[Plan, ...]:
    return PLANS


def get_plan(plan_id: str) -> Plan | None:
    normalized_id = plan_id.strip().lower()

    for plan in PLANS:
        if plan.id == normalized_id:
            return plan

    return None
