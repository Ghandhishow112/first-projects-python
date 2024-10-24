# Two players play the game against each other; let’s assume Player 1 and Player 2.

# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, The game continues till Player 2 eventually is able to guess the number entirely but will not be crowned mastermind.
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# If not, then Player 2 wins the game.


import math
Player_1=input("player one:  Enter your number :")
print(Player_1)
Player_2=input(" player two: Guess the number :")
print(Player_2)

if (Player_2==Player_1):
    print(" player two wins ")
else: 
    pass
count_player1=0   
while (Player_1 !=Player_2):
    Player_2=input(" player two :Guess the number :")
    count_player1+=1
    if count_player1==math.inf:
            break
print(f"player one guessed it right , the number is {Player_1} it took you {count_player1} times to get it")       

Player_2=input(" player two : Enter your number:")
print(Player_2)
Player_1=input(" player one : Guess the number :")
print(Player_1)

if (Player_2==Player_1):
    print("player two wins")
else: 
    pass
count_player2=0   
while (Player_2 !=Player_1):
    Player_1=input(" player one : Guess the number :")
    count_player2+=1
    if count_player1==math.inf:
            break
print(f"player two guessed it right , the number is {Player_2} it took you {count_player2} times to get it") 

if count_player1 < count_player2 :
    print()
    print("it took player one to guess the number with a lesser number of trials : player one wins and crowned mastermind")
elif count_player2 == count_player1 :
    print("its a tie")
else :
    print("it took player two to guess the number with a lesser number of trials : player two wins and crowned mastermind")