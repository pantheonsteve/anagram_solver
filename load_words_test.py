with open('words.txt', 'r') as f:
    myNames = [line.strip() for line in f]
    print(len(myNames))
    print(myNames[10000])

def words_by_length(length):
    words_by_length = []
    with open('words.txt', 'r') as f:
        words = [line.strip() for line in f]
        for word in words:
            if len(word) == length:
                words_by_length.append(word)
    return words_by_length

wbl = words_by_length(18)
print(len(wbl))
print(wbl[3])
