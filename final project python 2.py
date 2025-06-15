def printElement(dict, key):
     print("ID: " + str(key) + "\nName: " + str(dict[key][0]) + "\nAge: " + str(dict[key][1]))

def ErrorDigits(var):
    print("ID must be a numbers " + var + " is not a number")

def addItem(dict, average_age):
    ID  = input("ID: ")
    if not ID.isdigit():
        ErrorDigits(ID)
        return
    elif searchID(dict,int(ID)):
        print("Error: ID already exists: ")
        printElement(dict,int(ID))
        return       
    name = input("Name: ")
    if name.isdigit():
        print("Name must consist of letters.")
        return    
    age = input("Age: ")
    if not age.isdigit():
        ErrorDigits("Age")
        return  
    average_age = ((average_age * len(dict)) + int(age)) / (len(dict)+1)
    dict[int(ID)] = [name,int(age)]
    
    print("ID: [" + str(ID)  + "] saved successfuly")
    return average_age

def searchInDict(my_dict):
    ID_to_Search = (input("Please enter the ID you want to look for: "))
    if not ID_to_Search.isdigit():
        ErrorDigits(ID_to_Search)
        return
    ID_to_Search = int(ID_to_Search)
    if(searchID(my_dict, ID_to_Search)):
        printElement(my_dict,ID_to_Search)
    else:
        print("ID: " + str(ID_to_Search) + " not exist")

def searchID(dict, ID_to_Search):
    for key in dict.keys():
        if key == ID_to_Search:
            return True 
    return False 
    
def printAllNames(dict):
        counter = 1
        for counter, value in enumerate(dict.values()):
            print(str(counter) + ": "  + value[0])

def printAllIDs(dict):
        counter = 1
        for counter, key in enumerate(dict.keys()):
            print(str(counter) + ": " + str(key))
      
def printDict(dict):
    for counter, key in enumerate(dict.keys()):
        print(str(counter) + ". ID: " + str(key) + "\n\tName: " + str(dict[key][0]) + "\n\tAge: " + str(dict[key][1]))

def printByIndex(dict):
    index = input("Please enter the index of the entry you want to print: ")
    if not index.isdigit():
        ErrorDigits(index)
        return  
    index = int(index)
    dict_list = list(dict)
    if index < len(dict_list):
        key = dict_list[index] 
        printElement(dict,key)
        return
    else:
        print("Error: Index out of range. The maximum index allowed is: " + str(len(dict_list) - 1))
        
def menu():
    my_dict = {}
    average_age = 0
    exit_menu = ""
    while True:
        choice = input("1. Save a new entry " \
        "\n2. Search by ID" \
        "\n3. Print ages average " \
        "\n4. print all names" \
        "\n5. Print all IDs" \
        "\n6. Print all entries" \
        "\n7. Print entry by index " \
        "\n8. Exit" \
        "\nPlease enter your choice: ")
        press_enter = False
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                average_age = addItem(my_dict, average_age)
            elif choice == 2:
                searchInDict(my_dict)
            elif choice == 3:
                print("The average ages are: " + str(average_age))
            elif choice == 4:
                printAllNames(my_dict)
            elif choice == 5:
                printAllIDs(my_dict)
            elif choice == 6:
                printDict(my_dict)
            elif choice == 7:
                printByIndex(my_dict)
            elif choice == 8:
                while (exit_menu != "y") and (exit_menu != "n"):
                    exit_menu = input("Are you sure? (y/n)")
                if exit_menu == "y":
                    return
                exit_menu = ""
            elif choice < 1 or choice > 8:
                print("Please select a choice between 1 and 8")
            while not press_enter:
                choice = input("Please press Enter to continue: ")
                if choice == "":
                    press_enter = True
        else:
            ErrorDigits(choice)

menu()

