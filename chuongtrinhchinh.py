from book import book_menu
from readers import reader_menu
from borrow_return import borrow_menu
from statistics import statistics_menu
def main_menu():
    while True:
        print("\n====================================")
        print("  HỆ THỐNG QUẢN LÍ THƯ VIỆN ĐẠI HỌC")
        print("====================================")
        print("1. Quản lí sách")
        print("2. Quản lí bạn đọc (thẻ sinh viên)")
        print("3. Quản lí mượn _ trả sách")
        print("4. Thống kê _ báo cáo")
        print("0. Thoát chương trình")
        print("------------------------------------")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            book_menu()

        elif choice == "2":
            reader_menu()

        elif choice == "3":
            borrow_menu()

        elif choice == "4":
            statistics_menu()

        elif choice == "0":
            print("👋 Kết thúc chương trình. Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại!")
if __name__ == "__main__":
    main_menu()
