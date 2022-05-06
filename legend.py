class Legend:

    def __init__(self):
        #Letter dictionary
        self.key = {
        'a':'','b':'','c':'','d':'',
        'e':'','f':'','g':'','h':'',
        'i':'','j':'','k':'','l':'',
        'm':'','n':'','o':'','p':'',
        'q':'','r':'','s':'','t':'',
        'u':'','v':'','w':'','x':'',
        'y':'','z':''
        }

    def update(self,oldletter,newletter):
        #Update legend with known letter
        old_letter = oldletter.lower()
        new_letter = newletter.lower()
        self.key[old_letter] = new_letter

    def encode(self,word):
        translated_word = ''
        for letter in word:
            if self.key[letter] == '':
                translated_word += '_'
            else:
                translated_word += self.key[letter]
        return translated_word

    def replace_word(self,oldword,newword):
        old_word = []
        new_word = []
        if len(oldword) != len(newword):
            print('ERROR: Words must be the same length')
        else:
            for ol in oldword:
                old_word.append(ol)
            for nl in newword:
                new_word.append(nl)
        i = 0
        for i in range(len(old_word)):
            self.update(old_word[i], new_word[i])
            i += 1

    def show_progress(self, wordlist):
        #Replace each letter in a wordlist with its translated letter from the legend, or an underscore.
        #Good function for preparing the cryptogram for testing each word
        crypto_words = []
        for word in wordlist:
            wrd = ''
            for letter in word:
                if self.key[letter] == '':
                    wrd += '_'
                else:
                    wrd += self.key[letter]
            crypto_words.append(wrd)
        return crypto_words

    def test_letter(self,oldletter,newletter):
        self.update(oldletter,newletter)
        clue = self.sentence_to_list(self.clue)
        number_of_matches = []
        for word in clue:
            encoded_word = self.encode_word(word)
            #number_of_matches.append(self.number_of_matches(encoded_word))
            number_of_matches.append({f"{word}: {encoded_word} | {self.number_of_matches(encoded_word)}"})
        return number_of_matches



#legend = Legend()
#print(legend.encode('yes'))
#print(legend.key['y'])
#print(legend.key['e'])
#print(legend.key['s'])
#legend.replace_word('yes','old')
#print(legend.key['y'])
#print(legend.key['e'])
#print(legend.key['s'])
#progress = legend.show_progress(['yes','we','are','very','great'])
#print(progress)
