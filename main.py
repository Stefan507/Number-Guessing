
import random

def main():
    games = 0
    round = 0
    while games < 5:    
        random_number = generate_random_number()
        while round < 4:
            answer = input("Guess: ")
            points = validate_answer(answer, random_number, round)
            round += 1
        games += 1
    print(float(points))


def generate_random_number():
    """
    Generates a random number between 1 and 100.

    Returns:
        int: A random number between 1 and 100.
    """
    random_number = random.randint(1, 10)
    return random_number

def validate_answer(answer, random_number, round):
    points = 0
    if round == 0:
        if int(answer) == random_number:
            points += 3
        elif int(answer) > random_number:
            print("Smaller")
        elif int(answer) < random_number:
            print("Larger")
    elif round == 1:
        if int(answer) == random_number:
            points += 2
        elif int(answer) > random_number:
            print("Smaller")
        elif int(answer) < random_number:
            print("Larger")
    elif round == 2:
        if int(answer) == random_number:
            points += 1
        elif int(answer) > random_number:
            print("Smaller")
        elif int(answer) < random_number:
            print("Larger")
    elif round == 3:
        if int(answer) == random_number:
            points += 0.5
        elif int(answer) > random_number or int(answer) < random_number:
            print(f"The answer was: {random_number}")
        
    return float(points)



if __name__ == "__main__":
    main()
     