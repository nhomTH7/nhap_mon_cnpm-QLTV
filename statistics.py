from data import books, readers, borrow_records
from datetime import datetime

def statistics_menu():
    print("\n--- THỐNG KÊ _ BÁO CÁO ---")
    print("Tổng số sách:", len(books))
    print("Tổng số bạn đọc:", len(readers))
    print("Tổng lượt mượn:", len(borrow_records))

    overdue = 0
    today = datetime.now()
    for r in borrow_records:
        if r["status"] == "Đang mượn" and today > r["due_date"]:
            overdue += 1

    print("⚠ Số lượt mượn quá hạn:", overdue)