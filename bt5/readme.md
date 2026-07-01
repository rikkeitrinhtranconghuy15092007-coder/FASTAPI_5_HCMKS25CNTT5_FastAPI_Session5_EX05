PHẦN 1: LUỒNG XỬ LÝ DỮ LIỆU (DATA FLOW)
Khi Client gửi một request DELETE /products/{product_id} lên hệ thống, Backend sẽ xử lý theo các bước tuần tự sau:

Nhận request: Hệ thống tiếp nhận product_id từ đường dẫn (Path Parameter).

Tìm kiếm sản phẩm: Hệ thống duyệt qua danh sách products để tìm sản phẩm có id khớp với product_id được gửi lên.

Trường hợp không tìm thấy: Ngay lập tức bắn lỗi 404 Not Found kèm thông báo "Product not found".

Kiểm tra trạng thái (Nếu tìm thấy sản phẩm):

Nếu sản phẩm có "is_active": False: Hệ thống bắn lỗi 400 Bad Request kèm thông báo "Product already inactive".

Nếu sản phẩm có "is_active": True: Hệ thống tiến hành cập nhật trạng thái của sản phẩm đó thành False.

Trả về kết quả: Phản hồi về cho Client mã trạng thái thành công kèm thông tin sản phẩm đã được cập nhật.