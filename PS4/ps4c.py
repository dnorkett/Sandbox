import string
import copy
from GeneratePermutations import get_permutations

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    '''
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist

def is_word(word_list, word):
    '''
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')
    
    def get_message_text(self):
        '''
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy = self.valid_words.copy()
        return valid_words_copy
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        Returns: a dictionary mapping a letter (string) to another letter (string).
        '''

        punctuation = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        dict = {}
        for i, char in enumerate(vowels_permutation.lower()):
            dict[VOWELS_LOWER[i]] = char
        for i, char in enumerate(vowels_permutation.upper()):
            dict[VOWELS_UPPER[i]] = char
        for char in CONSONANTS_LOWER:
            dict[char] = char
        for char in CONSONANTS_UPPER:
            dict[char] = char
        for punc in punctuation:
            dict[punc] = punc
        return dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        enc_message = []
        for char in self.message_text:
            enc_message.append(transpose_dict[char])
        return ''.join(enc_message)

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Returns: the best decrypted message
        '''
        tranpose_dict_list = []
        de_message_list = []
        perm_list = get_permutations('aeiou')
        for perm in perm_list:
            tranpose_dict_list.append(self.build_transpose_dict(perm))
        for dic in tranpose_dict_list:
            de_message = self.apply_transpose(dic)
            de_message_list.append(de_message)
        test = []
        big_test = []
        word_list = self.get_valid_words()
        for mes in de_message_list:
            de_words = mes.split()
            for word in de_words:
                if is_word(word_list, word):
                    test.append(1)
                else:
                    test.append(0)
            big_test.append((sum(test), mes))
            del test[0:len(test)]
        best_choice = max(big_test)
        possible_de_message = []
        for tup in big_test:
            if tup[0] == best_choice[0] and tup[1] not in possible_de_message:
                possible_de_message.append(tup[1])
        de_string = ''
        for mes in possible_de_message:
            de_string = de_string + ', ' + mes
        return de_string[1:]
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     

