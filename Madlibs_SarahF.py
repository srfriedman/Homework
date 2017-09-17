#Madlibs
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

string = string.replace("1", input_one)
string = string.replace("2", input_two)
string = string.replace("3", input_three)
string = string.replace("4", input_four)
string = string.replace("5", input_five)
string = string.replace("6", input_six)
string = string.replace("7", input_seven)
string = string.replace("8", input_eight)
string = string.replace("9", input_nine)

print(string)

