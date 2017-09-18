#Counting Letters Lab
#Sarah Friedman
#9/18/17

string = str(input("Input a string: "))

dictionary = {}


def countAll(text):
    for letter in text:
        dictionary[letter] = text.count(letter)
countAll(string)
print(dictionary)
