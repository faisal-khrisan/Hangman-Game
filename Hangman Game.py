import random
from hangman_words import word_list
from hangman_art import  logo, stages
print(logo)
chosen_word=random.choice(word_list)
placeholder=""
for n in chosen_word:
    placeholder+="_"

print(f"Word to guess : {placeholder}")
lives=6
game_over=False
correct_letter=[]
while game_over==False:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess=str(input("Guess a letter :"))

    display = ""
    if guess in correct_letter:
        print(f"You have already guessed this letter {guess}")

    for letter in chosen_word:
        if letter== guess:
            display+=letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display+=letter
        else :
            display+="_"
    print(f"Word to guess :{display}")
    if display == chosen_word :
        game_over =True
    if guess not in chosen_word :
        print(f"You guessed {guess} which is wrong, you are losing your life ")
        lives-=1
        if lives==0:
            print(f"You lost,  The correct word that you were trying to guess is {chosen_word}")
            game_over=True

    print(stages[lives])
