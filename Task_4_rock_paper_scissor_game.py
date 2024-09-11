from tkinter import *
import random

# Function to identify the winner
def identify_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!!"
    else:
        return "Computer wins!!"

# Function to update the game
def update_game(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = identify_winner(user_choice, computer_choice)
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    
    if result == "You win!!":
        user_score += 1
    elif result == "Computer wins!!":
        computer_score += 1
        
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text=" ")
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")


root = Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize variable to hold the values(score)
user_score = 0
computer_score = 0

#buttons
rock_button = Button(root, text="Rock", width=10, command=lambda: update_game('rock'))
paper_button = Button(root, text="Paper", width=10, command=lambda: update_game('paper'))
scissors_button = Button(root, text="Scissors", width=10, command=lambda: update_game('scissors'))

rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

#to show the result
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

#to show the score
score_label = Label(root, text=f"Score - You: {user_score}, Computer: {computer_score}", font=("Helvetica", 12))
score_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Reset button
reset_button = Button(root, text="Reset", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
