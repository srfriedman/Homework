#HTCS 11.8 Exercise 1
#Sarah Friedman
#9/12/17

file = open("studentdata.txt", "r")

for line in file:
    index = line.split()
    print(index)
    if len(index[1:]) > 6:
        print(index[0])

file.close()
