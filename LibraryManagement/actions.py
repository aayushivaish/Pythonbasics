import os
import json
from book_return import select_return_book
script_dir = os.path.dirname(__file__)
rel_path = "Data/lib_categories.json"
cat_path = os.path.join(script_dir,rel_path)
book_rel_path = "Data/books.json"
books_path = os.path.join(script_dir, book_rel_path)



def user_menu(user_id):
    print("1.issue a book\n2.return a book\n ")
    option = int(input("enter choice "))
    if option == 1:
        print('select category')
        category_id = select_category()
        book_name = select_book(category_id)
        return category_id,book_name, option
    elif option == 2:       
        book = select_return_book(user_id)
        if book != "N/A":
            return book["category_id"],book["book"],option
        else:
            print("no books to return ")
            exit()



def select_category():
    f = open(cat_path,'r+')
    data = json.load(f) 
    i = 1
    for category in data["categories"]:
        print("{}.{}".format(i,category["category_name"]))
        i = i + 1
    cat = int(input())
    return data["categories"][cat-1]["id"]

def select_book(category_id):
    f = open(books_path,'r+')
    data = json.load(f)
    book_list = []
    for book in data["books"]:
        if book["category_id"] == category_id and book["is_available"] == True:
            book_list.append(book)
    if len(book_list) == 0:
        print("no books available ")
        return "N/A"
    else:
        print("select the book ")
        for i in range(0,len(book_list)):
            print("{}.{}".format(i+1,book_list[i]["name"]))
        book_index = int(input())
        return book_list[book_index-1]["name"]




    
    

        

        
