import random

def main():
    # Open the file and read its content
    with open("words.txt", "r") as file:
        content = file.read()

    # Split the content into words and store in a list
    words_list = content.split()

    # Choose a word randomly from the list
    word = random.choice(words_list)
    word_as_list = list(word)  # Convert the word to a list of characters
    word_guess = ["-" for _ in word_as_list]  # Create a list of dashes to represent the word
    attempts_left = 9  # Set the total attempt limit
    guessed_letters = set()  # Set to store all guessed letters
    correct_letters = set()  # Set to store correctly guessed letters

    print(f"-- Console Hangman by Daniel --")

    # Load ASCII sprites for the attempts
    with open("hangman_ascii.txt", "r") as file_ascii:
        ascii_content = file_ascii.readlines()

    # Split into chunks of 11 lines
    hangman_stages = [ascii_content[i:i +10] for i in range(0, len(ascii_content), 10)]
    hangman_stages = ["".join(stage) for stage in hangman_stages]

    while attempts_left > 0:
        print("\nCurrent word:", "".join(word_guess))
        print(f"Attempts remaining: {attempts_left}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        # Get user input
        choice = input("Enter a letter (or type 'exit' to quit): ")

        # Check for the escape condition
        if choice.lower() == "exit":
            print("Exiting the game.")
            break

        # Check if the input is a single alphabetic character
        if choice.isalpha() and len(choice) == 1:
            choice = choice.lower()

            # Check if the letter has already been guessed
            if choice in guessed_letters:
                if choice in correct_letters:
                    print("You've already correctly guessed that letter. Try a different one.")
                    print("\n---------------------------------------")
                else:
                    print("You've already guessed that letter and it was incorrect.")
                    print("\n---------------------------------------")
                continue

            # Add the guessed letter to the set of guessed letters
            guessed_letters.add(choice)

            # Check if the guessed letter is in the word
            if choice in word_as_list:
                # Add to correct letters set
                correct_letters.add(choice)

                # Update word_guess with the correct letter at all matching positions
                for i, letter in enumerate(word_as_list):
                    if letter == choice:
                        word_guess[i] = choice
                print("Correct guess!")
                print("\n---------------------------------------")

                # Check if the word is fully guessed
                if "-" not in word_guess:
                    print(f"Congratulations! You've guessed the word: {word}\n")
                    break
            else:
                # Penalize by reducing attempts for an incorrect guess
                attempts_left -= 1

                # Display the appropriate hangman stage based on the remaining attempts
                print(hangman_stages[8 - attempts_left])
                print("Incorrect guess. Try again.")
                print("\n---------------------------------------")

                # Check if attempts are exhausted
                if attempts_left == -1:
                    print(f"Game over! You've run out of attempts. The word was: {word}")
                    break
        else:
            print("Input is not a valid letter. Please enter a single alphabetic character.")

if __name__ == "__main__":
    main()