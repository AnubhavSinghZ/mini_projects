def start_game():
 print("WELCOME TO SNAKE AND LADDERS")
print("Rule: 1st player to reach 100 wins!")
p1_pos = 0
p2_pos = 0
game_over= False

# the game will be continued till one reach to 100
while p1_pos<100 and p2_pos<100:
 
 #player 1 turn
 print("\n Player 1 Turn")
 roll1=int(input("Enter dice roll(1-6):"))
 if p1_pos+roll1<=100:
  p1_pos+=roll1

  # Ladders
  if p1_pos==4: p1_pos=25; print("Ladder! upto 25")
 elif p1_pos==13: p1_pos=46; print("Ladder! upto 46")

   #Snake
 elif p1_pos==27: p1_pos=5; print("Snake! Down to 5")
 elif p1_pos==54: p1_pos=31; print("Snake! Down to 31")

print(f"Player 1 Position:{p1_pos}")
if p1_pos==100:
 print("Player 1 WIN")
 game_over= True

 

#player 2 turn
print("\n Player 2 Turn")
roll1=int(input("Enter dice roll(1-6):"))
if p2_pos+roll1<=100:
  p2_pos+=roll1

  # Ladders
  if p2_pos==4: p2_pos=25; print("Ladder! upto 25")
  elif p2_pos==13: p2_pos=46; print("Ladder! upto 46")

   #Snake
elif p2_pos==27: p2_pos=5; print("Snake! Down to 5")
elif p2_pos==54: p2_pos=31; print("Snake! Down to 31")

print(f"Player 2 Position:{p2_pos}")
if p2_pos==100:
 print("Player 2 WIN")
 game_over= True



start_game()