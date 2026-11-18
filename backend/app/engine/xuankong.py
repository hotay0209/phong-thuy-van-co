"""Transparent starter calculations for Xuan Kong Feng Shui.

Scope in MVP-0.1:
- Map a compass bearing to one of the traditional 24 mountains.
- Map a construction year to a 20-year period using the standard period table.
- Produce a clearly-labelled Luo Shu base-star grid for visual inspection.

This is NOT yet a complete Xuan Kong chart. Mountain star, facing star,
replacement stars, period-transition rules and school-specific rules are
intentionally withheld until verified against an expert-approved test corpus.
Bearings are degrees clockwise from true north, not uncorrected magnetic north.
"""
from dataclasses import dataclass

MOUNTAINS = [
    ("N1", "Nhâm", 337.5), ("N2", "Tý", 352.5), ("N3", "Quý", 7.5),
    ("NE1", "Sửu", 22.5), ("NE2", "Cấn", 37.5), ("NE3", "Dần", 52.5),
    ("E1", "Giáp", 67.5), ("E2", "Mão", 82.5), ("E3", "Ất", 97.5),
    ("SE1", "Thìn", 112.5), ("SE2", "Tốn", 127.5), ("SE3", "Tỵ", 142.5),
    ("S1", "Bính", 157.5), ("S2", "Ngọ", 172.5), ("S3", "Đinh", 187.5),
    ("SW1", "Mùi", 202.5), ("SW2", "Khôn", 217.5), ("SW3", "Thân", 232.5),
    ("W1", "Canh", 247.5), ("W2", "Dậu", 262.5), ("W3", "Tân", 277.5),
    ("NW1", "Tuất", 292.5), ("NW2", "Càn", 307.5), ("NW3", "Hợi", 322.5),
]
PERIODS = [(1864,1883,1),(1884,1903,2),(1904,1923,3),(1924,1943,4),
           (1944,1963,5),(1964,1983,6),(1984,2003,7),(2004,2023,8),
           (2024,2043,9),(2044,2063,1),(2064,2083,2)]
# Luo Shu arrangement, read top-left to bottom-right.
LUO_SHU = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

class CalculationInputError(ValueError):
    pass

def get_period(year: int) -> int:
    for start, end, number in PERIODS:
        if start <= year <= end:
            return number
    raise CalculationInputError("Năm nằm ngoài bảng vận đã cấu hình (1864–2083). Cần bổ sung quy tắc trước khi tính.")

def get_mountain(degrees: float) -> tuple[str, str]:
    if not 0 <= degrees < 360:
        raise CalculationInputError("Độ hướng phải nằm trong khoảng 0 đến dưới 360 độ.")
    # Each mountain occupies 15 degrees; sectors are centred on the listed midpoint.
    index = int(((degrees - 337.5) % 360) // 15)
    code, name, _ = MOUNTAINS[index]
    return code, name

def analyze_house(construction_year: int, facing_degrees: float) -> dict:
    if not 1000 <= construction_year <= 2100:
        raise CalculationInputError("Năm xây dựng không hợp lệ.")
    period = get_period(construction_year)
    facing_code, facing_name = get_mountain(facing_degrees)
    sitting_degrees = (facing_degrees + 180) % 360
    sitting_code, sitting_name = get_mountain(sitting_degrees)
    # Grid shown as a reference diagram only; not a full natal flying-star chart.
    return {
        "construction_year": construction_year,
        "period": period,
        "period_label": f"Vận {period}",
        "facing_degrees": round(facing_degrees, 2),
        "facing_mountain": {"code": facing_code, "name": facing_name},
        "sitting_degrees": round(sitting_degrees, 2),
        "sitting_mountain": {"code": sitting_code, "name": sitting_name},
        "luo_shu_reference_grid": LUO_SHU,
        "calculation_status": "partial_mvp",
        "limitations": [
            "Độ hướng đầu vào được giả định đã hiệu chỉnh về Bắc thực.",
            "Vận nhà tạm xác định theo năm xây dựng; cần xác minh năm hoàn công/nhập trạch và quy tắc chuyển vận của trường phái.",
            "Bảng Cửu cung hiển thị là bố cục Lạc Thư tham chiếu, chưa phải bàn Phi Tinh hoàn chỉnh.",
            "Chưa tính Sơn tinh, Hướng tinh, vận tinh, thế quái hoặc thay tinh."
        ]
    }
