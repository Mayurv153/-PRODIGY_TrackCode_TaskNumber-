import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
