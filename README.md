# Library Management System

**English** | [فارسی](#سامانه-مدیریت-کتابخانه)

A console-based library management application written in Python using object-oriented programming. It was built as a midterm project for the Advanced Programming course at the University of Qom.

The program lets you add books to a library with a limited capacity, borrow and return them, and view the library's current status through an interactive menu.

## Features

- Add new books (title, author, year) with a capacity limit
- Show all available books
- Borrow a book by its title
- Return a borrowed book
- Show all currently borrowed books
- Generate a report: available books, borrowed books, and remaining capacity

## Project Structure

```
library-management-system/
├── library_manager.py   # Classes and the interactive menu
├── README.md
└── .gitignore
```

## Classes

### `Book`
Represents a single book.

| Member | Description |
|---|---|
| `title`, `author`, `year` | Book information |
| `status` | `"available"` or `"borrowed"` |
| `borrow()` | Marks the book as borrowed if it is available |
| `return_book()` | Marks the book as available if it was borrowed |
| `is_available()` | Prints whether the book can be borrowed |
| `__str__()` | Readable text representation of the book |

### `Library`
Manages the collection of books.

| Member | Description |
|---|---|
| `books` | List of available books |
| `borrowed_books` | List of borrowed books |
| `max_size` | Maximum number of books the library can hold |
| `add_book()` | Adds a book if there is remaining capacity |
| `find_book()` | Searches the available books by title |
| `borrow_book()` / `return_book()` | Moves a book between the two lists |
| `show_books()` / `show_borrowed()` | Prints the corresponding list |
| `get_report()` | Prints the library status report |

## How to Run

Requires Python 3.8 or newer. No external libraries are needed.

```bash
git clone https://github.com/rominaxoii/library-management-system.git
cd library-management-system
python library_manager.py
```

## Usage

When the program starts, it shows this menu:

```
1. Add Book
2. Show Available Books
3. Borrow Book
4. Return Book
5. Show Borrowed Books
6. Show Report
7. Exit
```

Enter the number of the action you want and follow the prompts. The default library capacity is 20 books.

## Concepts Practiced

- Classes and objects
- Encapsulating data and behavior in methods
- Working with lists
- `__init__` and `__str__` special methods
- Input handling and an interactive menu loop

## Author

Romina Raeisi
- GitHub: [rominaxoii](https://github.com/rominaxoii)
- LinkedIn: [romina-raeisi](https://www.linkedin.com/in/romina-raeisi-a3b779445)

---

<div dir="rtl">

# سامانه مدیریت کتابخانه

[English](#library-management-system) | **فارسی**

یک برنامه کنسولی برای مدیریت کتابخانه که با زبان پایتون و به روش برنامه‌نویسی شی‌گرا نوشته شده است. این پروژه برای میان‌ترم درس برنامه‌نویسی پیشرفته در دانشگاه قم انجام شده است.

با این برنامه می‌توانید کتاب‌ها را به کتابخانه‌ای با ظرفیت محدود اضافه کنید، کتاب امانت بگیرید و برگردانید، و وضعیت کتابخانه را از طریق یک منوی تعاملی ببینید.

## امکانات

- افزودن کتاب جدید (عنوان، نویسنده، سال) با محدودیت ظرفیت
- نمایش همه کتاب‌های موجود
- امانت گرفتن کتاب با عنوان آن
- بازگرداندن کتاب امانت‌گرفته‌شده
- نمایش کتاب‌های امانت‌داده‌شده
- گزارش وضعیت: تعداد کتاب‌های موجود، امانت‌داده‌شده و ظرفیت باقی‌مانده

## ساختار پروژه

</div>

```
library-management-system/
├── library_manager.py   # کلاس‌ها و منوی تعاملی
├── README.md
└── .gitignore
```

<div dir="rtl">

## کلاس‌ها

### کلاس `Book`
نمایانگر یک کتاب.

| عضو | توضیح |
|---|---|
| `title`, `author`, `year` | اطلاعات کتاب |
| `status` | وضعیت: `"available"` یا `"borrowed"` |
| `borrow()` | اگر کتاب موجود باشد، آن را امانت‌داده‌شده می‌کند |
| `return_book()` | اگر کتاب امانت بوده باشد، آن را دوباره موجود می‌کند |
| `is_available()` | موجود بودن کتاب را چاپ می‌کند |
| `__str__()` | نمایش متنی خوانا از کتاب |

### کلاس `Library`
مدیریت مجموعه کتاب‌ها.

| عضو | توضیح |
|---|---|
| `books` | لیست کتاب‌های موجود |
| `borrowed_books` | لیست کتاب‌های امانت‌داده‌شده |
| `max_size` | بیشترین تعداد کتاب قابل نگهداری |
| `add_book()` | در صورت وجود ظرفیت، کتاب را اضافه می‌کند |
| `find_book()` | جستجوی کتاب موجود با عنوان |
| `borrow_book()` / `return_book()` | جابه‌جایی کتاب بین دو لیست |
| `show_books()` / `show_borrowed()` | چاپ لیست مربوطه |
| `get_report()` | چاپ گزارش وضعیت کتابخانه |

## نحوه اجرا

به پایتون ۳.۸ یا بالاتر نیاز دارد. کتابخانه خارجی لازم نیست.

</div>

```bash
git clone https://github.com/rominaxoii/library-management-system.git
cd library-management-system
python library_manager.py
```

<div dir="rtl">

## نحوه استفاده

با اجرای برنامه این منو نمایش داده می‌شود:

</div>

```
1. Add Book
2. Show Available Books
3. Borrow Book
4. Return Book
5. Show Borrowed Books
6. Show Report
7. Exit
```

<div dir="rtl">

شماره گزینه دلخواه را وارد کنید و مراحل را دنبال کنید. ظرفیت پیش‌فرض کتابخانه ۲۰ کتاب است.

## مفاهیم تمرین‌شده

- کلاس و شیء
- قرار دادن داده و رفتار در متدها
- کار با لیست‌ها
- متدهای خاص `__init__` و `__str__`
- دریافت ورودی و حلقه منوی تعاملی

## نویسنده

رومینا رئیسی (Romina Raeisi)
- گیت‌هاب: [rominaxoii](https://github.com/rominaxoii)
- لینکدین: [romina-raeisi](https://www.linkedin.com/in/romina-raeisi-a3b779445)

</div>
