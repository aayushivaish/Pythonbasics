import os
import uuid
import json
script_dir = os.path.dirname(__file__)
rel_path = "Data/lib_categories.json"
cat_path = os.path.join(script_dir,rel_path)
book_rel_path = "Data/books.json"
books_path = os.path.join(script_dir, book_rel_path)


def admin():
    code = input("enter secret code ")
    admin_code = "9119"
    if code == admin_code:
        print("admin panel\n1.Add a book\n2.Add category\n ")
        choice = int(input())
        if choice == 1:
            add_book()
        if choice == 2:
            add_category()
    else:
        print('invalid code')
        return False 
        

def write_cat_json(data,filename=cat_path):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)

def write_book_json(data,filename=books_path):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)

def if_categoryexist(category_name,data):
  for category in data["categories"]: 
    if category['name']==category_name:
      return True
  return False


def add_category():
    f = open(cat_path,'r+')
    data = json.load(f) 
    category_name = input("Enter the category name ")
    if(if_categoryexist(category_name,data)):
        print("already exist")
    else:
        temp = {
            "category_name" : category_name,
            "id": str(uuid.uuid4())
        }
        data["categories"].append(temp)
        write_cat_json(data)
        print("category successfully added ")

def add_book():
    f = open(cat_path,"r+")
    cat_data = json.load(f) #category_data
    g = open(books_path, "r+")
    book_data = json.load(g) #books_data
    fetch_categories(cat_data)
    book_cat = int(input("select category "))
    book_name = input("Enter book name ")
    publish_year = input("enter year of publish ")
    author_name = input("enter name of the author ")
    test = {
        "name": book_name,
        "year": publish_year,
        "author": author_name,
        "category_id": cat_data["categories"][book_cat - 1]["id"],
        "is_available": True
    }
    book_data["books"].append(test)
    write_book_json(book_data)
    print("book added successfully ")
def fetch_categories(data):
    i = 1
    for category in data["categories"]:
        print("{}.{}".format(i,category["category_name"]))
        i = i+1


