import random
# Get User's Name
name =  input("What is your name?")
print("Good Luck !", name)
# list of words for the game
words=["Python", "java", "Javascript", "C++", "Computer", "Programming", "Algorithms", "Mathematics", "Conditions", "Loops", "Rainbow"]
# Random choose a word from the list by using random.choice() method
word=random.choice(words) #Randomly choose a word from the list
print("\n Guess the character in the word")

#  Store guessed characters
guesses=""

# Number of turns
Turns= 12

while Turns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed+=1
    print()

    if failed==0:
        print("You Win")
        print("The word is:", word)
        break
    guess=input("Guess a character:").lower()

    if len(guess)!=1:
        print("Please enter a single character:")
        continue

    if guess in guesses:
        print("You have already guessed it.")
        continue

    guesses+=guess

    if guess not in word:
        Turns-=1
        print("wrong")
        print("You have", Turns,"more guesse")

        if Turns==0:
            print("You Lose.")
            print("The last word was:", word)
