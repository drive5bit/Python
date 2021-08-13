import time
import random
import os
# Replit Username: xXEradicationXx
# Github Username: drive5bit
# Discord Username: BurningAsh#3369
print("""
Replit Username: xXEradicationXx
Github Username: drive5bit
""")
# discord = os.environ['discord']
# discp = input("Enter password for discord username: ")
# if discp == os.environ['pwd']:
#     print(discord)
# else:
#     print("Let's just move on.")
def Guess():
    try:
        name = input("What's your name?: ")
        print(f"Hi {name}! Welcome to my game. You'll have to self learn this game and it's really easy! After 3 or 4 runs, you'll be great. Good luck!")
        a = int(input('Enter the number limit. Syntax(0 - '))
        while a < 0:
          print("That number is under zero, and that's not allowed. Please try again!")
          a = int(input('Enter the number limit. Syntax(0 - '))
        while a > 100000000000000:
          b = input("That number is so high that this game will take forever. Are you Sure? Y/N: ").lower()
          c = ['y', 'n']
          while b not in c:
            print("Our program does not recognize the value you entered. Try again.")
            b = input("That number is so high that this game will take forever. Are you sure? Y/N: ").lower()
          if b  == 'y':
              print('Okay. The value was intercepted as response 200.')
              break
          if b == 'n':
               quit(f"Our systems got impatient. They killed the program. Please use the game the right way, thanks. Run the program again to play {name}.")
        secret = int(input(f"What is the secret number now? It has to be between 0 and {a}: "))
        while secret < 0 or secret > a:
          if secret < 0:
            print("That number is under zero, and that's not allowed. Please try again!")
          if secret > a:
            print('That number is over the limits. Please try again!')
            secret = int(input(f"What is the secret number now? It has to be between 0 and {a}: "))
        print("The computer has started guessing.")
        startTime = time.time()
        computer = random.randint(0, a)
        while computer != secret:
          computer = random.randint(0, a)
        endTime = time.time()
        print(f"The computer successfully guessed your number. It guessed {str(computer)} and your number was {str(secret)}. The time taken for the computer to get this result was {endTime - startTime} seconds!")
        again = input("Do you want to play the game again? Y/N: ").lower()
        while again not in ['y', 'n']:
          print("Our programs aren't responding to the value you gave. Plase try again.")
          again = input("Do you want to play the game again? Y/N: ").lower()
        if again == 'y':
          print('Okay!')
          Guess()
        elif again == 'n':
          quit("Quiting the program. Thank you for playing!")
    except Exception:
        print("An unexpected error occured while the program was running. We are running the function again. All data was lost.")
        Guess()
Guess()
