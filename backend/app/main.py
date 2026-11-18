import json
from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import HouseAnalysis
from .schemas import HouseAnalysisRequest
from .engine.xuankong import analyze_house, CalculationInputError

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Đại Cát Phong Thủy API", version="0.1.0", description="MVP API – phân tích tọa hướng và vận nhà; kết quả đang ở mức thử nghiệm.")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
def health():
    return {"status": "ok", "product": "Đại Cát Phong Thủy", "version": "0.1.0"}

@app.post("/api/house/analyze")
def create_house_analysis(payload: HouseAnalysisRequest, db: Session = Depends(get_db)):
    try:
        result = analyze_house(payload.construction_year, payload.facing_degrees)
    except CalculationInputError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    record = HouseAnalysis(house_name=payload.house_name, address=payload.address,
        construction_year=payload.construction_year, facing_degrees=payload.facing_degrees,
        facing_mountain=result["facing_mountain"]["name"], sitting_mountain=result["sitting_mountain"]["name"],
        period_number=result["period"], result_json=json.dumps(result, ensure_ascii=False))
    db.add(record); db.commit(); db.refresh(record)
    return {"id": record.id, "house_name": record.house_name, "result": result}

@app.get("/api/house/analyses")
def list_house_analyses(db: Session = Depends(get_db)):
    rows = db.query(HouseAnalysis).order_by(HouseAnalysis.id.desc()).limit(50).all()
    return [{"id": r.id, "house_name": r.house_name, "construction_year": r.construction_year,
             "facing_degrees": r.facing_degrees, "period": r.period_number, "created_at": r.created_at.isoformat() if r.created_at else None} for r in rows]

FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"
app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
