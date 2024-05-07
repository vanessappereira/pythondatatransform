# Creation of a booklist with Title, Year, Author, Collection

import os
import pandas as pd
import matplotlib.pyplot as plt

global data
listBooks = {"Title": [], "Author": [], "Year": [], "Collection": []}
df = pd.DataFrame(listBooks)


def list_books():
    # Verify if there are books
    if df.empty:
        print("There are no books registered.")
    else:
        print("List of books registered: \n", df)


def search_menu(selection):
    try:
        if selection == "1":
            title = input("Please write the title you want to search: ")
            if not title:
                raise ValueError
            filteredBooks = df[df["Title"].str.contains(title, na=False)]
            if filteredBooks.empty:
                print(f"There is no book with the title '{title}'.")
            else:
                print(f"Listed Books with the title '{title}': \n", filteredBooks, "\n")
        elif selection == "2":
            collection = input("Please write the collection you want to search: ")
            if not collection:
                raise ValueError
            filteredCollection = df[df["Collection"].str.contains(collection, na=False)]
            if filteredCollection.empty:
                print(f"There is no book with the collection '{collection}'.")
            else:
                print(
                    f"Listed Books within the collection '{collection}': \n",
                    filteredCollection,
                    "\n",
                )
        elif selection == "3":
            year = int(input("Please write the year you want to search: "))
            if not year:
                raise ValueError
            filteredYear = df[df["Year"].str.contains(year, na=False)]
            if filteredYear.empty():
                print(f"There is no book with the year '{year}'.")
            else:
                print(f"Listed Books within the year '{year}': \n", filteredYear, "\n")
        elif selection == "4":
            author = input("Please write the author you want to search: ")
            if not author:
                raise ValueError
            filteredAuthor = df[df["Author"].str.contains(author, na=False)]
            if filteredAuthor.empty():
                print(f"There is no book listed made by '{author}' ")
            else:
                print(f"Listed Books made by '{author}': \n", filteredAuthor, "\n")
        elif selection == "0":
            menu()
        else:
            print("Invalid option! Please select a correct option.")
            return
    except ValueError:
        print("Invalid response, returning to menu...")
        return menu()


def book_management(number):
    try:
        if number == "1":
            bookTitle = input("Please write the title of the book you want to add: ").title()
            if not bookTitle:
                raise ValueError

            collection = input(
                "Please write which collection the book belongs to: ").title()
            if not collection:
                raise ValueError

            year = int(input("Please write which year the book was released: ")).title()
            if not year:
                raise ValueError

            author = input("Please write the author of the book: ").title()
            if not author:
                raise ValueError

            df.loc[len(df)] = [bookTitle, collection, year, author]
            print("Book added successfully")
        elif number == "2":
            bookTitle = input(
                "Please write the title of the book you want to remove: ").title()
            if not bookTitle:
                print(f"The book {bookTitle} doesn't exist in the list.")
                return
            else:
                confirmation = input(f"Está prestes a remover o livro {bookTitle} \n Pretende continuar? S/N ")
                if confirmation.lower() == "n":
                    print("A operação não foi realizada.")
                    return
                else:
                    removeBook = df[df["Title"] == bookTitle]
                    if removeBook.empty():
                        print("Book not found.")
                        return
                    df.drop(removeBook.index, inplace=True)
                    print("Book removed successfully")
        elif number == "0":
            menu()
        else:
            print("Invalid option! Please select a correct option.")
            return
    except ValueError:
        print("The response cannot be empty!")


def book_graphic():
    # Graphic bar book colletion, how many are with the same name on collection and the label is the title
    global df
    # Calculate the number of books in each collection
    collectionCounts = df["Collection"].value_counts()
    # Verify if exists data
    if len(collectionCounts) == 0:
        print("No data to show. \n Returning to menu... \n")
        return menu()
    # Create a pie chart
    plt.pie(collectionCounts.values, labels=collectionCounts.index, autopct="%1.1f%%")
    plt.title("Percentage of book in each collection")
    plt.axis("equal")
    plt.show()


def generate_file():
    # Generate a CSV file with the information on dataframe
    print("Generate file Menu")
    save_File = input("Please insert the name of the file: ").title()

    # Check if the file already exists
    if os.path.exists(f"{save_File}.csv"):
        print("File already exists.")
    else:
        # Save the file
        df.to_csv(f"{save_File}" + ".csv", index=False)
        print("File saved sucessfully.")


def load_file():
    df
    try:
        # Load the file
        load_File = input("Please insert the name of the file: ").title()
        # Check if the file exists
        if os.path.exists(f"{load_File}.csv"):
            df = pd.read_csv(f"{load_File}.csv")
            print("File loaded sucessfully.")
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        print("File not found, please go to the option to generate.")
        menu()


def menu():
    while True:
        print(
              "========== Welcome! ==========\n"
            + "==    1. Search a book      ==\n"
            + "==    2. List all books     ==\n"
            + "==    3. Book Management    ==\n"
            + "==    4. View graphic       ==\n"
            + "==    5. File Management    ==\n"
            + "==    0. Exit program       ==\n"
            + "==============================\n")
        option1 = input("Please select an option: ")
        if option1 == "1":
            print(
                  "========== Search ==========\n"
                + "==   1. By title          ==\n"
                + "==   2. By collection     ==\n"
                + "==   3. By year           ==\n"
                + "==   4. By author         ==\n"
                + "==   0. Previous Menu     ==\n"
                + "============================\n"
            )
            option2 = input("Please select an option: ")
            search_menu(option2)
        elif option1 == "2":
            list_books()
        elif option1 == "3":
            print(  "====== Book Management ======\n"
                  + "==     1. Add a book       ==\n" 
                  + "==     2. Remove a book    ==\n" 
                  + "==     0. Previous Menu    ==\n"
                  + "=============================\n")
            
            option3 = input("Please select an option: ")
            if option3 == "1":
                book_management(1)
            elif option3 == "2":
                book_management(2)
            elif option3 == "3":
                book_management(3)
            elif option3 == "0":
                menu()
            else:
                print("Invalid option! Please select a correct option.")
                return
        elif option1 == "4":
            book_graphic()
        elif option1 == "5":
            print("========== File Management ==========\n"
                + "==    1. Save list to a file       ==\n"
                + "==    2. Load list from a file     ==\n"
                + "==    0. Previous Menu             ==\n"
                + "=====================================\n"
            )
            option4 = input("Please select an option: ")
            if option4 == "1":
                generate_file()
            elif option4 == "2":
                load_file()
            elif option4 == "0":
                menu()
            else:
                print("Invalid option! Please select a correct option.")
                return
        elif option1 == "0":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid option! Please select a correct option.")
            return

menu()