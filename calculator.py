def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y
def main():
    x = int(input("Enter first number ")) 
    y = int(input("Enter second number "))
    print("CALCULATOR MENU\n1.add\n2.subtract\n3.multiply\n4.divide\n")
    choice = int(input("Enter choice "))

    if choice == 1:
        ans= add(x,y)
    elif choice == 2:
        ans= sub(x,y)
    elif choice == 3:
        ans= multiply(x,y)
    elif choice ==4:
        ans= divide(x,y)

    print(ans)
if __name__ == "__main__":
    main()
    