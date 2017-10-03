#HTCS 11.8 Exercise 1
#Sarah Friedman
#9/12/17


file = open("studentdata.txt", "r")

for line in file:
    index = line.split()
    num = str(index)
    num.replace('[', '')
    num.replace(']', '')
    print(num)


file.close()
