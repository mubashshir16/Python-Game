
#Rock, Paper, Scissors Game
# --------------------------
#How to Play:
#The player chooses Rock, Paper, or Scissors.
#The computer randomly picks Rock, Paper, or Scissors.

#Rules:
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock
# The game declares the winner of each round.
# The game continues until the player chooses to exit.
# Keeps track of wins, losses, and ties.

import random

def get_computer_choice():
    """Randomly returns Rock, Paper, or Scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """Determines the winner of a round."""
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_round():
    """Plays a single round of Rock, Paper, Scissors."""
    while True:
        player_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
        if player_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid input. Please try again.")

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice.capitalize()}")

    winner = determine_winner(player_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return winner

def main():
    """Main game loop."""
    wins, losses, ties = 0, 0, 0

    print("===== Welcome to Rock, Paper, Scissors =====")

    while True:
        print("\nMenu:")
        print("1. Play a round")
        print("2. View score")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            result = play_round()
            if result == "player":
                wins += 1
            elif result == "computer":
                losses += 1
            else:
                ties += 1
        elif choice == "2":
            print(f"\nScoreboard:")
            print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the game
if __name__ == "__main__":
    main()
