import random
import hangman_art as art
import hangman_words as wd
word_list = wd.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stages = art.stages

end_of_game = False
lives = 6
logo = art.logo
print(logo)
display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
        continue
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            guessed_letters.append(guess)
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
