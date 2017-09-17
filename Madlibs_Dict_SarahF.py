#Madlibs with Dictionary
#Sarah Friedman
#9/17/17

string = open("Madlibs.txt", "r")
string = string.read()

input_one = input("Enter a place: ")
input_two = input("Enter a noun: ")
input_three = input("Enter a name: ")
input_four = input("Enter an adjective: ")
input_five = input("Enter an adjective: ")
input_six = input("Enter a food: ")
input_seven = input("Enter an adjective: ")
input_eight = input("Enter an adjective: ")
input_nine = input("Enter an adjective: ")

replaceWith = {}

replaceWith["1"] = [input_one]
replaceWith["2"] = [input_two]
replaceWith["3"] = [input_three]
replaceWith["4"] = [input_four]
replaceWith["5"] = [input_five]
replaceWith["6"] = [input_six]
replaceWith["7"] = [input_seven]
replaceWith["8"] = [input_eight]
replaceWith["9"] = [input_nine]

print(replaceWith)

newString = []
words = string.split()
print(words)

for word in words:
    if word in replaceWith:
        newString.append(replaceWith[word])
    else:
        newString.append(word)

print(newString)
print("".join(newString))

