import os
import statistics
import time
import random
# import functions  # Create your own modules

# How to store the data in a text file

# r -> read
# w -> write
# a -> append
# x -> creates a new file -> throws and error if file already exists

# Write the data to a text file


def write(filename, data):
    file = open(filename, "a")
    file.write(f"{data}\n-")
    file.close()

# Read the data from the file


def read(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    return data


def overwrite(filename, data):
    file = open(filename, "w")
    file.write(f"{data}")
    file.close()


# call the write() function
# write("sample.txt", "The class is awsome!")
data = read("Database/users.txt")

# Delete a file
# os.remove("sample.txt")

# -----------------------------
nums = [1, 2, 4, 1, 11, 25, 22, 11, 2, 6]
# Mean = add all elements of list / length of list
# print(statistics.mean(nums))
# # time.sleep(5)
# print("Hi")

# print(random.randint(1, 100))

# print(functions.greetings())
