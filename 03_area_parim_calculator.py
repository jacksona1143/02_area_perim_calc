

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
                print()
                        

       
        
        

         


#code runs here

    width = num_check ( "Width: ")
    height = num_check ( "Height: ")
    print("width",width)
    print("height",height)
    area = width * height
    perimiter = (width + height)* 2
    print("Perimeter: ", perimiter)
    print("Area: ", area)
            
    num_check(question)

        