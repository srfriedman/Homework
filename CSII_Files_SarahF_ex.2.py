#HTCS 11.8 Exercise 1
#Sarah Friedman
#9/12/17

#DOES NOT WORK

file = open("studentdata.txt", "r")

for line in file:
    index = line.split()
    num = str(index)
    num.replace('[', '')
    num.replace(']', '')
    print(num)


file.close()
