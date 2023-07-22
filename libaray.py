class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        
        self.books = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create labels and entry fields
        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.author_label = tk.Label(self.root, text="Author:")
        self.author_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.author_entry = tk.Entry(self.root)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Create buttons
        self.add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)
        
        self.search_button = tk.Button(self.root, text="Search Books", command=self.search_books)
        self.search_button.grid(row=2, column=1, padx=10, pady=5)
        
        self.display_button = tk.Button(self.root, text="Display Books", command=self.display_books)
        self.display_button.grid(row=2, column=2, padx=10, pady=5)
        
        # Create text widget
        self.text_widget = tk.Text(self.root, height=10, width=40)
        self.text_widget.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
        
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        
        if title and author:
            book = {"title": title, "author": author}
            self.books.append(book)
            
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            
            self.text_widget.insert(tk.END, "Book added successfully!\n")
        else:
            self.text_widget.insert(tk.END, "Please enter title and author.\n")
        
    def search_books(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        
        if title or author:
            self.text_widget.delete(1.0, tk.END)
            
            found_books = []
            for book in self.books:
                if (title and title.lower() in book["title"].lower()) or \
                   (author and author.lower() in book["author"].lower()):
                    found_books.append(book)
                    
            if found_books:
                self.text_widget.insert(tk.END, "Found books:\n")
                for book in found_books:
                    self.text_widget.insert(tk.END, f"Title: {book['title']}\nAuthor: {book['author']}\n\n")
            else:
                self.text_widget.insert(tk.END, "No books found.\n")
        else:
            self.text_widget.insert(tk.END, "Please enter title or author.\n")
        
    def display_books(self):
        self.text_widget.delete



