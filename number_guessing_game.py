import random
print("Welcome to the Number Guessing Game!!")
print("I will pick a number between 1 and 50. You have 5 chances to guess it.")
guess_count=0
number=random.randint(1,50)
while guess_count<5:
    guess= input("What is your guess?")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess=int(guess)
    guess_count+=1
    if guess < number:
        print(f"Try a higher number. Remaining guesses: {5-guess_count}")
    elif guess > number:
        print(f"Try a lower number. Remaining guesses: {5-guess_count}")
    else:
        print(f"CONGRATULATIONS!! You won! It took you {guess_count} guesses. The number was {number}.")
        break
else:
    print(f"You lost! You've used all your guesses. The number was {number}.")