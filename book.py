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
