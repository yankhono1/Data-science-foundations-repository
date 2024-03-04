# Simple example to demonstrate a library checkout

# Define an inventory of books with their availability and borrowers
books_inventory = {'Book1': {'copies': 5, 'current_borrowers': []},
                   'Book2': {'copies': 3, 'current_borrowers': []}}

# Create a dictionary to store user information including borrowed books and fines
users_info = {'User1': {'borrowed_books': [], 'fines': 0},
              'User2': {'borrowed_books': [], 'fines': 0}}

# Function to check out a book for a user
def checkout_book(book_title, user_name):
    
    # Check if the book is available and user hasn't reached maximum borrow limit
    if books_inventory[book_title]['copies'] > 0 and len(users_info[user_name]['borrowed_books']) < 3:
        # Reduce available copies of the book by 1
        books_inventory[book_title]['copies'] -= 1
        # Add user to current borrowers of the book
        books_inventory[book_title]['current_borrowers'].append(user_name)
        # Add borrowed book to user's borrowed books list
        users_info[user_name]['borrowed_books'].append(book_title)
        
        # Print success message
        print(f"Book '{book_title}' checked out successfully.")
    
    else:
        # Print error message if book is not available or user has reached maximum borrow limit
        print("Error: Book not available or user has reached the maximum borrow limit.")

# Function to return a book borrowed by a user
def return_book(book_title, user_name):
    
    # Check if the book is borrowed by the user
    if book_title in users_info[user_name]['borrowed_books']:
        # Increase available copies of the book by 1
        books_inventory[book_title]['copies'] += 1
        # Remove user from current borrowers of the book
        books_inventory[book_title]['current_borrowers'].remove(user_name)
        # Remove returned book from user's borrowed books list
        users_info[user_name]['borrowed_books'].remove(book_title)
        
        # Print success message
        print(f"Book '{book_title}' returned successfully.")
    
    else:
        # Print error message if user hasn't borrowed this book
        print("Error: User has not borrowed this book.")

# Call the checkout_book function to check out a book for User1
checkout_book('Book1', 'User1')
