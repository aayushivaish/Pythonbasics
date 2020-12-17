import json
import uuid


f = open('users.json','r+')
data = json.load(f) 
#Array or List


# JSON or object


def welcomePage(data):
  print("welcome {}".format(data['name']))
  print(data)


def login(data):

  email = input("Enter your email ")
  password = input("enter your password ")

  for user in data['users']:
    if user['email'] == email:
      if user['password'] == password:
        print("LOGIN SUCESSFUL")
        welcomePage(user)
        break
      else:
        print("Wrong password")
        break
    else:
      print("user not found / please signup")
      signup(data)
      break

def if_userexist(email,data):
  for user in data["users"]: 
    if user['email']==email:
      return True
  return False

def write_json(data,filename='users.json'):
  with open(filename,'w') as file:
    json.dump(data,file,indent=4)
  



def signup(data):
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

login(data)








# Primary Key

# unique entity for a object
