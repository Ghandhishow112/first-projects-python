while True :
    
        name=input("what is your name :")
        print(f"welcome to the tournament mr {name}")
        import random
        def get_choice():
           options=["rock", "paper", "scissors"]
    
           while True:
                computer_choice= random.choice(options)
                player_choice=input(f"enter a valid choice ,{options} :")
                if (player_choice== "rock"):
                 break
                elif(player_choice=="paper"):   
                 break  
                elif(player_choice=="scissors"):   
                 break
               
               
           if (player_choice=="rock" and computer_choice=="scissors"):
                 print("you win")
           elif (player_choice=="paper" and computer_choice=="paper"):
                 print("it\'s a tie")
           elif(player_choice=="scissors" and computer_choice=="paper"):
                 print("you win")
    
           if (player_choice=="scissors" and computer_choice=="rock"):
                 print("computer win")
           elif (player_choice=="paper" and computer_choice=="scissors"):
                 print("computer win")
           elif(player_choice=="rock" and computer_choice=="paper"):
                  print("computer win")
        
           if (player_choice=="scissors" and computer_choice=="scissors"):
                  print("it\'s a tie")
           elif (player_choice=="rock" and computer_choice=="rock"):
                 print("it\'s a tie")
           elif(player_choice=="paper" and computer_choice=="rock"):
                 print("you win")  
    
           choices={"player choice": player_choice, "computer choice": computer_choice}
    
           return choices   
        choices=  get_choice()
        print(choices)
        option_2=["yes", "no"]
 
        restart= input(f"will you like to restart the game ,{option_2}  ")
        if (restart=="yes"):
         breakpoint
         
    
        elif(restart=="no"):
         print("thank you for playing")
         break  
  
