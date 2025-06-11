import time
print("Hello, This is my final project")
name = input("What is your name? ")
print("Hi " + name +", nice to meet you\nThis is a special calculator, I would need two numbers from you")
num_1 = int(input("First number "))
num_2 = int(input("Second number "))
result = None
error = False
print("Thank you for putting in your numbers, " + str(num_1) + " and " + str(num_2) +"\nI can see that the first number", end= "")
if(num_1%2 == 0 and num_2%2 == 0):
    print(" And the second is even")
elif(num_1%2 == 1 and num_2%2 == 1):
    print(" And the second is odd")
else:
    if(num_1%2 == 0 and num_2%2 == 1):
        print(" even And the second is odd")
    else:
        print(" odd And the second is even")
Operator = input("Operator (+, -, *, /): ")
if(Operator == "+"):
    result = int(num_1) + int(num_2)
elif(Operator == "-"):
        result = int(num_1) - int(num_2)
elif(Operator == "*"):
    result = int(num_1) * int(num_2)
elif(Operator == "/"):
    if num_2 == 0:
        error = True
    else:
        answer = input("You chose division, should the result be integer? (y/n) ")
        if answer == "y":
            result = num_1 // num_2
        else:
            result = num_1 / num_2
else:
    error = True
if(error == True):
    if(Operator == "/" and num_2 == 0):
        print("Error: num_2 is zero")
    else:
        print("Error: Operator " + Operator + " is not supported")
    print("An error has occurred, please try again.")
else:
    print(str(num_1) + " " + str(Operator) + " " + str(num_2) + " = " + str(result))

print("Thank you " + name + " for using the calculator on " + time.ctime() )

