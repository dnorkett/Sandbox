import string
import copy

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        text (string): the message's text
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        '''
        Returns: copy of self.valid_words
        '''
        valid_words_copy = copy.copy(self.valid_words)
        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to another letter (string).
        '''
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shifted_lower = lower_letters[shift:] + lower_letters[:shift]
        shifted_upper = upper_letters[shift:] + upper_letters[:shift]
        shift_dict = {}
        for i in range(26):
            lower_char = lower_letters[i]
            upper_char = upper_letters[i]
            shift_dict[lower_char] = shifted_lower[i]
            shift_dict[upper_char] = shifted_upper[i]
        return shift_dict

    def apply_shift(self, shift):
        '''
        Returns: the message text (string) in which every character is shifted down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        shifted_message_text = ''
        for char in self.message_text:
            shifted_message_text += shift_dict[char]

        return shifted_message_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        text (string): the message's text
        shift (integer): the shift associated with this message
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


    def get_shift(self):
        '''
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        shift (integer): the new shift that should be associated with this message.
        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #print(self.message_text, self.valid_words)
        split_str=self.message_text.split()
        decrypt_key = 0
        decrypt_key_counter = 0

        for i in range(26):
            temp_key_counter = 0
            for word in split_str:
                new_word = (self.apply_shift(26-i))
                if is_word(self.get_valid_words(), new_word):
                    temp_key_counter += 1
            if temp_key_counter > decrypt_key_counter:
                decrypt_key = 26-i
                decrypt_key_counter = temp_key_counter

        return(decrypt_key, self.apply_shift(decrypt_key))



if __name__ == '__main__':
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
