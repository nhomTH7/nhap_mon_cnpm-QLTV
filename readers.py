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
# 6. Cảnh báo bạn đọc vi phạm (quá hạn)
def warning_violation():
    today = datetime.now()
    violated = False

    for r in borrow_records:
        if r["status"] == "Đang mượn" and today > r["due_date"]:
            violated = True
            late_days = (today - r["due_date"]).days
            print(
                f"⚠ MSSV: {r['student_id']} | "
                f"Sách: {r['book_id']} | "
                f"Quá hạn: {late_days} ngày"
            )

    if not violated:
        print("✔ Không có bạn đọc vi phạm")
# MENU QUẢN LÍ BẠN ĐỌC
def reader_menu():
    while True:
        print("\n--- QUẢN LÍ BẠN ĐỌC ---")
        print("1. Thêm bạn đọc")
        print("2. Sửa thông tin bạn đọc")
        print("3. Xóa bạn đọc")
        print("4. Tìm kiếm bạn đọc")
        print("5. Xem lịch sử mượn – trả")
        print("6. Cảnh báo bạn đọc vi phạm")
        print("0. Quay lại")

        choice = input("Chọn: ")

        if choice == "1":
            add_reader()
        elif choice == "2":
            update_reader()
        elif choice == "3":
            delete_reader()
        elif choice == "4":
            search_reader()
        elif choice == "5":
            view_borrow_history()
        elif choice == "6":
            warning_violation()
        elif choice == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")








