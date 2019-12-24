import string
import copy

class PhraseTrigger(object):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        text = text.lower()

        for char in text:
            if char in string.punctuation:
                text = text.replace(char, ' ')

        split_text = text.split()

        clean_text = ' '.join(split_text)

        if clean_text in self.phrase:
            return True
        else:
            return False

samplePhraseTrigger = PhraseTrigger('PurPle cow')

print(samplePhraseTrigger.is_phrase_in('purple$#@cow'))