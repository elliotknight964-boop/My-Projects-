import random 

def random_number(guess): 
    num = random.randint(1, 100) 
    attempts = 0 
    while True: 
        if guess > num: 
            guess = int(input("Too high, try again: "))
            attempts += 1
        elif guess < num: 
            guess = int(input("Too low, try again: "))
            attempts += 1
        else: 
            print(f"Congrats, you found the number!, total attempts: {attempts}")
            repeat = input("Would you like to guess a new number? Press x to quit: ") 
            if repeat == "x": 
                break 
            else: 
                num = random.randint(1, 100) 
                attempts = 1
                    
guess = int(input("Guess the number: "))
random_number(guess) 
