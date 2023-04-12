from getpass import getpass as input
print("Welcome to Rock, Paper, Scissors")
winner1=0
winner2=0
while True:
  # welcome the user
  
  print()
  print("Pick R, P, S")
  print()
  
  print(winner1)
  print(winner2)
  
  # assign player 1 and 2
  player_1=input("player1, pick: ")
  player_2=input("player2, pick: ")
  # conditions to find the answer
  if player_1=="R" and player_2=="R":
    print("Rock and Rock, It's a draw")
  elif player_1=="R" and player_2=="P":
    winner2+=1
    print("Paper covers Rock, player2 wins!")
  elif player_1=="R" and player_2=="S":
    winner1+=1
    print("Rock smashes Scissors, player1 wins!")
  elif player_1=="P" and player_2=="P":
    print("Paper and Paper, it's a draw!")
  elif player_2=="P" and player_2=="R":
    winner2+=1
    print("Paper covers Rock, player2 wins!")
  elif player_1=="P" and player_2=="S":
    winner2+=1
    print("Scissors cuts Paper, player2 wins!")
  elif player_1=="S" and player_2=="S":
    print("Scissors and Scissors, it's a draw")
  elif player_1=="S" and player_2=="R":
    winner2+=1
    print("Rock smashes Scissors, player2 wins!")
  elif player_1=="S" and player_2=="P":
    winner1+=1
    print("Scissors cuts Paper, player1 wins")
  if winner1==3 or winner2==3:
    print(f"Player1 has {winner1} points")
    print(f"player2 has {winner2} points")
    exit()
