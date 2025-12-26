from data import books
def add_book():
    book_id = input("Nhập mã sách: ")
    title = input("Nhập tên sách: ")
    author = input("Nhập tác giả: ")
    quantity = int(input("Nhập số lượng: "))

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    })
    print("✔ Thêm sách thành công")
def show_books():
    if not books:
        print("Chưa có sách")
        return
    for b in books:
        print(b)    
def search_book():
    key = input("Nhập tên sách cần tìm: ")
    for b in books:
        if key.lower() in b["title"].lower():
            print(b)
def delete_book():
    book_id = input("Nhập mã sách cần xóa: ")
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            print("✔ Đã xóa sách")
            return
    print("❌ Không tìm thấy sách")            
def book_menu():
    while True:
        print("\n--- QUẢN LÍ SÁCH ---")
        print("1. Thêm sách")
        print("2. Xem danh sách")
        print("3. Tìm sách")
        print("4. Xóa sách")
        print("0. Quay lại")

        choice = input("Chọn: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "0":
            break    