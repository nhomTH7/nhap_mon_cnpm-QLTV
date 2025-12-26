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

