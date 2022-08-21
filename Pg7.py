# random number generator that generates random numbers between 1 and 6 (simulates a dice).

import random # module to generate random values

def randGen(guess): # function to check users input with generated value 
    genNum = random.randint(1,6) # number generated
    if guess == genNum: 
        print(f'Congrats !!! {genNum} is the correct guess.')
    else:
        print(f'OOPS !!! your number {guess} does not match with {genNum}')

print("Enter a number between 1 and 6 to check if your guess was right.")

randGen(int(input("Your Guessed Number : "))) # calling the function along with users input