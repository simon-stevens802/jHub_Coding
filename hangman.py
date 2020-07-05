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
    secret_word = re.sub('[0-9a-zA-Z]','-',chosen_word)


###define process to andle player guesses
# define 'guess' as the function, with 'letter', 'word' and 'encoded' as strings
    def guess(letter, word, encoded):

# first, set the 'found' variable to false
        found = False
# now check if the guessed string 'letter' is in the string 'word'
        if letter in word:
# letter found, so set 'found' variable to 'true'
            found = True
# letter was found, replace the dashes with the guessed letter
# for each character in the chosen_word, check all characters of the word and compare them to guessed letter
            for char in range(0, len(word)):
# if the guess matches characters in the chosen_word
                if word[char] == letter:
# take the secret_word, and replace each hidden character with the match, then check the next character in word
                    encoded = encoded[0:char] + letter + encoded[char+1:len(encoded)]
#
        return (found, encoded)
###end of defining the function

#start the game
    print("Time to play, you have", lives, "lives.")
    print("Your word is:", secret_word)
    print("Lets play!")
    
    #set while loop for number of lives
    while(lives > 0):
        guessed = input("What's your guess: ")[:1]       
        letter_found, secret_word = guess(guessed, chosen_word, secret_word)

    #check if the guessed letter exists in the hidden word
        if not letter_found:
            lives -= 1
            if lives == 0:
                print("Oh no! You've used up your lives. The word was:",chosen_word,". Better luck next time!")
                break
            else:
                print("Ooops, that letter isn't in the word, you have",lives,"lives remaining.")
                print(secret_word)

    #if the guessed letter isn't in the word
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
