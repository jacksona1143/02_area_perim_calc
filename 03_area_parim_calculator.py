
from re import A
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
                        print(error)
                        

       
        
        

         


#code runs here

    width = num_check ( "Width: ")
    height = num_check ( "Height: ")
    print()
    print("Width", width)
    print("Height", height)
    print()
            

        