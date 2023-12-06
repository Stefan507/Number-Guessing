import random

def main():
    """
    The `main` function is the entry point of the program. 
    It prompts the user to guess a number between 1 and 10 for a total of 5 games. 
    It calls the `generate_number` function to generate a random number for each game and passes it to the `play_game` function. 
    The `play_game` function allows the user to make up to 4 guesses and keeps track of the number of correct guesses. 
    Finally, the `main` function prints the total number of correct guesses made by the user.
    
    Inputs: None
    Outputs: The total number of correct guesses made by the user.
    """
    print("Welcome the number guessing, can you guess the number between 1 and 10?")
    score = 0
    for games in range(5):
        print(f"This is game {games + 1}")
        random_number = generate_number()
        score += play_game(random_number)
    print(f"You guessed {score} numbers correct!")

def play_game(random_number):
    """
    Play a number guessing game.

    Args:
    random_number (int): The randomly generated number that the user needs to guess.

    Returns:
    int: The number of correct guesses made by the user.
    """
    score = 0
    for round in range(4):
        while True:
            answer = input("Guess: ")
            if answer.isdigit() and 1 <= int(answer) <= 10:
                break
            else:
                print("Invalid input. Please enter an integer between 1 and 10.")
        if int(answer) == random_number:
            score += 1
            print("Correct!")
            break
        elif int(answer) < random_number:
            print("Larger")
        elif int(answer) > random_number:
            print("Smaller")
    else:
        print(f"Incorrect, the number was {random_number}")
    return score

def generate_number():
    """
    Generates a random number between 1 and 10.

    Returns:
        int: A random number between 1 and 10.
    """
    random_number = random.randint(1, 10)
    return random_number

if __name__ == "__main__":
    main()