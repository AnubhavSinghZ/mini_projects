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
guess=""

# Number of turns
Turns= 12
