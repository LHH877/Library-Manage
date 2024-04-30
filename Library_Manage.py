#LIM HENG HOE
#TP077567

def addBook(filename, title, author): # Define addbook function.
    if not title or not author: # If user input is empty, print "Please enter both title and author".
        print("Please enter both title and author.")
    else: # open library.txt, write user input book title and author in file.
        with open(filename, "a") as file:
            file.write(f"{title}, {author}\n")
        print(f"Added book: {title} by {author}") #print title and author of added book.


def updateBook(filename, old_title, old_author, new_title, new_author):
    if not old_title or not old_author: # If user input is empty, print "Please enter both title and author".
        print("Please enter the title and author of book to be updated.")
    elif not new_title or not new_author: # If user input is empty, print "Please enter the new title and the new author".
        print("Please enter the new title and the new author.")
    else: # Open library.txt and read each line.
        with open(filename, "r") as file:
            lines = file.readlines()

        found = False # Assume that the book was not found initially.
        with open(filename, "w") as file: #Open library.txt and write.
            for line in lines: # For loop to iterate each line of library.txt.
                book_data = line.strip().split(", ") # Remove spacing before and after each line, split title and author with a comma.
                if len(book_data) == 2: # Check if book_data has two elements
                    book_title, book_author = book_data #Unpack book_data into book_title and book_author
                    if book_title == old_title and book_author == old_author: #Check if book_title and book_author matched with old_title and old_author.
                        file.write(f"{new_title}, {new_author}\n") #Update old book data with new book data
                        print(f"Updated book: {new_title} by {new_author}") #Print message to inform user about updated book.
                        found = True #Set found variable as true so that if not found will not execute.
                    else:
                        file.write(line) #If book data does not match user input, system writes the original line back to the file.

        if not found: #Check whether found is still false, if yes, print the below statement.
            print(f"No book matching '{old_title}' by '{old_author}' found in the library.")


def viewAllBook(filename): # Define viewallBook function.
    with open(filename, "r") as file: # Open library.txt and read lines from the file
        books = file.readlines()
    if not books: # If books is empty after reading from library.txt, print "The library is empty."
        print("The library is empty.")
    else: # If books is not empty,
        print("Books in the library:") # If books are not empty, enumerates and prints each book data with a numeric index.
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book.strip()}")


def searchBook(filename, keyword): #Define searchBook
    if not keyword: # If user input is empty, print "The field must not be empty".
        print("The field must not be empty.")
    else: # Open library.txt, read, and store the book data in books variable.
        with open(filename, "r") as file:
            books = file.readlines()

        found_books = [] #Create an empty list to store books that match with user's input.
        #Use for loop to match keyword with stored book data, use ".lower" to make search case-insensitive.
        for book in books:
            if keyword.lower() in book.lower():
                found_books.append(book.strip()) #Remove leading and trailing whitespace
        #Check if books match with search criteria
        if found_books:
            print(f"Books containing '{keyword}':") # Print book title that matches with keyword
            # For loop to print each matching book starting from 1.
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. {book}")
        #Print message below in console if no book title matches with keyword.
        else:
            print(f"No books found containing '{keyword}'.")


def deleteBook(filename, title, author):
    # If user input is empty, print "Please enter both title and author".
    if not title or not author:
        print("Please enter both title and author.")
    # Open library.txt, read, and store the book data in books variable.
    else: # Read book data from library.txt.
        with open(filename, "r") as file:
            lines = file.readlines()


        removed = False # Assume removed to be False initially
        with open(filename, "w") as file: #Open library.txt and write.
            for line in lines: # For loop to iterate each line of library.txt
                book_data = line.strip().split(", ") # Remove spacing before and after each line, split title and author with a comma.
                if len(book_data) == 2: # Check if book_data has two elements.
                    book_title, book_author = book_data #Unpack book_data into book_title and book_author.
                    # Check if user input match with book data in library.txt
                    if book_title == title and book_author == author:
                        removed = True #Set removed variable as true so that else will not execute.
                    else:
                        file.write(line) #If book data does not match the one to be updated, this writes the original line back to the file.

        if removed: #If removed became True, print the message below.
            print(f"Removed book: {title} by {author}")
        else: #If removed remained False, print the message below.
            print(f"No book matching '{title}' by '{author}' found in the library.")


def main(): #Define main function
    filename = "library.txt" #Assign a txt file named "library" to filename variable.
    try: #Open a txt file named "library", If file exists, then read and pass
        with open(filename, "r") as file:
            pass
    except FileNotFoundError: #If file does not exist, create an empty file
        with open(filename, "w") as file:
            pass
    except Exception as e: #If encounter any other error, then print the message below.
        print(f"An error occurred while accessing the file: {e}")
        return

    while True: #Continue to ask for user's choice of operation until user exits.
        choice = input("****************\n" #Menu of choices for user to choose operation.
                       "Main Menu\n"
                       "1. Add Book\n"
                       "2. Update Book\n"
                       "3. List all book\n"
                       "4. Search Book\n"
                       "5. Remove Book\n"
                       "6. Exit\n"
                       "****************\n"
                       "Enter your choice: ")


        if choice == "1": # If user input = "1", ask for title and author input, then run function addbook.
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            addBook(filename, title, author)

        elif choice == "2": # If user input = "2", ask for old_title, old_author, new_title, new_author input, then run function updateBook.
            old_title = input("Enter the title of the book to update: ")
            old_author = input("Enter the author of the book to update: ")
            new_title = input("Enter the updated title: ")
            new_author = input("Enter the updated author: ")
            updateBook(filename, old_title, old_author, new_title, new_author)

        elif choice == "3": # If user input = "3", run function viewAllBook.
            viewAllBook(filename)

        elif choice == "4": # If user input = "4", ask for keyword input, then run function searchBook.
            keyword = input("Enter a keyword to search for books: ")
            searchBook(filename, keyword)

        elif choice == "5": # If user input = "5", ask for title and author input, then run function deleteBook.
            title = input("Enter the title of the book to remove: ")
            author = input("Enter the author of the book to remove: ")
            deleteBook(filename, title, author)

        elif choice == "6": # If user input = "6", print "Thank you. Goodbye", then exit the while loop.
            print("Thank you. Goodbye")
            break

        else: # If user input choices other than 1 to 6, print "Invalid choice. Please try again.", and rerun while loop.
            print("Invalid choice. Please try again.")


main() #run main function
