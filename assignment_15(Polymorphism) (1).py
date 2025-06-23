from Person import Person
from Student import Student
from Employee import Employee

def printElement(key):
    print(key.printPerson())

def errorDigits(var):
    print("ID must be a number. " + var + " is not a number")

def choiceType():
    while True:
        choice = int(input("Select type of information addition:" \
        "\n1. Person" \
        "\n2. Student" \
        "\n3. Employee "))
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 3:
            return 3
        else:
            print("Error Try again")

def addPerson(name, age, id, pepole_list):
    p = Person(name, id, age)
    pepole_list.append(p)

def addStudent(name, age, id, pepole_list):
    while True:
        faculty = input("Faculty: ")
        if not faculty.isdigit():
            break
        print("Error. Faculty cannot be a number.")
    while True:
        years = input("Year: ")
        if years.isdigit():
            break
        print("Error. year must be a number.")
    while True:        
        score_avg = input("Grade point average: ")
        if score_avg.isdigit():
            break
        print("Error.Grade must be a number.")
    s = Student(name, age, id, faculty, years, score_avg)
    pepole_list.append(s)

def addEmployee (name, age, id, pepole_list):
    while True:
        job = input("job: ")
        if not job.isdigit():
            break
        print("Error. job cannot be a number.")
    while True:        
        salary = input("Salary: ")
        if salary.isdigit():
            break
        print("Error.Salary must be a number.")
    e = Employee(name, age, id, job, salary)
    pepole_list.append(e)

def addItem(average_age, pepole_list):
    type_person = choiceType()
    id = input("ID: ")
    if not id.isdigit():
        errorDigits(id)
        return average_age
    
    p = searchID(pepole_list, int(id))
    if p != False:
        print("Error: ID already exists: ")
        printElement(p)
        return average_age       
    name = input("Name: ")
    if name.isdigit():
        print("Name must consist of letters.")
        return average_age    
    age = input("Age: ")
    if not age.isdigit():
        errorDigits("Age")
        return average_age  
    
    age = int(age) 
    total_people = len(pepole_list)
    new_total = total_people + 1
    average_age = (average_age * total_people + age) / new_total

    if type_person == 1:
        addPerson(name, age, id, pepole_list)
    elif type_person == 2:
        addStudent(name, age, id, pepole_list)
    elif type_person == 3:
        addEmployee(name, age, id, pepole_list)

    print("ID: [" + id + "] saved successfully")
    return average_age

def searchInList(people_list):
    id_to_search = input("Please enter the ID you want to look for: ")
    if not id_to_search.isdigit():
        errorDigits(id_to_search)
        return
    id_to_search = int(id_to_search)
    person_to_search = searchID(people_list, id_to_search)
    if(person_to_search):
        printElement(person_to_search)
    else:
        print("ID: " + str(id_to_search) + " not exist")

def searchID(people_list, id_to_search):
    for p in people_list:
        if int(p.getId()) == id_to_search:
            return p
    return False

def printAllNames(people_list):
    for counter, p in enumerate(people_list, start = 1):
        print(str(counter) + ": " + p.getName())

def printAllIDs(people_list):
    for counter, p in enumerate(people_list, start = 1):
        print(str(counter) + ": " + str(p.getId()))

def printPeopleList(people_list):
    for counter, key in enumerate(people_list, start = 1):
        print(str(counter), end = " ")
        printElement(key)

def printByIndex(people_list):
    index = input("Please enter the index of the entry you want to print: ")
    if not index.isdigit():
        errorDigits(index)
        return  
    index = int(index)
    if index < len(people_list):
        printElement(people_list[index])
    else:
        print("Error: Index out of range. The maximum index allowed is: " + str(len(people_list) - 1))

def menu():
    return input("1. Save a new entry " \
    "\n2. Search by ID" \
    "\n3. Print ages average " \
    "\n4. print all names" \
    "\n5. Print all IDs" \
    "\n6. Print all entries" \
    "\n7. Print entry by index " \
    "\n8. Exit" \
    "\nPlease enter your choice: ")

def exitMenu():
    choice = ""
    while (choice != "y") and (choice != "n"):
        choice = input("Are you sure? (y/n) ")
        if choice == "y":
            return True
    return False

def options(choice, average_age, people_list):
    press_enter = False
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 1:
        average_age = addItem(average_age, people_list)
    elif choice == 2:
        searchInList(people_list)
    elif choice == 3:
        print("The average age is: " + str(average_age)) 
    elif choice == 4:
        printAllNames(people_list)
    elif choice == 5:
        printAllIDs(people_list)
    elif choice == 6:
        printPeopleList(people_list)
    elif choice == 7:
        printByIndex(people_list)
    elif choice == 8:
        if exitMenu():
            return -1 
    elif str(choice) < str(1) or str(choice) > str(8):
        print("Please select a choice between 1 and 8")
    
    choice = input("Please press Enter to continue: ")
    return average_age

def start():
    people_list = []
    average_age = 0
    running = True
    while running:
        choice = menu()
        average_age = options(choice, average_age,people_list)  
        if average_age == -1:
            running = False

start()
