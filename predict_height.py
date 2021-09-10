import os

    
def predict_height():

 while True:

    name = str(input("Please enter your name to predict your child's height: "))
    welcome = print(f"Welcome {name}")
    mom = int(input("Enter mom's height in cm: "))
    dad = int(input("Enter dad's height in cm: "))
    total = int(mom + dad)
    sex = input("Choose your sex f or m: ")
    if sex == "m":
        print(f"your height will be: {int(total / 2) + 13}cm {os.linesep}")
    elif sex == "f":
        print(f"your height will be: {int(total / 2)}cm  {os.linesep}")
    else:
        print(f"Enter a valid option {os.linesep}")

predict_height()
