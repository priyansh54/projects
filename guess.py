
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            Guess = random.randint(low, high)
        else:
            Guess = low
        feedback = input(f"is {Guess} too high (h) if guess low (l) if guess is correct (c)").lower()    
        if feedback == "h":
            high = Guess - 1
        elif feedback == "l":
            low = Guess + 1    

    print(f'Yay, congrats. You have guessed the number {Guess} correctly!!')


computer_guess(100)