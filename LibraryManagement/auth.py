import json
import uuid
import os
script_dir = os.path.dirname(__file__)
rel_path = "Data/lib_users.json"
abs_path = os.path.join(script_dir,rel_path)

def if_userexist(email,data):
  for user in data["users"]: 
    if user['email']==email:
      return True
  return False

def write_json(data,filename=abs_path):
  with open(filename,'w') as file:
    json.dump(data,file,indent=4)
  

def signup():
    f = open(abs_path,'r+')
    data = json.load(f) 
    name = input('Enter your name ')
    email = input('Enter your email ')
    password = input('Enter your password ')
    age = int(input('Enter your age '))

    if(if_userexist(email,data)):
        print('user already exist')
        exit()
    else:
        temp={
            "name": name,
            "id": str(uuid.uuid4()),
            "email": email,
            "password": password,
            "age": age

        }
        data['users'].append(temp)
        write_json(data)
        print('signup successful')

def login():
     f = open(abs_path,'r+')
     data = json.load(f) 
     email = input("Enter your email ")
     password = input("enter your password ")
     for user in data['users']:
         if user['email'] == email:
             if user['password'] == password:
                 print("LOGIN SUCCESSFUL")
                 return True, user["id"]
             else:
                print("Wrong password")
                return False
         else:
            print("user not found / please signup")
            break