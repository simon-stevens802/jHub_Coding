def hangman():

    import random
    import re

    #open the wordlist

    with open('words.txt','r')as words:
        word_list = words.read().splitlines()

    #set number of lives
    lives = 10

    #choose a random word for the game
    random_num = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_num]


    #hide the chosen_word
    secret_word = re.sub('[0-9a-zA-Z]','#',chosen_word)


    #define process to andle player guesses
    def guess(letter, word, encoded):
        # Does the letter exist within the word?
        found = False
        if letter in word:
            found = True
            # Replace the dashes with the letter
            for i in range(0, len(word)):
                if word[i] == letter:
                    encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
        return (found, encoded)

    #start the game
    print("Time to play, you have", lives, "lives left...")
    print("Your word is... :", secret_word)

    #set while loop for number of lives
    while(lives > 0):
        guessed = input("Your guess: ")[:1]
            
        letter_found, secret_word = guess(guessed, chosen_word, secret_word)

        if not letter_found:
            lives -= 1
            if lives == 0:
                print("Oh no! You've used up your lives. The word was:",chosen_word,". Better luck next time!")
                break
            else:
                print("Ooops, that letter isn't in the word, you have",lives,"lives remaining.")
                print(secret_word)
        else:
            if "#" not in secret_word:
                print("Congratulations! You won with", lives,"remaining. The word was", chosen_word,".")
                break
            else:
                print("well done! That letter was found. You still have", lives, "remaining.")
                print(secret_word)
                
    #want to play again? reset the game
    restart = input("Want to play again? (y = yes, n = no) ")
    if restart == "y":
        hangman()
    else:
        print("Ok, thanks for playing")
        print("        \|/        ") 
        print("_____mm_0,0_mm_____")
#start the game
hangman()
