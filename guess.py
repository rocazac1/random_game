from random import randint
from IPython.display import clear_output

guessed = False                # Set the guessed to false
number = randint(0, 100)       # Pick random number between 0 - 100
guesses = 0                    # Set guess counter to 0


# while loop which loops betwen the lines until the number is guessed
#print(number)
while not guessed:
    ans = input("What numer am I thinking of between 0 - 100? ")       # Ask for user input
    guesses += 1                                                       # Add +1 to  guess when loop runs
    clear_output()
    try:                                          
        if int(ans) == number:
            print("You picked the right number: {}" .format(number))
            print("You guessed after {} tries!" .format(guesses))
            break
        
        elif int(ans) > number:
            print("The number is a bit too high")
        
        elif ans > 100:
            print("Number is out of range")
        
        else:
            print("The number is too small")
    
    except ValueError:                                              # Catches the wrong type of data 
        print("Please insert a number")
