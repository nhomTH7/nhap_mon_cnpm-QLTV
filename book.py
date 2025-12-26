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