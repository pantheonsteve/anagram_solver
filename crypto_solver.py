import re
from legend import Legend
from wordlist import Wordlist
from cryptogram import Cryptogram
import time


class CryptoSolver:

    def __init__(self):
        self.legend = Legend()
        self.wordlist = Wordlist()
        self.crypto = Cryptogram()
        self.crypto_progress = []
        self.tested_wordlist = []

    def solve(self):
        crypto = self.crypto
        legend = self.legend
        wordlist = self.wordlist
        #list of words in the cryptogram
        crypto_words = crypto.sentence_to_list(crypto.clue)
        #list of unique letters in the cryptogram
        crypto_letters = crypto.get_unique_letters(crypto_words)
        #update the legend to reflect the initial letter substitution
        legend.update(crypto.initial_letter,crypto.replacement_letter)
        print(legend.key)
        #find the first word with the initial substitution
        first_word = wordlist.find_words_with_letter(crypto_words, crypto.initial_letter.lower())
        first_word_encoded = legend.encode(first_word[0])
        #print out a list of possible matches for the first word.
        possible_first_matches = wordlist.possible_matches(first_word_encoded)
        print(len(possible_first_matches))
        possible_matches = []
        start_time = time.time()
        for match in possible_first_matches: #for each word in the list of possible matches
            legend.replace_word(first_word[0],match) #replace the initial word with that word
            #Get a list of number of matches
            number_of_matches = []
            for word in legend.show_progress(crypto_words):
                number_of_matches.append(len(wordlist.possible_matches(word)))
                print(word)
            if 0 not in number_of_matches:
                possible_matches.append(match)
        print(first_word)
        print(possible_matches)
        print(f"process took {time.time() - start_time} to run.")







cs = CryptoSolver()
cs.solve()

#
#--- Legend functions:
#      legend.update(oldletter,newletter) - #Update legend letter with known letter
#      legend.encode(word) - #Returns a word consisting of _ for unknown letters, and the letter of known letters.
#           #Used to prepare non-translated crypto words for testing
#      legend.replace_word(oldword,newword) - updates dictionary letters from one word with letters of another word.
#           #words must be the same length
#      legend.show_progress(wordlist) - #Replace each letter in a wordlist with its translated letter from the legend, or an underscore.
#           #Good function for preparing the cryptogram for testing each word
#--- Wordlist functions:
#      wordlist.same_length_as(inputword) - #Returns a list of words of the same length as the input word (utility function)
#      wordlist.possible_matches(word) - #returns a list of possible matches for a word with blanks and known letters.
#           #Word Example: possible_matches('m__ic') = ['magic', 'manic', 'medic', 'mimic', 'mimic', 'music
#      wordlist.find_words_with_letter(wordlist,letter) - #Returns words in a wordlist containing a letter. Useful for identifying where to start solving (i.e. a word with the replacement letter)
#      wordlist.test_wordlist(wordlist) - #Returns number of possible matches for each word when a replacement is made.
#--- Cryptogram functions:
#      cryptogram.sentence_to_list(sentence) - #Breaks a sentence into a list
#      cryptogram.get_unique_letters(cryptogram) - #Return a of unique letters in reverse order of frequency, for maximum efficiency
#      cryptogram.list_to_sentence(list) - #utility function to convert a list to a sentence string
