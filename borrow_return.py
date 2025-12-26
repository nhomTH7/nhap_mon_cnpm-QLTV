from data import books, readers, borrow_records
from datetime import datetime, timedelta
BORROW_DAYS = 7 #han 7 ngay

def borrow_book():
    student_id = input("Nhập mã thẻ sinh viên: ")
    book_id = input("Nhập mã sách: ")

    # kiểm tra sinh viên tồn tại
    if not any(r["student_id"] == student_id for r in readers):
        print("❌ Thẻ sinh viên không tồn tại")
        return

    for book in books:
        if book["id"] == book_id and book["quantity"] > 0:
            borrow_date = datetime.now()
            due_date = borrow_date + timedelta(days=BORROW_DAYS)

            borrow_records.append({
                "student_id": student_id,
                "book_id": book_id,
                "borrow_date": borrow_date,
                "due_date": due_date,
                "status": "Đang mượn"
            })

            book["quantity"] -= 1
            print(f"✔ Mượn sách thành công | Hạn trả: {due_date.strftime('%d/%m/%Y')}")
            return

    print("❌ Không mượn được sách")
    
def return_book():
    student_id = input("Nhập mã thẻ sinh viên: ")
    book_id = input("Nhập mã sách trả: ")

    for record in borrow_records:
        if (record["student_id"] == student_id and
            record["book_id"] == book_id and
            record["status"] == "Đang mượn"):

            record["status"] = "Đã trả"
            return_date = datetime.now()

            if return_date > record["due_date"]:
                late_days = (return_date - record["due_date"]).days
                print(f"⚠ QUÁ HẠN {late_days} ngày")

            for book in books:
                if book["id"] == book_id:
                    book["quantity"] += 1

            print("✔ Trả sách thành công")
            return

    print("❌ Không tìm thấy thông tin mượn")