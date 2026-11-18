# Đại Cát Phong Thủy – MVP 0.1

## Phạm vi bản đầu
- Responsive web UI màu đen – vàng kim.
- FastAPI backend.
- Lưu hồ sơ phân tích bằng SQLite mặc định; hỗ trợ PostgreSQL qua `DATABASE_URL`.
- Engine khởi đầu: phân vùng 24 Sơn theo độ hướng, tra vận 20 năm theo bảng cấu hình.
- API: `GET /api/health`, `POST /api/house/analyze`, `GET /api/house/analyses`.

## Chạy local
Yêu cầu Python 3.11+.

```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Mở http://127.0.0.1:8000. Tài liệu API tại http://127.0.0.1:8000/docs.

## Dùng PostgreSQL
Đặt biến môi trường `DATABASE_URL`, ví dụ:

```bash
DATABASE_URL='postgresql+psycopg://user:password@localhost:5432/daicat' uvicorn app.main:app --reload
```

## Cấu trúc
- `backend/app/main.py`: API và khởi tạo ứng dụng.
- `backend/app/database.py`: kết nối DB.
- `backend/app/models.py`: bảng hồ sơ phân tích.
- `backend/app/engine/xuankong.py`: engine tính toán thử nghiệm.
- `frontend/`: giao diện web.
- `database/schema.sql`: schema PostgreSQL tham khảo.

## Cảnh báo độ chính xác
Đây là MVP kỹ thuật, chưa phải công cụ luận đoán phong thủy hoàn chỉnh. Năm xây dựng hiện được dùng làm proxy để tra vận; thực tế cần xác minh mốc lập vận theo trường phái, quá trình xây dựng/cải tạo và nhập trạch. Độ hướng phải là Bắc thực sau hiệu chỉnh. Bảng 3x3 hiện chỉ minh họa Lạc Thư, không phải bàn Phi Tinh cá nhân. Chưa tính Sơn tinh, Hướng tinh, Vận tinh, thế quái, thay tinh hay các quy tắc trường phái. Cần chuyên gia thẩm định và bộ test đối chiếu trước khi phát hành.
