from book import book_menu
from readers import add_reader, update_reader
from borrow_return import borrow_menu
from statistics import statistics_menu

def reader_menu():
    while True:
        print("\n--- QUẢN LÍ BẠN ĐỌC ---")
        print("1. Thêm bạn đọc")
        print("2. Cập nhật thông tin bạn đọc")
        print("0. Quay lại")

        choice = input("Chọn: ")
        if choice == "1":
            add_reader()
        elif choice == "2":
            update_reader()
        elif choice == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

def main_menu():
    while True:
        print("\n====== HỆ THỐNG QUẢN LÍ THƯ VIỆN ======")
        print("1. Quản lí sách")
        print("2. Quản lí bạn đọc")
        print("3. Mượn – Trả sách")
        print("4. Thống kê – Báo cáo")
        print("0. Thoát")

        choice = input("Chọn: ")
        if choice == "1":
            book_menu()
        elif choice == "2":
            reader_menu()
        elif choice == "3":
            borrow_menu()
        elif choice == "4":
            statistics_menu()
        elif choice == "0":
            print("👋 Kết thúc chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# Điểm bắt đầu chương trình
if __name__ == "__main__":
    main_menu()