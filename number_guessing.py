
import random

def mode():
    
    print("🎯 Welcome to the Number Guessing Game!")   
    print("Please enter the gamemode.")
    print("Type 'e' for Easy Mode")
    print("Type 'm' for Medium Mode")
    print("Type 'h' for Hard Mode")
    gamemode=input("Gamemode: ")
    if gamemode=="e":
        play(1,20)
    elif gamemode=="m":
        play(1,40)
    elif gamemode=="h":
        play(1,80)


def leave():
    playagain=input("Do you want to play again? (y/n) - ")
    if playagain=="y":
        mode()
    elif playagain=="n":
        print("Thank you for playing, Have a nice day!")

    
def play(para_min,para_max):   
    
    print("I have selected a number between", para_min , "and" , para_max , "(inclusive).")
    print("Your task is to guess the number.")
    print("Type 'g' anytime if you want to give up and reveal the answer.")
    print("Let's begin!\n")
    
    num = random.randint(para_min, para_max)

    attempts=0

    while True:
        feed=input("Guess the Number: ")
        if feed=="g":
            print("The number i guessed was", num)
            return leave()
        try:
            guess=int(feed)
        except ValueError:
            print("Please enter a valid Number")
            continue
        attempts=attempts+1
        if guess==num:
            print("You Guessed the number correctly")
            print("Number of attempts: ", attempts)
            return leave()

        difference=guess-num
        if difference>0:
            if difference>=10:
                print("Too High")
            elif difference>=5:
                print("High")
            else:
                print("High but close")
        else:
            if difference<=-10:
                print("Too Low")
            elif difference<=-5:
                print("Low")
            else:
                print("Low but close")
            

mode()
