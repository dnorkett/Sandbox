import math
import random
import string
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

WORDLIST_FILENAME = "words2.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word.
    The first component is the sum of the points for letters in the word.
    The second component is the larger of 1 or (7 * wordlength - 3 *(n-wordlength)
    word: string
    n: int >= 0
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if 7 * len(word) - 3 * (n - len(word)) > 1:
        score *= 7 * len(word) - 3 * (n - len(word))
    else:
        score *= 1
    return score


def display_hand(hand):
    """
    Displays the letters currently in the hand.
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        if i == 0:
            hand['*'] = 1
        else:
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand

def update_hand(hand, word):
    """
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    new_hand = copy.deepcopy(hand)
    for letter in word.lower():
        if new_hand.get(letter,0) > 0:
            new_hand[letter] = new_hand.get(letter,0) - 1
    return new_hand


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    possible_words = []

    for vowel in VOWELS:
        possible_words.append(word.replace('*', vowel))

    for letter in word:
        if word.count(letter) > hand.get(letter, 0):
            return False

    if word not in word_list:
        if '*' in word:
            for item in possible_words:
                if item in word_list:
                    return True
        return False

    return True


def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen=0
    for key in hand:
        handlen += hand[key]
    return handlen


def play_hand(hand, word_list):
    """
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: the total score for the hand
    """
    total_score = 0

    while calculate_handlen(hand) > 0:
        user_input = input('Enter word, or "!!" to indicate that you are finished:')

        if user_input == '!!':
            break
        else:
            if is_valid_word(user_input, hand, word_list):
                word_score = get_word_score(user_input, calculate_handlen(hand))
                print(user_input, 'earned', word_score, 'points. Total points:', total_score)
                total_score += word_score
            else:
                print('This is not a valid word. Please enter another word.')

            hand = update_hand(hand, user_input)

    if user_input != '!!':
        print('You ran out of letters.')

    print('Round: ', total_score, 'points.')
    return total_score


def substitute_hand(hand, letter):
    """
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter not in hand.keys():
        return hand

    else:
        all_letters = VOWELS + CONSONANTS
        sub_letters = all_letters.replace(letter, '')
        for key in hand.keys():
            if key == letter:
                sub_letters = sub_letters.replace(key,'')

        new_hand = copy.deepcopy(hand)

        for key in hand.keys():
            if key == letter:
                for i in range(hand[key]):
                    x = random.choice(sub_letters)
                    new_hand[x] = hand.get(x, 0) + 1
                new_hand.pop(letter)
        return new_hand


def play_game(word_list):
    """
    * Returns the total score for the series of hands
    word_list: list of lowercase strings
    """
    series_score = 0
    has_used_sub = False
    number_of_hands = int(input("Enter total number of hands:"))

    for i in range(number_of_hands):
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        if not has_used_sub:
            if input("Would you like to substitute a letter? ") == 'yes':
                has_used_sub = True
                sub_letter = str(input("Which letter would you like to replace: "))
                hand = substitute_hand(hand, sub_letter)
        series_score += play_hand(hand, word_list)
    return series_score


if __name__ == '__main__':
    word_list = load_words()
    series_score = play_game(word_list)
    print("Total Score: ", series_score)