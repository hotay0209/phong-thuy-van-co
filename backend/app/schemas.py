from pydantic import BaseModel, Field

class HouseAnalysisRequest(BaseModel):
    house_name: str = Field(default="Nhà ở", max_length=160)
    address: str | None = Field(default=None, max_length=300)
    construction_year: int = Field(ge=1000, le=2100)
    facing_degrees: float = Field(ge=0, lt=360, description="Độ hướng tính theo chiều kim đồng hồ từ Bắc thực")

class HouseAnalysisResponse(BaseModel):
    id: int
    house_name: str
    result: dict
