
class AnagramSolver:

    def __init__(self,encodeletter,decodeletter):
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
        self.output = []

        self.quotelist = self.sentence_to_list(self.quote)

    def unique_letters(self):
        #Creates list of unique letters in a clue
        letters = []
        for word in self.clue:
            for letter in word:
                if letter.isalpha():
                    letters.append(letter)
        return list(set(letters))

    def convert_letter(self,word,letter,replacement):
        #Takes word, existing letter in the word, and replacement letter. Returns word with replacement letters
        letters = []
        for ltr in word:
            if ltr == letter:
                letters.append(replacement)
            else:
                letters.append(ltr)
        return ''.join(map(str, letters))

    def replace_letter(self,original_letter,replacement_letter):
        anagram = self.clue
        self.legend[original_letter] = replacement_letter
        output = []
        for word in anagram:
            updatedword = ''
            for letter in word:
                if letter == original_letter:
                    updatedword += self.legend[replacement_letter]
                else:
                    updatedword += letter
            output.append(updatedword)
        self.output = output


    def convert_word(self,original_word,guess_word):
        #break original and guess words into letters
        original_letters = list(original_word)
        guess_letters = list(guess_word)

        #iterator
        i = 0

        if len(original_letters) != len(guess_letters):
            print('Error: Guess word needs to be same length as original word')
        else:
            while i < len(original_letters):
                original_letters[i] = guess_letters[i]
                i += 1
        return guess_letters

    #convert input anagram to list
    def sentence_to_list(self,lst):
        return ([i for item in lst for i in item.split()])

    def encode(self, actual_word, scrambled_word):
        #break words into a list of letters
        scrambled_letters = list(scrambled_word)
        actual_letters = list(actual_word)

        i = 0

        while i < len(scrambled_letters):
            self.legend[scrambled_letters[i]] = actual_letters[i]
            i += 1

    def decode(self, scrambled_word):
        #break words into a list of letters
        scrambled_letters = list(scrambled_word)
        decoded_word = ''

        for letter in scrambled_letters:
            decoded_word += self.legend[letter]

        return decoded_word


anagram_solver = AnagramSolver('e','q')

print(anagram_solver.quotelist)
print(anagram_solver.convert_letter('Hello','l','z'))
print(anagram_solver.convert_word('Bitto','Hello'))
print(anagram_solver.output)
anagram_solver.encode('hello','svddi')
print(anagram_solver.legend)
print(anagram_solver.decode('svddi'))
print(anagram_solver.unique_letters())
