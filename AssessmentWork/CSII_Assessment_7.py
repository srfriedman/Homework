#CSII Assessment #1
#Question #7
#Sarah Friedman

try:
    text = open("Alice's_Adventures_In_Wonderland", "r")
    text = text.read()

    def key_sort(text):
        dict = {}
        dictTwo = {}
        word = ''
        for aline in text:
            letter = aline
            if letter != ' ':
                word = word + letter
            else:
                dict[word] = text.count(word)
                word = ''
        key_list = list(dict.keys())
        key_list = sorted(dict)
        begin = key_list.index("A")
        for i in key_list[begin:]:
            for i in key_list[begin:]:
                dictTwo[i] = text.count(i)
            return dictTwo

    dict = key_sort(text)

    try:
        file = open("Written_Alice", "w")
        try:
            file.write(str(dict))
        finally:
            file.close()
    finally:
        file = open("Written_Alice", "w")
        file.close()
except IOError:
    print("This file is not found.")
