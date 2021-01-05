import os
import json
import datetime
from issue import update_book_issue_status
script_dir = os.path.dirname(__file__)
book_rel_path = "Data/books.json"
books_path = os.path.join(script_dir, book_rel_path)
issue_rel_path = "Data/issue.json"
issue_path = os.path.join(script_dir,issue_rel_path)

def write_issue_json(data,filename=issue_path):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)

def write_book_json(data,filename=books_path):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)

def select_return_book(user_id):
    f = open(issue_path,'r+')
    data = json.load(f)
    user_books = []
    for book in data["book_issue_data"]:
        if book["user"] == user_id and book["return_time"] == "N/A":
            user_books.append(book)
    print("select book to return ")
    for i in range(0,len(user_books)):
        print("{}.{}".format(i+1,user_books[i]["book"]))
    choice = int(input())
    return user_books[choice-1]

def return_book(user_id,book_name):
    f = open(issue_path,'r+')
    data = json.load(f)
    i = 0
    for book in data["book_issue_data"]:
        if book["user"] == user_id and book["book"] == book_name and book["return_time"]  == "N/A":
            temp ={
                "return_time": str(datetime.datetime.now())
            }
            book.update(temp)
            data["book_issue_data"][i] = book
        i = i+1
    write_issue_json(data)
    update_book_issue_status(True, book_name)
    print("book returned successfully ")







