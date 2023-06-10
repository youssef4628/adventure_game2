import random
from time import sleep
import sys

# replay the game
def replay_game():
    while True:
        answer=input(write_text("Do you want repaly the game again ? (yes/no)")).lower()
        if answer == "yes":
            game()
        else:
            sys.exit()
    

def write_text(text):
    for char in text:
        print(char, end="", flush=True)
        sleep(0.008)


def choose_right_left():
    while True:
        choice = input("Which door do you choose? (left/right)").lower()
        if choice == "left":
            return choice
            break
        else:
            return choice
            break


def choose_play_again():
    return input("Do you want to play again? (yes/no) ").lower()


def game():
    print("Welcome to the giza maze!")
    # Initialize any necessary variables
    play_again = "yes"
    num_wins = 0
    num_losses = 0
    while play_again == "yes":
        # Game loop
        write_text("""You find yourself in a dark room.
You see two doors, one on the left and one on the right.\n""")
        choice = choose_right_left()
        # Randomly determine the outcome of the choice
        outcome = random.choice(["win", "lose"])
        if choice == "left":
            if outcome == "win":
                write_text("""You open the door on the left and find a treasure chest!
Inside the chest, you find a bag of gold and a note that reads:
You're rich! Spend this money on something silly, like a giant rubber duck!
Congratulations, you win!""")
                num_wins += 1
            elif outcome == "lose":
                write_text("""You open the door on the left and find a room full of Angry chickens!
The chickens peck at you relentlessly, and you are unable to escape
Sorry, you lose!\n""")
                num_losses += 1
        else:
            if outcome == "win":
                write_text("""You open the door on the right and find a magic portal!
You step through the portal and find yourself in a strange laboratory.
A mad scientist appears and invites you to be his assistant.
As you work with the scientist,
you discover his secretformula for a potion that makes people dance uncontrollably.
'You're a dancing scientist! Use this knowledge to create the ultimate dance party!'
Congratulations, you win! \n""")
                num_wins += 1
            elif outcome == "lose":
                write_text("""You open the door on the right and find a room full of clowns!
The clowns are friendly at first, but then they start to get creepy.
They start to chase you around the room with pies and squirt flowers.
Sorry, you lose!\n""")
                num_losses += 1

        # Check if the player has won or lost enough to end the game
        print(f"Now you won {num_wins} times and lost {num_losses}")
        if num_wins >= 3:
            write_text("""You've won three times! You win the game.
But wait, there's a plot twist!
You suddenly wake up from a dream and realize that you've been playing a video game all along.\n""")
            break
        elif num_losses >= 3:
            write_text("""You've lost three times!You lose the game.
But wait, there's a plot twist!
You suddenly wake up from a dream and realize that you've been playing a video game all along.\n""")
            break
        # Ask the player if they want to play again
        play_again = choose_play_again()
    print("Thanks for playing!")
    replay_game()



if __name__ == '__main__':
    game()
