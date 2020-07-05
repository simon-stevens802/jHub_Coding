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
# now return the secret word containing the matched guesses
        return (found, encoded)
###end of defining the function

#start the game
    print("Time to play, you have", lives, "lives.")
    print("Your word is:", secret_word)
    print("Lets play!")
    
    #set a while loop to run for 10 lives
    while(lives > 0):
# get the guessed letter from player, assign that letter to variable 'guessed'
        guessed = input("What's your guess: ")[:1]       
# assign a correct guess and the secret_word to the pre-defined 'guess' function
    letter_found, secret_word = guess(guessed, chosen_word, secret_word)

# check if the guessed letter exists in the hidden word
        if not letter_found:
# letter not matched, remove one life from 'lives'        
            lives -= 1
# check if there are no more lives left - if none, end game. 
            if lives == 0:
                print("Oh no! You've used up your lives. The word was:",chosen_word,". Better luck next time!")
                break
# check lives left, if yes tell player wrong guess and show lives left, move to next guess, show word left to guess.                
            else:
                print("Ooops, that letter isn't in the word, you have",lives,"lives remaining.")
                print(secret_word)

# if the guessed letter isn't in the word
# first check if the word still has characters to guess
        else:
            if "#" not in secret_word:
# no letters left to guess - player wins                
                print("Congratulations! You won with", lives,"remaining. The word was", chosen_word,".")
                break
# correct guess, more letters left to guess. Show lives left, show word left to guess.     
            else:
                print("well done! That letter was found. You still have", lives, "remaining.")
                print(secret_word)
                
# see if the player wants to play again? reset the game
    restart = input("Want to play again? (y = yes, n = no) ")
# player wants to play again, they enter 'y' and press enter
    if restart == "y":
        hangman()
        
# player doesn't want to play again, game ends.
    else:
        print("Ok, thanks for playing")
        print("        \|/        ") 
        print("_____mm_0,0_mm_____")
        
# begin the game
hangman()
