
from re import A

#testing github

valid = False

error = "Please enter a value more than 0"

while not valid:
    try:
        response = float(input("Enter a number: "))

        if response > 0:
            valid = True

        else:
                print(error)
                print()

    except ValueError:
        print(error)
        

        