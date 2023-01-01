import random
import time

words = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'watermelon']

word = random.choice(words)

word_list = list(word)

random.shuffle(word_list)

shuffled_word = ''.join(word_list)

print("Your word is:", shuffled_word)

time.sleep(1)

print("\033[H\033[J")

guess = input("Enter your guess: ")

if guess == word:
  print("Congratulations! You guessed correctly.")
else:
  print("Sorry, that's incorrect. The correct word was:", word)
