import random

def rock_paper_scissors(): 
    print("Press X to exit and view the score") 
    player = input("Choose:\n1.Rock\n2.Paper\n3.Scissors\nYou: ").lower()
    computer = random.randint(1, 3)
    com_win = "Computer wins!" 
    pla_win = "Player wins!" 
      
    if computer == 1: 
        computer = "rock"
        print(f"Computer: {computer.title()}\n")
    elif computer == 2: 
        computer = "paper" 
        print(f"Computer: {computer.title()}\n")
    else: 
        computer = "scissors"
        print(f"Computer: {computer.title()}\n") 
        
    if player == "rock" and computer == "scissors": 
        print(pla_win) 
    elif player == "paper" and computer == "rock": 
        print(pla_win)  
    elif player == "scissors" and computer == "paper": 
        print(pla_win)  
    elif player == computer: 
        print("Tie!") 
    else: 
        print(com_win)
       


rock_paper_scissors() 




