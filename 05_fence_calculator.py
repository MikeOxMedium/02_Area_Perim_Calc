# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing
    print("press put in the width and height")

    # Calulate perimeter (width + height) x 2
    width=num_check("width: ")
    height=num_check("height: ")
    cost=num_check("cost per meter: ")

    # fencing (perimeter x price / meter)
    perimeter= 2 * (width + height)
    # print(perimeter)
    price = perimeter * cost

    print("the perimeter is {} m".format(perimeter))
    print("the cost per meter is ${}".format(price))

    # Output the perimeter and cost of the fencing


    keep_going = input("Press <enter> to keep going or any key to quit")
    
print()
print("Thanks for using the Fencing cost calculator")

        
    
    