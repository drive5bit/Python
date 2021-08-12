# Replit Username: xXEradicationXx
# Github Username: drive5bit

import time
import random

a = int(input('Enter the number limit. Syntax(0 - '))
while a < 0:
  print("That number is under zero, and that's not allowed. Please try again!")
  a = int(input('Enter the number limit. Syntax(0 - '))
while a > 100000000000000:
  b = input("That number is so high that this game will take forever. Are you sure? Y/N: ").lower()
  c = ['y', 'n']
  while b not in c:
    print("Our program does not recognize the value you entered. Try again.")
    b = input("That number is so high that this game will take forever. Are you sure? Y/N: ").lower()
    if b  == 'y':
      print('Okay. The value was intercepted as response 200.')
    if b == 'n':
      quit("We are killing the program. Run the program again to play. Don't forget to put your value beneath 100000000000000!")
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
print(f"The computer successfully guessed your number. It guessed {str(computer)} and your number was {str(secret)}. The time taken for the computer to get this result was {endTime - startTime}!")
