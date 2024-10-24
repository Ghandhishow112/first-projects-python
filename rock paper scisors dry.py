while True :
    
        name=input("what is your name :")
        print(f"welcome to the tournament mr {name}")
        import random
        def get_choice(computer_choice,player_choice ):
           while True:
                
                if (player_choice== "rock"):
                 break
                elif(player_choice=="paper"):   
                 break  
                elif(player_choice=="scissors"):   
                 break
               
               
           
           if (player_choice=="rock" and computer_choice=="scissors"):
                 print("you win")   
           elif(player_choice=="scissors" and computer_choice=="paper"):
                 print("you win")
           if (player_choice=="scissors" and computer_choice=="rock"):
                 print("computer win")
           elif (player_choice=="paper" and computer_choice=="scissors"):
                 print("computer win")
           elif(player_choice=="rock" and computer_choice=="paper"):
                  print("computer win")
           elif(player_choice=="paper" and computer_choice=="rock"):
                 print("you win")  
           elif(player_choice==computer_choice):
                 print('it\'s a tie')
           choices={"player choice": player_choice, "computer choice": computer_choice}
           
           return choices   
        options=["rock", "paper", "scissors"]
        choices=  get_choice(computer_choice=random.choice(options),player_choice= input(f"enter a valid choice ,{options} :"))
        print(choices)
        option_2=["yes", "no"]
 
        restart= input(f"will you like to restart the game ,{option_2}  ")
        if (restart=="yes"):
         breakpoint
         
    
        elif(restart=="no"):
         print("thank you for playing")
         break  
  