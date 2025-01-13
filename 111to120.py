print(" 111.	Simple Password Generator\n 112.	Contact Book\n 113.	Quiz Game\n 114.	Hangman Game\n 115.	Tic-Tac-Toe\n 116.	Text-based Adventure\n 117.	Rock-Paper-Scissors\n 118.	Email Slicer\n 119.	Dictionary App\n 120.	Basic To-Do List Manager\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 111:
# Generate a random password of a specified length with letters, digits, and special characters.
 import random
 import string

 def generate_password(length):
    # Define the characters that can be used in the password
     all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the list to form the password
     password = ''.join(random.choice(all_characters) for _ in range(length))
    
     return password

# Get password length from the user
 try:
     length = int(input("Enter the desired password length: "))
     if length < 8:
         print("It's recommended to have a password length of at least 8 characters.")
     password = generate_password(length)
     print(f"Generated password: {password}")
 except ValueError:
     print("Please enter a valid integer for the password length.")

elif question==112:
# Write a program to store contact details (name, number, email) in a file and allow adding/searching.
 import os

# Function to add a contact
 def add_contact():
     name = input("Enter name: ")
     number = input("Enter phone number: ")
     email = input("Enter email: ")

    # Save contact to file
     with open("contacts.txt", "a") as file:
         file.write(f"{name},{number},{email}\n")
     print("Contact added successfully.")

# Function to search for a contact
 def search_contact():
     search_name = input("Enter the name to search: ")

     found = False
     with open("contacts.txt", "r") as file:
         for line in file:
             name, number, email = line.strip().split(",")
             if search_name.lower() in name.lower():
                 print(f"Name: {name}, Phone: {number}, Email: {email}")
                 found = True
                 break

     if not found:
         print("Contact not found.")

# Function to display the menu
 def display_menu():
     print("\nContact Book Menu")
     print("1. Add Contact")
     print("2. Search Contact")
     print("3. Exit")

# Main program
 def main():
     while True:
         display_menu()
         choice = input("Enter your choice: ")

         if choice == "1":
            add_contact()
         elif choice == "2":
            search_contact()
         elif choice == "3":
            print("Exiting...")
            break
         else:
             print("Invalid choice. Please try again.")

# Check if contacts.txt exists, create it if not
 if not os.path.exists("contacts.txt"):
     with open("contacts.txt", "w") as file:
         pass  # Just create an empty file if it doesn't exist

# Start the program
 if __name__ == "__main__":
     main()

elif question==113:
# Build a simple quiz game that asks multiple-choice questions and tracks the score.
# List of questions, choices, and the correct answer
 quiz_questions = [
     {
         "question": "What is the capital of France?",
         "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
         "answer": "C"
     },
     {
         "question": "Which programming language is known as the 'language of the web'?",
         "choices": ["A) Python", "B) JavaScript", "C) Java", "D) C++"],
         "answer": "B"
     },
     {
         "question": "What is the largest planet in our solar system?",
         "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
         "answer": "C"
     },
     {
         "question": "Which element has the chemical symbol 'O'?",
           "choices": ["A) Oxygen", "B) Gold", "C) Osmium", "D) Ozone"],
         "answer": "A"
     }
 ]

# Function to display the question and get user's answer
 def ask_question(question, choices, correct_answer):
     print(question)
     for choice in choices:
         print(choice)

     answer = input("Enter your answer (A/B/C/D): ").upper()
    
     if answer == correct_answer:
         print("Correct!\n")
         return 1  # 1 point for correct answer
     else:
         print(f"Wrong! The correct answer is {correct_answer}.\n")
         return 0  # 0 points for incorrect answer

# Function to run the quiz
 def run_quiz():
     score = 0
     print("Welcome to the Quiz Game!\n")
    
     for question_data in quiz_questions:
         question = question_data["question"]
         choices = question_data["choices"]
         correct_answer = question_data["answer"]
        
         score += ask_question(question, choices, correct_answer)

     print(f"Your final score is {score} out of {len(quiz_questions)}.")

# Start the quiz game
 if __name__ == "__main__":
     run_quiz()

elif question==114:
# Implement the “Hangman” word-guessing game using loops and conditionals.
 import random

# List of words for the game
 word_list = ["python", "hangman", "programming", "developer", "computer", "algorithm"]

# Function to display the current state of the word
 def display_word(word, guessed_letters):
     display = ""
     for letter in word:
         if letter in guessed_letters:
            display += letter + " "
         else:
             display += "_ "
     return display.strip()

# Function to play the Hangman game
 def play_hangman():
     word = random.choice(word_list)  # Randomly choose a word
     guessed_letters = []  # List to track guessed letters
     attempts = 6  # Number of allowed incorrect guesses
     correct_guesses = 0  # Number of correct guesses

     print("Welcome to Hangman!")
    
    # Main game loop
     while attempts > 0 and correct_guesses < len(word):
         print("\nWord to guess: ", display_word(word, guessed_letters))
         print(f"Guesses remaining: {attempts}")
         print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get the player's guess
         guess = input("Enter a letter: ").lower()

        # Check for invalid input
         if len(guess) != 1 or not guess.isalpha():
             print("Please enter a valid single letter.")
             continue
        
        # Check if the letter has already been guessed
         if guess in guessed_letters:
             print("You already guessed that letter. Try again.")
             continue

        # Add the guessed letter to the list of guessed letters
         guessed_letters.append(guess)

        # Check if the guess is in the word
         if guess in word:
             print("Correct guess!")
             correct_guesses += word.count(guess)  # Count how many times the guessed letter appears in the word
         else:
             print("Incorrect guess!")
             attempts -= 1  # Decrease attempts for an incorrect guess

    # Check if the player won or lost
     if correct_guesses == len(word):
         print("\nCongratulations! You've guessed the word:", word)
     else:
           print("\nGame Over! The correct word was:", word)

# Start the game
 if __name__ == "__main__":
     play_hangman()

elif question==115:
# Implement the 2-player Tic-Tac-Toe game on the console.
# Function to print the Tic-Tac-Toe board
 def print_board(board):
     print("\n")
     print(f" {board[0]} | {board[1]} | {board[2]} ")
     print("---+---+---")
     print(f" {board[3]} | {board[4]} | {board[5]} ")
     print("---+---+---")
     print(f" {board[6]} | {board[7]} | {board[8]} ")
     print("\n")

# Function to check if a player has won
 def check_winner(board, player):
    # Winning combinations
     win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                         (0, 4, 8), (2, 4, 6)]            # diagonals

    # Check for winning combination
     for combination in win_combinations:
         if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
             return True
     return False

# Function to check if the board is full
 def is_board_full(board):
     return "_" not in board

# Main game loop
 def play_tic_tac_toe():
    # Initial empty board
     board = ["_" for _ in range(9)]

    # Player symbols
     player_turn = "X"  # Player 1 is X, Player 2 is O

     print("Welcome to Tic-Tac-Toe!")
     print_board(board)

     while True:
        # Ask the current player for a move
         print(f"Player {player_turn}'s turn.")
         move = int(input("Enter your move (1-9): ")) - 1  # Convert to 0-indexed

        # Check if the move is valid
         if move < 0 or move > 8 or board[move] != "_":
             print("Invalid move. Try again.")
             continue

        # Make the move
         board[move] = player_turn

        # Print the board
         print_board(board)

        # Check if the current player wins
         if check_winner(board, player_turn):
             print(f"Player {player_turn} wins!")
             break

        # Check if the board is full (draw)
         if is_board_full(board):
             print("It's a draw!")
             break

        # Switch players
         player_turn = "O" if player_turn == "X" else "X"

# Start the game
 if __name__ == "__main__":
     play_tic_tac_toe()

elif question==116:
# Create a small text-based adventure game with multiple rooms and user choices.
# Function to display the current room's description and prompt for choices
 def display_room(room):
     print("\n" + room['description'])
     for option, choice in room['choices'].items():
         print(f"{option}. {choice['action']}")

# Function to handle the player's movement through rooms
 def move_to_room(choice, rooms):
     if choice in rooms:
         return rooms[choice]
     else:
         print("Invalid choice. Please select a valid option.")
         return None

# Game function to start the adventure
 def start_adventure():
    # Define rooms with descriptions and choices
     rooms = {
         'start': {
             'description': "You are in a dark, mysterious cave. There are two exits: one to the north and one to the east.",
             'choices': {
                 '1': {'action': 'Go north', 'next_room': 'library'},
                 '2': {'action': 'Go east', 'next_room': 'treasure_room'}
             }
         },
         'library': {
             'description': "You enter a dusty old library filled with ancient books. There's a strange book glowing on a shelf.",
             'choices': {
                 '1': {'action': 'Read the glowing book', 'next_room': 'secret_passage'},
                 '2': {'action': 'Leave the library and go back', 'next_room': 'start'}
             }
         },
         'treasure_room': {
             'description': "You enter a room filled with gold and treasure. But suddenly, a trapdoor opens beneath you!",
             'choices': {
                 '1': {'action': 'Try to escape through the trapdoor', 'next_room': 'escape'},
                 '2': {'action': 'Sit and enjoy the treasure', 'next_room': 'treasure_end'}
             }
         },
         'secret_passage': {
             'description': "You find yourself in a hidden passage. It leads you to an eerie underground tunnel.",
             'choices': {
                 '1': {'action': 'Continue down the tunnel', 'next_room': 'final_room'},
                 '2': {'action': 'Go back to the library', 'next_room': 'library'}
             }
         },
         'escape': {
             'description': "You managed to escape the trapdoor and find yourself back at the start of the cave. The adventure continues!",
             'choices': {
                 '1': {'action': 'Go back to the library', 'next_room': 'library'},
                 '2': {'action': 'Return to the treasure room', 'next_room': 'treasure_room'}
             }
         },
         'treasure_end': {
             'description': "You stay in the treasure room, but eventually, the treasure fades away, and you are left alone in the dark.",
             'choices': {
                 '1': {'action': 'Go back to the library', 'next_room': 'library'},
                 '2': {'action': 'Try to leave the cave', 'next_room': 'start'}
             }
         },
         'final_room': {
             'description': "You reach the final room, a chamber with an ancient artifact glowing in the center. It’s the end of your journey.",
             'choices': {
                 '1': {'action': 'Take the artifact', 'next_room': 'win'},
                 '2': {'action': 'Leave the artifact and go back', 'next_room': 'secret_passage'}
             }
         },
        'win': {
             'description': "Congratulations! You’ve successfully completed the adventure and obtained the artifact!",
             'choices': {}
         }
     }

    # Start the adventure from the starting room
     current_room = rooms['start']

    # Game loop
     while True:
         display_room(current_room)
         if 'choices' in current_room and current_room['choices']:
             choice = input("\nWhat will you do? (Enter the number of your choice): ")
             if choice in current_room['choices']:
                 next_room_key = current_room['choices'][choice]['next_room']
                 current_room = rooms[next_room_key]
               else:
                 print("Invalid choice, try again!")
         else:
             break  # If no choices are left, the game ends

     print("\nGame Over. Thanks for playing!")

# Start the game
 if __name__ == "__main__":
     start_adventure()

elif question==117:
# Build a Rock-Paper-Scissors game where the user plays against the computer.
 import random

# Function to get the user's choice
 def get_user_choice():
     while True:
         user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
         if user_choice in ["rock", "paper", "scissors"]:
             return user_choice
         else:
             print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

# Function to get the computer's choice
 def get_computer_choice():
     return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
 def determine_winner(user_choice, computer_choice):
     if user_choice == computer_choice:
        return "It's a tie!"
     elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
         return "You win!"
     else:
         return "Computer wins!"

# Main game loop
 def play_game():
     print("Welcome to Rock-Paper-Scissors game!")
    
    # Loop for the game to continue
     while True:
         user_choice = get_user_choice()
         computer_choice = get_computer_choice()

         print(f"\nYou chose: {user_choice}")
         print(f"Computer chose: {computer_choice}")

         result = determine_winner(user_choice, computer_choice)
         print(result)
        
        # Ask if the user wants to play again
         play_again = input("\nDo you want to play again? (yes/no): ").lower()
         if play_again != "yes":
             print("Thanks for playing! Goodbye.")
             break

# Start the game
 if __name__ == "__main__":
     play_game()

elif question==118:
# Prompt the user for an email address, extract the username and domain, and display them.
# Function to extract username and domain from the email address
 def extract_email_parts(email):
    # Split the email into username and domain at the '@' symbol
     if '@' in email:
         username, domain = email.split('@', 1)
         return username, domain
     else:
         print("Invalid email format.")
         return None, None

# Main program
 def main():
    #    Prompt the user for an email address
     email = input("Enter your email address: ")

    # Extract username and domain
     username, domain = extract_email_parts(email)

    # Display the results
     if username and domain:
         print(f"Username: {username}")
         print(f"Domain: {domain}")

# Start the program
 if __name__ == "__main__":
     main()

elif question==119:
# Use dictionary file (or API) to create a simple command-line dictionary to look up words and their definitions.
# Define a simple dictionary within the program
 simple_dictionary = {
     "apple": "A round fruit with red or green skin and a whitish interior.",
     "banana": "A long curved fruit with a yellow skin and soft, sweet flesh.",
     "orange": "A round citrus fruit with orange skin and a tangy, juicy interior.",
     "python": "A high-level programming language known for its readability and simplicity.",
     "computer": "An electronic device for storing and processing data.",
     "keyboard": "A device used to input text into a computer."
 }

# Function to look up the word in the dictionary
 def lookup_word(word):
    return simple_dictionary.get(word.lower(), "Word not found in the dictionary.")

# Main program
 def main():
     print("Welcome to the command-line dictionary!")
     while True:
        # Prompt the user for a word to look up
         word = input("\nEnter a word to look up (or 'exit' to quit): ").strip()
        
         if word.lower() == "exit":
             print("Goodbye!")
             break
        
        # Look up the word and display the result
         definition = lookup_word(word)
         print(f"Definition of '{word}': {definition}")

# Start the program
 if __name__ == "__main__":
     main()

elif question==120:
# Allow users to add tasks, mark them as done, and view tasks. Store tasks in a file or in memory.
# Function to load tasks from a file
 def load_tasks(filename="tasks.txt"):
     try:
         with open(filename, "r") as file:
             tasks = file.readlines()
        # Strip newlines and return tasks
         return [task.strip() for task in tasks]
     except FileNotFoundError:
         return []

# Function to save tasks to a file
 def save_tasks(tasks, filename="tasks.txt"):
     with open(filename, "w") as file:
         for task in tasks:
             file.write(f"{task}\n")

# Function to add a task
 def add_task(task, tasks):
     tasks.append(f"[ ] {task}")  # Task is initially not done
     save_tasks(tasks)

# Function to mark a task as done
 def mark_task_done(task_index, tasks):
     if 0 <= task_index < len(tasks):
         tasks[task_index] = tasks[task_index].replace("[ ]", "[X]")  # Mark task as done
         save_tasks(tasks)
     else:
         print("Invalid task number.")

# Function to view tasks
 def view_tasks(tasks):
     if not tasks:
           print("No tasks available.")
     else:
         for index, task in enumerate(tasks, 1):
             print(f"{index}. {task}")

# Main program
 def main():
     tasks = load_tasks()  # Load existing tasks from the file
     print("Welcome to the Task Manager!")
    
     while True:
         print("\nOptions:")
         print("1. Add a new task")
         print("2. Mark a task as done")
         print("3. View tasks")
         print("4. Exit")
        
         choice = input("Enter your choice: ").strip()
        
         if choice == "1":
             task = input("Enter the task description: ").strip()
             add_task(task, tasks)
             print("Task added successfully.")
        
         elif choice == "2":
             view_tasks(tasks)
             try:
                 task_number = int(input("Enter the task number to mark as done: ").strip())
                 mark_task_done(task_number - 1, tasks)  # Subtract 1 for zero-based index
                 print("Task marked as done.")
             except ValueError:
                 print("Please enter a valid task number.")
        
         elif choice == "3":
             view_tasks(tasks)
        
         elif choice == "4":
             print("Goodbye!")
             break
        
         else:
             print("Invalid choice. Please try again.")

# Run the program
 if __name__ == "__main__":
     main()
