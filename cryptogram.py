import re
from legend import Legend
from wordlist import Wordlist

class Cryptogram:

    def __init__(self):
        #self.clue = [input(str("Enter a cryptogram. ")).lower()]
        #self.clue = ['"JB WOO EPH DBBJ TBK GWY, VT WOO EPH SHWYX WNWFOWVOH, FY WOO EPH CWTX TBK GWY, FY WOO EPH ROWGHX TBK GWY." SFW ZWIIBC'.lower()]
        self.clue = ['"U PS HE HBV DJUSV XEIVG UX FNVDUZUD ABPH HEGFHEM UF HE HBV JCFFUPX XEIVG PXT ABPH RVVHBEIVX UF HE SCFUD." OPSVF VGGJEM'.lower()]
        #self.initial_letter = input(str("What letter are you replacing? ").lower())
        #self.initial_letter = 'N'
        self.initial_letter = 'Z'
        #self.replacement_letter = input(str(f"What will you be replacing {self.initial_letter} with? ").lower())
        #self.replacement_letter = 'v'
        self.replacement_letter = 'F'
        self.list_words = self.sentence_to_list(self.clue)


    #convert input anagram to list
    def sentence_to_list(self,sentence):
        split_sentence = [i for item in sentence for i in item.split()]
        clue = []
        for word in split_sentence:
            wrd = ''
            for letter in word:
                if letter.isalpha():
                    wrd += letter
            if wrd:
                clue.append(wrd)
        return clue

    #convert a list to a sentence string
    def list_to_sentence(self,lst):
        snt = ' '.join([str(elem) for elem in lst])
        return (snt)

    def get_unique_letters(self,cryptogram):
        #Return a of unique letters in reverse order of frequency, for maximum efficiency
        str = self.list_to_sentence(cryptogram)
        letters = []
        for letter in str:
            if letter.isalpha():
                letters.append(letter)

        letters_by_count = {}
        for letter in letters:
            letters_by_count[letter] = letters.count(letter)
        sorted_letters = sorted(letters_by_count.items(), key=lambda x:x[1], reverse=True)


        letters_in_order = []
        for letter in sorted_letters:
            letters_in_order.append(letter[0])

        return letters_in_order
