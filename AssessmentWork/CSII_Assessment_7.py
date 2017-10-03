aliceBook = open("Alice's_Adventures_In_Wonderland.txt", "r")
aliceWrite = open("Written_Alice.txt", "w")

string = aliceBook.read()

words = string.split()

alice_words = {}

character = ["â", "€", "™", "œ", "˜"]


def sortedList(dict, writeTo, char):
    keylist = list(dict.keys())
    keylist.sort()
    start = keylist.index("Alice")
    allWords = str(keylist[start:])

    for word in allWords:
        if word in char:
            allWords = allWords.replace(char, "")

    writeTo.write("".join(allWords))

for word in words:
    alice_words[word] = words.count(word)

sortedList(alice_words, aliceWrite, character)
