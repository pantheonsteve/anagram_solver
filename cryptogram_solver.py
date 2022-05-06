import re

class CryptoSolver:

    def __init__(self):
        #Letter dictionary
        self.legend = {
        'a':'','b':'','c':'','d':'',
        'e':'','f':'','g':'','h':'',
        'i':'','j':'','k':'','l':'',
        'm':'','n':'','o':'','p':'',
        'q':'','r':'','s':'','t':'',
        'u':'','v':'','w':'','x':'',
        'y':'','z':''
        }
        #List of letters that have not been guessed
        self.remaining_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        #self.remaining_letters = []
        # take input and convert into a list
        #self.clue = [input(str("Enter an anagram. ")).lower()]
        self.clue = ['"JB WOO EPH DBBJ TBK GWY, VT WOO EPH SHWYX WNWFOWVOH, FY WOO EPH CWTX TBK GWY, FY WOO EPH ROWGHX TBK GWY." SFW ZWIIBC'.lower()]
        #self.initial_letter = input(str("What letter are you replacing? ").lower())
        self.initial_letter = 'N'
        #self.replacement_letter = input(str(f"What will you be replacing {self.initial_letter} with? ").lower())
        self.replacement_letter = 'v'
        self.update_legend(self.initial_letter, self.replacement_letter)
        #self.update_legend('w','a')
        #self.update_legend('f','i')
        #self.update_legend('o','l')
        #self.update_legend('v','b')
        #self.update_legend('h','e')
        #self.update_legend('t','y')
        #self.update_legend('j','d')
        #self.update_legend('b','o')
        #self.update_legend('e','t')
        #self.update_legend('p','h')
        #self.update_legend('k','u')
        #self.update_legend('c','d')
        #self.update_legend('x','s')
        #self.update_legend('y','n')
        #self.update_legend('r','p')
        #self.update_legend('g','c')
        #self.update_legend('s','m')
        #self.update_legend('d','g')
        print(f'OK, {self.initial_letter} is now {self.legend[self.initial_letter.lower()]}.')
        #self.clue = self.sentence_to_list(self.crypto)
        self.output = []

    #---Utility Functions---
    #convert input anagram to list
    def sentence_to_list(self,sentence):
        split_sentence = [i for item in sentence for i in item.split()]
        clue = []
        for word in split_sentence:
            wrd = ''
            for letter in word:
                if letter.isalpha():
                    wrd += letter
            clue.append(wrd)
        return clue

    def show_remaining_letters(self):
        guessed_letters = []
        for key in self.legend:
            if self.legend[key] != '':
                guessed_letters.append(self.legend[key])
        remaining_letters = [l for l in self.remaining_letters if l not in guessed_letters]
        return remaining_letters

    #---Word Functions---
    def encode_word(self,word):
        #Replaces unknown letters with a _ and known letters with that letter. E.g. Cuba becomse ___g if "a" is replaced by "g"
        output = ''
        word = word.lower()
        #Takes word, loops through each letter
        for letter in word:
        #If letter has replacement in the legend, replace that letter with the replacement letter
            if letter.isalpha():
                if self.legend[letter] != '':
                        output += self.legend[letter]
                else:
                    output += ('_')
        #Return word shape with underscores for mystery letters, letter for replacement letter
        return output

    def test_word_with_letter(self,letter):
        #Find the first word with letter in it, test that word
        clue_words = []
        for word in self.sentence_to_list(self.clue):
            clue_words.append(self.encode_word(word))
        possible_words = []
        for word in clue_words:
            if letter in word:
                possible_words.append(word)
        return possible_words

    #---Cryptographic Functions
    def update_legend(self,oldletter,newletter):
        #Update legend with known letter
        old_letter = oldletter.lower()
        new_letter = newletter.lower()
        if self.legend[old_letter] == '':
            self.legend[old_letter] = new_letter


    def list_possible_words(self,inputword):
        #take input word and return a list of possible matches. Input word should be encoded first.
        #Unknown letters should be uppercase
        possible_length_words = []
        # Return words of length to match length of input word
        with open('words.txt', 'r') as f:
            words = [line.strip() for line in f]
            for word in words:
                if len(inputword) == len(word):
                    if '\"' not in word:
                        possible_length_words.append(word)

        #Convert input word to regex
        input_word = ''
        #input_word += '\"'
        for letter in inputword:
            if letter == '_':
                input_word += '.'
            else:
                input_word += letter.lower()
        #input_word += '\"'

        possible_words = ''
        possible_words += '\"'
        for word in possible_length_words:
            #remove words that have spaces in them
            possible_words += f"{word}"
            possible_words += '\"'

        wordlist = re.findall(f"{input_word}", possible_words)

        return wordlist

    def number_of_matches(self, inputword):
        number_of_matches = len(self.list_possible_words(inputword))
        return number_of_matches

    def test_letter(self,oldletter,newletter):
        self.update_legend(oldletter,newletter)
        clue = self.sentence_to_list(self.clue)
        number_of_matches = []
        for word in clue:
            encoded_word = self.encode_word(word)
            #number_of_matches.append(self.number_of_matches(encoded_word))
            number_of_matches.append({f"{word}: {encoded_word} | {self.number_of_matches(encoded_word)}"})
        return number_of_matches

    def test_word_replacement(self,oldword,newword):
        #Take a word, replace any letters in the Legend that have not already been replaced
        for index in range(len(oldword)):
            self.update_legend(oldword[index],newword[index])
        number_of_matches = []
        for word in self.clue:
            if word != oldword:
                number_of_matches.append(self.list_possible_words(word))
        return number_of_matches

    def certainty_score(self):
        clue = self.clue
        total_words = len(clue)
        total_possibilities = 0
        for word in clue:
            encoded_word = self.encode_word(word)
            total_possibilities += self.number_of_matches(encoded_word)
        certainty_score = total_possibilities/total_words
        return certainty_score


    def solve(self):
        #Start with the word that has the known letter replacement:
        first_word = self.test_word_with_letter(self.replacement_letter)
        print(f"first word: {first_word}")
        #Next, generate a list of possible words for the first word
        initial_word_list = self.list_possible_words(first_word)
        print(f"List of possible words: {initial_word_list}")

        #solution = ''
        #for word in self.clue:
        #    for letter in word:
        #        if letter.isalpha():
        #            solution += self.legend[letter.lower()]
        #        else:
        #            solution += letter
        #    solution += ' '
        #return solution


cs = CryptoSolver()
print(cs.clue)

print(f"Test Letter: {cs.test_letter(cs.initial_letter,cs.replacement_letter)}")
print(f"List possible words: {cs.test_word_with_letter('v')}")
print(f"Remaining letters to guess: {cs.show_remaining_letters()}")
print(cs.solve())
print(f"certainty score: {cs.certainty_score()}")

#Sample crypto: "JB WOO EPH DBBJ TBK GWY, VT WOO EPH SHWYX WNWFOWVOH, FY WOO EPH CWTX TBK GWY, FY WOO EPH ROWGHX TBK GWY." SFW ZWIIBC
# N = V
