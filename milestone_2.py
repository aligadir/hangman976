import random  # Import the random module to randomly select a word

word_list = ['apple', 'banana', 'cherry', 'mango', 'pear']

print("List of words:", word_list)


word = random.choice(word_list)


print("Randomly selected word:", word)

guess = input("Enter a single letter: ").lower()  # Convert input to lowercase


if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input. Please enter a single letter.")
