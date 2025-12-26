from data import readers, borrow_records
from datetime import datetime
# 1. Thêm bạn đọc
def add_reader():
    student_id = input("Nhập mã thẻ sinh viên: ")
    name = input("Nhập họ tên sinh viên: ")

    for r in readers:
        if r["student_id"] == student_id:
            print("❌ Thẻ sinh viên đã tồn tại")
            return

    readers.append({
        "student_id": student_id,
        "name": name
    })
    print("✔ Thêm bạn đọc thành công")
# 2. Sửa thông tin bạn đọc
def update_reader():
    student_id = input("Nhập mã thẻ sinh viên cần sửa: ")
    for r in readers:
        if r["student_id"] == student_id:
            r["name"] = input("Nhập tên mới: ")
            print("✔ Cập nhật thông tin thành công")
            return
    print(" Không tìm thấy bạn đọc")
# 3. Xóa bạn đọc
def delete_reader():
    student_id = input("Nhập mã thẻ sinh viên cần xóa: ")
    for r in readers:
        if r["student_id"] == student_id:
            readers.remove(r)
            print("✔ Đã xóa bạn đọc")
            return
    print("Không tìm thấy bạn đọc")
# 4. Tìm kiếm bạn đọc
def search_reader():
    keyword = input("Nhập tên hoặc MSSV cần tìm: ").lower()
    found = False
    for r in readers:
        if keyword in r["student_id"].lower() or keyword in r["name"].lower():
            print(f"MSSV: {r['student_id']} | Tên: {r['name']}")
            found = True
    if not found:
        print(" Không tìm thấy kết quả")
# 5. Xem lịch sử mượn – trả
def view_borrow_history():
    student_id = input("Nhập mã thẻ sinh viên: ")
    found = False

    for r in borrow_records:
        if r["student_id"] == student_id:
            found = True
            print(
                f"Sách: {r['book_id']} | "
                f"Mượn: {r['borrow_date'].strftime('%d/%m/%Y')} | "
                f"Hạn trả: {r['due_date'].strftime('%d/%m/%Y')} | "
                f"Trạng thái: {r['status']}"
            )

    if not found:
        print("❌ Không có lịch sử mượn – trả")