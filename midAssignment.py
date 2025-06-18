import os
import json
import pandas as pd

def printElement(row):
    print("ID: " + str(row['ID']) + "\nName: " + str(row['Name']) + "\nAge: " + str(row['Age']))
def errorDigits(var):
    print("ID must be a number. " + var + " is not a number")

def addItem(my_data, average_age, id_list):
    id = input("ID: ")
    if not id.isdigit():
        errorDigits(id)
        return average_age
    elif searchID(my_data, int(id)):
        print("Error: ID already exists: ")
        printElement(my_data, int(id))
        return average_age       
    name = input("Name: ")
    if name.isdigit():
        print("Name must consist of letters.")
        return average_age    
    age = input("Age: ")
    if not age.isdigit():
        errorDigits("Age")
        return average_age  
    
    id = int(id)
    age = int(age) 
    total_people = len(my_data)
    new_total = total_people + 1
    average_age = (average_age * total_people + age) / new_total
    
    with open("C:\\Users\\idoel\\OneDrive\\שולחן העבודה\\confi.json") as json_file:
        loaded = json.load(json_file)
    

    new_row = {
        loaded['ID']: id,
        loaded['Name']: name,
        loaded['Age']: age
    }
    my_data.append(new_row)
    id_list.append(id)
    print("ID: [" + str(id) + "] saved successfully")
    return average_age

def searchInDict(my_data):
    id_to_search = input("Please enter the ID you want to look for: ")
    if not id_to_search.isdigit():
        errorDigits(id_to_search)
        return
    id_to_search = int(id_to_search)
    if not searchID(my_data, id_to_search):
        print("ID: " + str(id_to_search) + " not exist")

def searchID(my_data, id_to_search):
    for row in my_data:
        if row['ID'] == id_to_search:
            printElement(row)
    return False

def printAllNames(my_data):
    for index, row in enumerate(my_data):
        print(str(index) + ": " + str(row['Name']))

def printAllIDs(my_data):
    for index, row in enumerate(my_data):
        print(str(index) + ": " + str(row['ID']))

def printDict(my_data):
    for row in my_data:
        printElement(row)

def printByIndex(my_data, id_list):
    index = input("Please enter the index of the entry you want to print: ")
    if not index.isdigit():
        errorDigits(index)
        return  
    index = int(index)
    if index < len(id_list):
        printElement(my_data[index])
    else:
        print("Error: Index out of range. The maximum index allowed is: " + str(len(id_list) - 1))

def saveOnCsv(my_data):
    df = pd.DataFrame(my_data)
    file_name = input("what is your output file name? ")
    df.to_csv(file_name, index = False)
    print(file_name + " Created successfully")

def menu():
    return input("1. Save a new entry " \
    "\n2. Search by ID" \
    "\n3. Print ages average " \
    "\n4. print all names" \
    "\n5. Print all IDs" \
    "\n6. Print all entries" \
    "\n7. Print entry by index " \
    "\n8. Save file"\
    "\n9. Exit" \
    "\nPlease enter your choice: ")

def exitMenu():
    choice = ""
    while (choice != "y") and (choice != "n"):
        choice = input("Are you sure? (y/n) ")
        if choice == "y":
            return True
    return False


def options(choice, my_data, average_age, id_list):
    press_enter = False
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 1:
        average_age = addItem(my_data, average_age, id_list)
    elif choice == 2:
        searchInDict(my_data)
    elif choice == 3:
        print("The average age is: " + str(average_age)) 
    elif choice == 4:
        printAllNames(my_data)
    elif choice == 5:
        printAllIDs(my_data)
    elif choice == 6:
        printDict(my_data)
    elif choice == 7:
        printByIndex(my_data, id_list)
    elif choice == 8:
        saveOnCsv(my_data)
    elif choice == 9:
        if exitMenu():
            return -1 
    elif choice < 1 or choice > 9:
        print("Please select a choice between 1 and 8")
    
    choice = input("Please press Enter to continue: ")
    return average_age

def start():
    my_data = []
    id_list = []
    average_age = 0
    running = True
    while running:
        choice = menu()
        average_age = options(choice, my_data, average_age, id_list)  
        if average_age == -1:
            running = False

start()