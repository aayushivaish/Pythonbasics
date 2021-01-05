'''
We have to make Data Files(User,Books,Issue/Return Status)
User_login
User will select category from various genre.
User will select book.
If Book is available, user can issue it.
If Book is not available, user will return back to category menu.

'''

from auth import signup, login
from admin import admin
from actions import user_menu
from issue import issue
from book_return import return_book

def lib_mgmt():
    print("Welcome to library management ")
    print("select option\n1.signup\n2.login\n3.admin actions\n  ")
    option = int(input())
    if option == 1:
        signup()
    elif option == 2:
        users_auth, user_id = login()
        if users_auth == True:
            category_id, book_name, option = user_menu(user_id)
            if option == 1 and book_name != "N/A":
                issue(category_id,book_name,user_id)
            elif option == 2:
                return_book(user_id, book_name)
        else:
            print("Please try again")
            lib_mgmt()
    elif option == 3:
        admin()
    else:
        print("Please enter correct choice ")
        exit()









lib_mgmt() 