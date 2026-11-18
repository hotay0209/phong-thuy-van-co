# PHONG THỦY VẠN CỔ – Web App/PWA MVP 0.1

## Chạy thử trên máy tính
- Mở terminal trong thư mục này.
- Chạy `python -m http.server 8080`.
- Mở `http://localhost:8080`.

## Đưa lên Internet
Có thể triển khai thư mục này lên GitHub Pages, Netlify hoặc Render Static Site. Cần dùng HTTPS để trình duyệt cho phép cảm biến thiết bị.

## Tính năng đang có trong bản 0.1
- Giao diện responsive tiếng Việt, đen/vàng kim.
- La Kinh: đọc DeviceOrientation khi trình duyệt hỗ trợ, nhập góc thủ công, tra cứu sơ bộ 24 Sơn.
- Bát Trạch: tra cứu cung phi/hướng theo công thức phổ thông sơ bộ.
- Huyền Không: nhập dữ liệu công trình và minh họa Cửu cung; chưa lập tinh bàn thực.
- Lịch dương tương tác; chưa có chuyển đổi âm lịch/Can Chi.
- Tuổi xây dựng: phép tra cứu sơ bộ, cần đối chiếu quy ước.
- Hồ sơ công trình lưu trên localStorage của trình duyệt.
- PWA manifest, service worker và biểu tượng cài đặt.

## Giới hạn quan trọng
Đây là bản MVP giao diện và tương tác ban đầu, không phải bản sao phần mềm thương mại, không phải hệ thống phong thủy đã thẩm định. Độ chính xác cảm biến phụ thuộc thiết bị và hiệu chỉnh từ trường. Huyền Không Phi Tinh cần chốt trường phái, cách xác định vận nhà, tọa/hướng và quy tắc an tinh trước khi lập bàn chính thức. Âm lịch/Can Chi và tiết khí chưa được tích hợp. Dữ liệu hồ sơ hiện chỉ lưu cục bộ trên thiết bị, chưa đồng bộ tài khoản/cloud.
