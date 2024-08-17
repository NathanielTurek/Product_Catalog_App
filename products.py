import file_handling as fh


#apple
#this is the best product
#3.0
#3.00
#food 


def view_products() :
    all_products = fh.read("Database/products.txt")
    return all_products


def unique_product(name):
    data = fh.read("Database/products.txt")
    return name not in data


def add_product():
    name = input("Product Name: ")
    desc = input("Product descripton: ")
    rating = float(input("Product rating: "))
    price = float(input("Product price: "))
    type = input("Product type: ")

    data = f"\n{name}\n{desc}\n{rating}\n{price}\n{type}"
    if (unique_product(name)):
        fh.write("Database/products.txt", data)
        print(f"{name} ADDED SUCCESSFUL!")
    else:
        print("Please enter a unique product name")

#add_product()


def search_product(name):
    data = fh.read("Database/products.txt")
    list_products = data.split("-")
    for product in list_products:
        if (name in product):
            return product

    return "product does not exist"


# print(search_product("apple"))


def update_product(name, updated_data):
    data = fh.read("Database/products.txt")
    new_data = data.split("-")
    # for each product in the new data, if the product exists
    # then you insert it into the list

    for i in range(len(new_data)):
        if name in new_data[i]:
            new_data[i] = updated_data

            new_data = "-\n".join(new_data).strip()
            # tiny bit of change '\n'
            fh.overwrite("Database/products.txt", new_data)

    return "product doesn't exist"


#update_product("mango", 'apple\nthis is apple\n4.00\n2.12\nfruit\n')

# print("\n-".join(['Candy\nthis is cadny\n3.00\n1.12\nfood',
#       '\nsoda\nthis is soda\n4.5\n2.50\ndrink\n', '']))


def delete_product(name):
    data = fh.read("Database/products.txt")
    new_data = data.split("-")
    for product in new_data:
        if name in product:
            new_data.remove(product)
    updated_data = ("-".join(new_data)).strip()
    print(updated_data)
    fh.overwrite("Database/products.txt", updated_data)


# delete_product("Candy")

list_products = ['Soda\nthis is soda\n4.00\n12.1\nfood',
                 'Candy\nthis is cadny\n3.00\n1.12\nfood']

for product in list_products:
    if ("Soda" in product):
        list_products.remove(product)
        # data = product.split("\n")
        # product_dict = {
        #     'name':  data[0],
        #     'desc':  data[1],
        #     'rating':  data[2],
        #     'price':  data[3],
        #     'type':  data[4],
        # }
        # print(product_dict)

# print(list_products)
