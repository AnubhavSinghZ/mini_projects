

def start_game():

 print("__WELCOME TO NUMBER GUESS GAME__")

#Player 1 sets target
target=float(input("Player1, enter a number that should be the secret(0-100):"))

#Hide the number from Player2 by printing empty lines
print("\n *50")

print("Player2, start guessing!")
attempts=0
is_coreect=False

guess=float(input("Enter your Guess:"))
attempts+=1
if guess==target:
 print("Correct! You found it in {attempts}attempts.")
 is_correct=True
elif guess>target:
 print("Try a lower number:")
else:
 print("Try a higher number")      

start_game()