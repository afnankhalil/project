import random
possible_actions=["rock","paper","scissors"]
user_input=input("please enter your rock,paper or scissor:")
computer_action=random.choice(possible_actions)

if computer_action==user_input:
    print("computer action is:" + computer_action)
    print("the game is a draw")
elif computer_action=="rock" and user_input=="paper" or computer_action=="scissor" and user_input=="rock" or computer_action=="paper" and user_input=="scissor":
    print("computer action is:" + computer_action)
    print("you have won the game")
elif computer_action=="rock" and user_input=="scissor" or computer_action=="paper" and user_input=="rock" or computer_action=="scissor" and user_input=="paper":
    print("computer action is:" + computer_action)
    print("you have lost the game")