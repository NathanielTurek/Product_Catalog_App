import file_handling as fh
import products as pr
# login and sign up

ADMIN_EMAIL= "1abc@"
ADMIN_PASSWORD = "1abc"

def unique_email(email):
    data = fh.read("Database/users.txt")
    return email not in data


def signup():
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    country = input("Enter county: ")

    data = f"\n{email}\n{password}\n{name}\n{age}\n{country}"
    if unique_email(email) and check_password(password):
        fh.write("Database/users.txt", data)
        print("SIGN UP SUCCESSFUL!")
    else:
        print("Inncorect input, please try again. ")

def check_password(password):
    if len(password) >= 8 :
        for char  in password :
            if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) :
                return True
        
    return False

def check_email(email) :
    return unique_email(email) and "@" in email 
    

def login(email, password) :
    data = fh.read("Database/users.txt")
    data = data.split("-")
    for user in data :
        user_data = user.split("\n")
        if user_data[0] == email and user_data[1] == passsword :
            return True
    return False
        
# password requirements
# must contains at least 8 characters
# Must have at least one Upper Case and one lower Case letter

# Log in functionality


def user_options() :
    print("Enter [1] to search for a product")
    print("Enter [2] to view all products ")
    choice = int(input(">>"))
    if choice == 1 :
        searched_item = pr.search_product(input("Enter your search "))
        print(searched_item)
        user_options()
    elif choice == 2 :
        viewed_products = pr.view_products()
        print(viewed_products)
        user_options()
    else :
        print("wrong input ")
    

def admin_options() :
    print("Enter [1] to search for a product ")
    print("Enter [2] to view all products ")
    print("Enter [3] to add a product ")
    print("Enter [4] to deleta a product ")
    print("Enter [5] to update a product ")
    choice = int(input(">>"))
    if choice == 1 :
        searched_item = pr.search_product(input("Enter your search "))
        print(searched_item)
        admin_options()
    elif choice == 2 :
        viewed_products = pr.view_products()
        print(viewed_products)
        admin_options()
    elif choice == 3 :
        pr.add_product()
        admin_options()
    elif  choice == 4 :
        pr.delete_product(input("Enter the name of the product you want to delete "))
        admin_options()
    elif choice == 5 :
        name = input("Enter the name of the product you want to update: ")
        searched_item = pr.search_product(name)
        print(searched_item)
        updated_name = input("Enter updated product name : ")
        updated_description = input("Enter updated describtion : ")
        updated_rating = float(input("Enter updated detail 2: "))
        updated_price = float(input("Enter updated price : "))
        updated_category = input("Enter updated category : ")
        updated_data = f"{updated_name}\n{updated_description}\n{updated_rating}\n{updated_price}\n{updated_category}\n"
        pr.update_product(name, updated_data)
        print(name, "was updades succesfully ")
        admin_options()
    else :
        print("wrong input ")


while True:
    print("Enter [1] to Login")
    print("Enter [2] to Sign Up")
    print("Enter [3] to Exit")

    # input
    choice = int(input(">>"))
    if (choice == 1):
        email = input("enter your email ")
        passsword = input("enter your password ")
        if email == ADMIN_EMAIL and passsword == ADMIN_PASSWORD :
            print("logged in as admin")
            admin_options()
        else :
            
            if login(email, passsword) :
                user_options()
            else :
                print("Wrong credentials ")
    elif (choice == 2):
        signup()
    elif (choice == 3):
        break
    else:
        print("Invalid choice")


# Requriements for the project
# Product Catalog Project

# Actors
# User:
# 1. View all the products
# 2. Add a product the cart
# 2. Purchase the product
# 3. Search a product

# Admin
# Add a new product
# Modify an existing product
# Delete a product

# Files
# users (for authentication)
# products (for product details)
# cart (for mainting the cart items)

# Product Model
# name
# description
# rating
# price
# type

# Cart Model
# user_email
# [names_of_products]


#do admin for homework