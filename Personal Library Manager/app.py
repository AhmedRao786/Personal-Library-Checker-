import json

class LibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        """Load library from a file if it exists."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_library(self):
        """Save library to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        """Let the user add a new book to their collection."""
        print("\nLet's add a new book to your library!")
        title = input("📖 Enter the book title: ").strip()
        author = input("✍️ Enter the author's name: ").strip()
        year = input("📅 Enter the publication year: ").strip()
        genre = input("🎭 Enter the genre: ").strip()
        read_status = input("👓 Have you read this book? (yes/no): ").strip().lower() == "yes"
        
        book = {"title": title, "author": author, "year": int(year), "genre": genre, "read": read_status}
        self.library.append(book)
        self.save_library()
        print("✅ Book added successfully!\n")

    def remove_book(self):
        """Allow the user to remove a book by its title."""
        print("\nLet's remove a book from your collection.")
        title = input("🗑️ Enter the title of the book to remove: ").strip()
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        self.save_library()
        print("✅ Book removed successfully!\n")

    def search_book(self):
        """Help the user find a book by title or author."""
        print("\n🔍 Searching for a book...")
        keyword = input("Enter book title or author: ").strip().lower()
        results = [book for book in self.library if keyword in book["title"].lower() or keyword in book["author"].lower()]
        
        if results:
            print("\n📚 Here are the matching books:")
            for book in results:
                self.display_book(book)
        else:
            print("❌ No books found matching your search.\n")

    def display_book(self, book):
        """Show a book's details in a friendly format."""
        print(f"\n📖 Title: {book['title']}")
        print(f"✍️ Author: {book['author']}")
        print(f"📅 Year: {book['year']}")
        print(f"🎭 Genre: {book['genre']}")
        print(f"👓 Read: {'✅ Yes' if book['read'] else '❌ No'}\n")

    def display_all_books(self):
        """List all books in the library beautifully."""
        print("\n📚 Your Personal Library:")
        if self.library:
            for book in self.library:
                self.display_book(book)
        else:
            print("❌ No books in the library yet.\n")

    def display_statistics(self):
        """Give insights about the user's reading habits."""
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book["read"])
        read_percentage = (read_books / total_books * 100) if total_books > 0 else 0

        print("\n📊 Library Statistics:")
        print(f"📚 Total books: {total_books}")
        print(f"👓 Books read: {read_books} ({read_percentage:.2f}%)\n")

    def menu(self):
        """Guide the user through the menu system."""
        while True:
            print("\n📖 Welcome to Your Personal Library Manager! 📖")
            print("1️⃣ Add a book")
            print("2️⃣ Remove a book")
            print("3️⃣ Search for a book")
            print("4️⃣ Display all books")
            print("5️⃣ Display statistics")
            print("6️⃣ Exit")
            
            choice = input("\n👉 Choose an option: ").strip()
            print()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_all_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("👋 Exiting program. Happy reading!")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = LibraryManager()
    manager.menu()
