from enum import Enum


class SilwanWorld(str, Enum):
    MITHWA_SAMT = "mithwa_samt"
    MAQAM_NAQLAH = "maqam_naqlah"
    MAHKAMAT_ALNAFS = "mahkamat_alnafs"


WORLD_INFO = {
    SilwanWorld.MITHWA_SAMT: {
        "name": "مَثوى الصمت",
        "purpose": "تحليل أنماط المستخدم العاطفية",
    },
    SilwanWorld.MAQAM_NAQLAH: {
        "name": "مَقام النقلة",
        "purpose": "تمارين واستجابات فورية",
    },
    SilwanWorld.MAHKAMAT_ALNAFS: {
        "name": "مَحكمة النفس",
        "purpose": "جلسات عميقة وسرد شخصي",
    },
}


def get_world(world: SilwanWorld) -> dict:
    return WORLD_INFO[world]
