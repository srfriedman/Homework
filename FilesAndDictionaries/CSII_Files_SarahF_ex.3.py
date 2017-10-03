#HTCS 11.8 Exercise 1
#Sarah Friedman
#9/13/17

file = open("studentdata.txt", "r")

for line in file:
    items = line.split()
    print(items[0], "'s max score is:", max(items[1:]), ", and his min score is:", min(items[1:]))

file.close()
