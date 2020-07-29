def hangman():

    import random
    import re

#open the wordlist
    file = 'word_list.txt'
    with open(file,'r')as words:
        word_list = words.read().splitlines()

#set number of lives to 7
    lives = 7

#choose a random word for the game
    random_num = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_num]

#hide the chosen_word
    secret_word = re.sub('[0-9a-zA-Z]','*',chosen_word)

    
###define process to handle player guesses
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
    print("The word to guess is:", secret_word)
    print("Lets play!")
    
# set a while loop to run for 7 lives
    while(lives > 0):
# get the guessed letter from player, assign that letter to variable 'guessed'
        guessed = input("Please enter your next guess: ")[:1]       
# assign a correct guess and the secret_word to the pre-defined 'guess' function
        letter_found, secret_word = guess(guessed, chosen_word, secret_word)

# check if the guessed letter exists in the hidden word
        if not letter_found:
# letter not matched, remove one life from 'lives'        
            lives -= 1
# check if there are no more lives left - if none, end game. 
            if lives == 0:
                print("I'm sorry, you have no lives left. The word was:", chosen_word)
                print("You lose.")
 
                break
# check lives left, if yes tell player wrong guess and show lives left, move to next guess, show word left to guess.                
            else:
                print("Ooops, that letter isn't in the word, you have",lives,"lives remaining. The word to guess is: ", secret_word)
                
# if the guessed letter isn't in the word
# first check if the word still has characters to guess
        else:
            if "*" not in secret_word:
# no letters left to guess - player wins
                print("Well done, the word was:", chosen_word)
                print("Congratulations you win!")

                break
# correct guess, more letters left to guess. Show lives left, show word left to guess.     
            else:
                print("Well done! That letter was found. You still have", lives, "remaining. The word to guess is: ", secret_word)                
# begin the game
hangman()
