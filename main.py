import book_data
import library_logic

def show_menu():
    print("\n" + "="*40)
    print("      CSE DEPARTMENT LIBRARY SYSTEM")
    print("="*40)
    print(" 1. View Inventory")
    print(" 2. Issue a Book")
    print(" 3. Return a Book")
    print(" 4. Restock/Add New Book")
    print(" 5. Exit")
    print("-" * 40)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            print("\n--- Current Library Stock ---")
            # Using items() to loop through the book dictionary
            for title, count in book_data.BOOKS.items():
                print(f" * {title:<30} | Copies: {count}")

        elif choice == '2':
            user = input("Student Name: ")
            book = input("Book Title: ")
            try:
                days = int(input("Issue duration (days): "))
                # Logic handles stock check and date math
                status = library_logic.issue_book(book_data.BOOKS, book_data.ISSUED_RECORDS, user, book, days)
                print(status)
                book_data.save_data(book_data.BOOKS, book_data.ISSUED_RECORDS)
            except ValueError:
                print("❌ Error: Please enter a valid number for days.")

        elif choice == '3':
            user = input("Student Name: ")
            status = library_logic.return_book(book_data.BOOKS, book_data.ISSUED_RECORDS, user)
            print(status)
            # Save progress after book is returned
            book_data.save_data(book_data.BOOKS, book_data.ISSUED_RECORDS)

        elif choice == '4':
            title = input("Enter book title: ")
            try:
                qty = int(input(f"How many copies of '{title}' to add? "))
                if qty < 0:
                    print("❌ Error: You cannot add a negative number of books.")
                else:
                    # Update dictionary and save to JSON
                    book_data.BOOKS[title] = book_data.BOOKS.get(title, 0) + qty
                    print(f"✅ Updated: {title} now has {book_data.BOOKS[title]} copies.")
                    book_data.save_data(book_data.BOOKS, book_data.ISSUED_RECORDS)
            except ValueError:
                print("❌ Error: Please enter a whole number.")

        elif choice == '5':
            print("\nShutting down system. Goodbye! 👋")
            break
            
        else:
            print("❌ Invalid input. Please select 1 to 5.")

if __name__ == "__main__":
    main()