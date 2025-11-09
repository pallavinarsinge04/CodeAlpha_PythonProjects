import random

def hangman():
    words = ["python", "programming", "developer", "code", "alpha"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎯 Welcome to Hangman!")
    print("Word: " + " ".join(guessed))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct! " + " ".join(guessed))
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

        if "_" not in guessed:
            print("🎉 You won! The word was:", word)
            break
    else:
        print("💀 You lost! The word was:", word)

hangman()
