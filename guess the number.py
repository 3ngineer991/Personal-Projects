import time
import random

restart = True
guess = None
won = False

# loops every time that the player restarts without the same number
while restart:
    sameNum = True
    num = random.randint (1, 10)

# loops every time that the player chooses to play with the same number after a loss
    while sameNum:
        print("You have 5 attempts")
        for i in range(5):

            while not won:
                guess = input("Guess the number(1-10)")

                try:
                    if num == int(guess):
                        print("You won!\n")
                        time.sleep(1)
                        won = True
                    elif num >= int(guess) >= 1:
                        print ("too low\n")
                    elif num <= int(guess) <= 10:
                        print ("too high\n")
                    else:
                        print(guess + " is not 1-10\n")
                    break
                except:
                    print(guess + " is not a number silly\n")
            
        if int(guess) != num:
            print("you lost")

        time.sleep(2)
        ans = input ("Would you like to play agian?(y/n)")

        if ans == "n":
            print ("Goodbye!")
            restart = False
            break
        elif ans == "y":

            if guess != num:
                ans2 = input("Would you like to play with the same number?(y/n)")

                if ans2 == "n":
                    sameNum = False
                elif ans2 == "y":
                    sameNum = True
                else:
                    print("Error did not expect '" + ans2 + "'\n exiting program")
                    time.sleep(1)
                    restart = False
                    sameNum = False
            else:
                sameNum = False
        else:
            print("Error did not expect '" + ans + "'\n exiting program")
            time.sleep(1)
            restart = False
            sameNum = False

time.sleep (5)
