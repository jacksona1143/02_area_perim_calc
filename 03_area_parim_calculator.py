

#functions

#check if number is greater than zero
def num_check (question):
    valid = False
    while not valid: 
        
        error = "Please enter a value more than 0"

        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                

        except ValueError:
                print("Please enter a number")
                print()
                        


#code runs here

keep_going = ""
while keep_going == "":


    width = num_check ( "Width: ")
    height = num_check ( "Height: ")
    print("width",width)
    print("height",height)
    area = width * height
    perimeter = (width + height)* 2
    print()
    print()
    print("Perimeter: {:.2f} units" .format(perimeter))
    print("Area: {:.2f} square units".format(area))

    keep_going = input("Press <enter> to keep going or any key to quit")

    

   

    
print()
print("Thanks for using area/perimeter calculator")
        