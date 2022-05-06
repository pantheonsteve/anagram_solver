import re

def list_possible_words(inputword):
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
    number_of_matches = len(wordlist)

    print(f"Input word: {input_word}")
    print(f"Possible matches: {len(wordlist)}")
    print(f"Number of Matches: {number_of_matches}")

list_possible_words('_v_______')
list_possible_words('m____')
list_possible_words('m__i_')
list_possible_words('m__ic')
list_possible_words('ma_ic')
