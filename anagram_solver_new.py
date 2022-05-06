import re

class AnagramSolver:

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
        # take input and convert into a list
        self.clue = [input(str("Enter an anagram. ")).lower()]
        self.initial_letter = input(str("What letter are you replacing? ").lower())
        self.replacement_letter = input(str(f"What will you be replacing {self.initial_letter} with? "))
        self.update_legend(self.initial_letter, self.replacement_letter)
        print(f'OK, {self.initial_letter} is now {self.legend[self.initial_letter.lower()]}.')
        self.clue = self.sentence_to_list(self.clue)
        self.output = []
        #print(f'Here is the solution: {self.solve_anagram(self.clue)}')

    #convert input anagram to list
    def sentence_to_list(self,sentence):
        return ([i for item in sentence for i in item.split()])

    def list_to_sentence(self,lst):
        snt = ' '.join([str(elem) for elem in lst])
        return (snt)

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

    def update_legend(self,oldletter,newletter):
        #Update legend with known letter
        old_letter = oldletter.lower()
        new_letter = newletter.lower()
        if self.legend[old_letter] != '':
            print(f'"{old_letter}" already guessed as {legend[oldletter]}')
        else:
            self.legend[old_letter] = new_letter

    def display_anagram_progress(self):
        #display anagram in progress
        input = self.sentence_to_list(self.clue)
        output = []
        for word in input:
            wrd = self.encode_word(word)
            output.append(wrd)
        return ' '.join(output)

    def list_possible_words(self,inputword):
        #take input word and return a list of possible matches. Input word should be encoded first.
        #Unknown letters should be uppercase
        possible_length_words = []
        # Return words of length to match length of input word
        with open('words.txt', 'r') as f:
            words = [line.strip() for line in f]
            for word in words:
                if len(inputword) == len(word):
                    possible_length_words.append(word.lower())

        #Convert input word to regex
        input_word = ''
        #input_word += '\"'
        for letter in inputword:
            if letter == '_':
                input_word += '.'
            else:
                input_word += letter.lower()
        #input_word += '\"'
        print(f"Input word: {input_word}")

        possible_words = ''
        possible_words += '\"'
        for word in possible_length_words:
                #remove words that have spaces in them
                possible_words += f"{word}"
        possible_words += '\"'

        #print(f"Possible words: {possible_words}")

        wordlist = re.findall(f"{input_word}", possible_words)

        return wordlist

    def word_certainty_score(self,word):
        #return a score based on number of possible words. Higher is better.
        score = 1/len(self.list_possible_words(word))*100
        return score

    def decode_anagram(self,anagram):
        #Display updated anagram with letters replaced with legend letters
        decoded_anagram = []
        for word in anagram:
            replacement_word = ''
            for letter in word:
                if letter.isalpha():
                    if self.legend[letter.lower()] != '':
                        replacement_word += self.legend[letter.lower()].upper()
                    else:
                        replacement_word += letter.lower()
            decoded_anagram.append(replacement_word)
        return decoded_anagram

    def get_unique_letters(self,anagram):
        #Return a of unique letters in reverse order of frequency, for maximum efficiency
        str = self.list_to_sentence(anagram)
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


    def decode_word(self,word):
        #replaces letters in the word that have been updated in the legend. E.g. Cuba becomes CubG if "a" is replaced by "g"
        decoded_word = ''
        for letter in word:
            if letter.isalpha():
                if self.legend[letter.lower()] != '':
                    decoded_word += self.legend[letter.lower()].upper()
                else:
                    decoded_word += letter.lower()
        return decoded_word

    def test_letters(self):
        matching_words_counts = [] #A list containing number of matches for each word once tested against the legend
        for word in self.sentence_to_list(self.clue):
            number_of_matches = self.list_possible_words(self.encode_word(word))
            print(f"number_of_matches: {len(number_of_matches)}")
            matching_words_counts.append(number_of_matches)
        return matching_words_counts

    def reset_legend(self):
        for letter in self.legend:
            self.legend[letter] = ''
        self.update_legend(self.initial_letter, self.replacement_letter)

    def solve_anagram(self):
        #These are the letters that need to be solved, in order of frequency with which they appear
        letters_in_clue = self.get_unique_letters(self.clue)
        letters_by_frequency = ['e','t','a','i','n','o','s','h','r',
                                'd','l','u','c','m','f','w','y','g',
                                'b','v','k','q','j','x','z']
        #Create the dictionary to guess the letters
        guesses = {}

        #populate the guessed_letters dictionary with each letter and an empty list to track guesses
        for letter in letters_in_clue:
            guesses[letter] = []
            guesses[self.initial_letter] = self.replacement_letter

        #populate guessed_letters dictionary with letters and empty lists to store previous guesses
        i = 0
        while i < len(letters_in_clue):
            guesses[self.initial_letter] = self.replacement_letter
            print(guesses)
            if letters_by_frequency[i] not in guesses[letters_in_clue[i]]:
                guesses[letters_in_clue[i]] = letters_by_frequency[i]
                print(guesses)
                self.legend[letters_in_clue[i]] = letters_by_frequency[i]
                print(self.test_letters())
                j = 0
                while j < len(self.clue):
                    if len(self.test_letters()[j]) == 0:
                        self.reset_legend()
                    j += 1
            i += 1




    #    for letter in letters_in_clue:
             #use letters that appear most frequently to maximize efficiency in creating combinations
    #        letters_by_frequency = ['e','t','a','i','n','o','s','h','r',
    #         'd','l','u','c','m','f','w','y','g','b','v','k','q','j','x','z']
    #        if letter == self.initial_letter:
                #Add letter to list of guesses
    #            guesses[letter].append(self.replacement_letter)
                #update legend with known replacement letter. This won't change
    #            self.legend[self.initial_letter] = self.replacement_letter
    #        else:
    #            print(f"letter 171: {letter}")
                #try each letter combination until there is exactly one word possible
    #            for ltr in letters_by_frequency:
    #                print(f"ltr 174: {ltr}")
    #                if ltr not in guesses[letter]:
    #                    print(f"ltr {ltr} not in guesses")
    #                    self.legend[letter] = ltr
    #                    print(f"self.legend[letter] is {self.legend[letter]}")
    #                    for word in self.sentence_to_list(self.clue):
    #                        print(f"word 180: {word}")
    #                        encoded_word = self.encode_word(word)
    #                        print(f"encoded_word 182: {encoded_word}")
    #                        if len(self.list_possible_words(encoded_word)) == 0:
    #                            guesses[letter].append(ltr)
        return guesses


angslv = AnagramSolver()
#print(angslv.clue)
#print(angslv.decode_word('Cuba'))
#print(angslv.encode_word('Cuba'))
#print(anagram_solver.display_anagram_progress())
print(angslv.list_possible_words('_V_______'))
print(len(angslv.list_possible_words('_V_______')))
#print(angslv.list_possible_words('C__A'))
#print(angslv.word_certainty_score('CuBA'))
print(angslv.legend)
#print(angslv.solve_anagram())
#print(angslv.decode_anagram(angslv.clue))
print(angslv.get_unique_letters(angslv.clue))
print(len(angslv.test_letters()))
#angslv.update_legend('s','h')
#print(len(angslv.test_letters()))
#angslv.update_legend('q','d')
#print(len(angslv.test_letters()))


            #    for word in self.sentence_to_list(self.clue):
            #        clue_word_decoded = self.decode_word(word)
                    #print(clue_word_decoded)
            #        for ltr in clue_word_decoded:
            #            if ltr.islower():
#
#                    for ltr in letters_by_frequency:
#                        #Check and see if a letter has already been guessed for this letter:
#                        if ltr not in set(guesses[letter]):
#                            #update the legend
#                            self.legend[letter] = ltr
#                            #Test the dictionary update against the words in the cluster
#                            for clue_word in self.sentence_to_list(self.clue):
#                                #Decode word if possible
#                                #figure out how many possible words it could be. If 0, move on
#                                if len(self.list_possible_words(clue_word_decoded)) == 0:
#                                    guesses[letter].append(ltr)
    #    return guesses




    #put all the letteres in place in the dictionary
    #for each of the words in the clue, see how many possible words there are with the those replacements.
    #If the number of possible words is zero, it's the wrong combination.
    #IN that case, throw each letter away by putting it into the quessed letters list.
    #When each word has exactly one word on its list of possible words, the anagram is solved.


                #populate the guessed_letters dictionary with each letter and an empty list to track guesses
                #guesses[letter] = []
                #replace a letter in the dictionary
                #for ltr in letters_by_frequency:
                #     guesses[letter].append(ltr)
                #update all words with the new letter
                #Find numbe of possible words for each word
                #if there are no possible words for a word, that means the combindation is wrong.
                #Keep track of letters guessed for each letter with a list as a dictionary value for each letter

        #words = []
        #ALL THE possible words for a given word with a pattern
        #clue = self.sentence_to_list(self.clue)
        #for word in clue:
        #    if self.initial_letter in word:
        #        words.append(self.encode_word(word))

        #print(words)


        #return self.legend



        #Decode anagram for initial clue
        #ang = self.decode_anagram(anagram)
        #solution = []
            #solution.append(self.list_possible_words(word))
        #return solution

        #Find the first word with the initial letter solved in that word.
        #generate a list of possible words for that word.
        #Loop through the list of possible words.
        #test the first possible word by replacing letters one by one in that word.
        #For each letter that is replaced in that word, replace other letters in other words.
        #once all letters are replaced in the first word, move to another word that has some letters solved
        #replace the letters in that word with known letters from the legend.
        #If no possible words come up once those letters have been replaced, start over by removing all guesses except the first guess.
        #The class dictionary self.legend is the source of truth. As new letters are confirmed, those letters are added to the legend.
        #TODO: How do confirm that a letter is correct?
        #If there is a word with at least one letter known, test out all possible matches for that word.
        #once letters have been replaced in that word, test the next word with any known letters.






#Albert Einstein
#bmcfsu fjotufjo
