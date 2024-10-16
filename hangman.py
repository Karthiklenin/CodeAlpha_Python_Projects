import random

def get_word():
    words = ["codealpha", "amazon", "python", "hangman", "discipline"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |
           |
        """,
        """
           ------
           |    
           |    
           |    
           |
           |
        """,
        """
           
        """,
    ]
    return stages[tries]

def play():
    word = get_word()
    guessed = []
    tries = 6
    win = False

    print("Let's begin the game Hangman!")
    
    while tries > 0 and not win:
        print(display_hangman(tries))
        print("Word: ", " ".join([letter if letter in guessed else "_" for letter in word]))
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("Hey buddy! You already guessed that letter.")
        elif guess not in word:
            print("Sorry buddy! Wrong guess.")
            tries = tries - 1
            guessed.append(guess)
        else:
            print("Hurray! Good guess!")
            guessed.append(guess)

        if all(letter in guessed for letter in word):
            win = True

    if win:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you lost! The word was: {word}")

if __name__ == "__main__":
    play()
