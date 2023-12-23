from mimetypes import guess_all_extensions
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too high (h) if guess low (l) if guess is correct (c)").lower()    
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1    

    print(f'Yay, congrats. You have guessed the number {guess_all_extensions} correctly!!')


computer_guess(10000)