# Jake Gapusan
# CIS 256 Fall 2024
# EX 4

# import random to generate random numbers
import random

# create and define a list of words for the game
words = ["gaming", "coding", "testing", "homework", "habits"]

# create and define a method
def choose_word():
    return random.choice(words)

# define a method that displays the word
def show_word(word, guesses):
    return " ".join([letter if letter in guesses else "_" for letter in word])

def start_game():
    word = choose_word()
    guessed_letters = set()
    attempts = len(word) + 3 # this allows extra attempts

    print("Hello! Welcome to Word Guessing Game!")

    while attempts > 0:
        print(f"\nWord: {show_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word} correctly!")
                return
            
        else:
            attempts -= 1
            print(f"Incorrect guess. Attempts remaining: {attempts}")

    print(f"Sorry, you've run out of attempts. The word was: {word}")

# run the game with start_game() 
if __name__ == "__main__":
    start_game()