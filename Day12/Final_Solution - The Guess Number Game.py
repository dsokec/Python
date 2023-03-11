from random import randint
#from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess actual answer
def checkAnswer(guess, answer, turns):
    """ Check answer againts a guessed number. Returns a number of turns remaining. """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

# Make function to set difficulty
def setDifficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100.
    #print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1,100)
    #print(f"Pssst, the correct answer is {answer}")

    # Repeat the guessing functionality if they get it wrong.
    turns = setDifficulty()
    
    guess = 0
    while guess != answer:
        # Let the user guess a number.
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = checkAnswer(guess, answer, turns)
    # Track the number of turns and reduce by 1 if they get it wrong.
        if turns == 0:
            print("You've run out of guesses. You lose.\n")
            return
        elif guess != answer:
            print("Guess again.")

game()


