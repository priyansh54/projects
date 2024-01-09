import random

rsp = ['r', 'p', 's']
user = input("r for rock p for paper s for scissors: ")
computer = random.choice(rsp)

def rock_paper_scissor():
    if user == computer:
      print("it is a tie")
    
    elif user == "r" and computer == "s":
      print("you win")
    
    elif user == "p" and computer == "r":
      print("you win")  
    
    elif user == "s" and computer == "p":
      print("you win")  
    
    else:
      print("you lost, computer win")  

rock_paper_scissor()
