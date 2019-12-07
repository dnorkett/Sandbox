import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string that represents which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string comprised of letters that have not yet been guessed.
    '''
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''
    secret_word = secret_word
    letters_guessed = []
    remaining_guesses = 10

    print('Welcome to Hangman!')
    print('I am thinking of a word that is', str(len(secret_word)), 'letters long')

    while remaining_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print('-' * 50)
        print('You have', remaining_guesses, 'remaining guesses')
        print('Available letters:', str(get_available_letters(letters_guessed)))
        guess = str.lower(input('Guess a letter: '))
        if guess in letters_guessed:
            print('You have already guessed that letter, try again:', get_guessed_word(secret_word, letters_guessed))
        elif not str.isalpha(guess):
            print('Invalid guess, please try again:', get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed += guess
            print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed += guess
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            remaining_guesses -= 1

    if remaining_guesses > 0:
        score = remaining_guesses * len(set(secret_word))
        print('-' * 50)
        print("Congratulations! You Won!")
        print('Your total score for this round:', str(score))
    else:
        print('-' * 50)
        print("Sorry, you've run out of guesses!")
        print("The secret word was:", secret_word)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    pass


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)