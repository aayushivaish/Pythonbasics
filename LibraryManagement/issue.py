import os
import json
import datetime
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



def issue(category_id,book_name,user_id):
    f = open(issue_path,'r+')
    data = json.load(f) 
    temp ={
        "user": user_id,
        "category_id": category_id,
        "book": book_name,
        "issue_time": str(datetime.datetime.now()),
        "return_time": "N/A"
    }
    data["book_issue_data"].append(temp)
    write_issue_json(data)
    print("issued successfully ")
    update_book_issue_status(False, book_name)


def update_book_issue_status(value, book_name):
    g = open(books_path,"r+")
    data = json.load(g)
    i = 0
    for book in data["books"]:
        if book["name"] == book_name:
            temp = {
                "is_available": value
            }
            book.update(temp) 
            data["books"][i] = book
        i = i+1
    write_book_json(data)
    




    


