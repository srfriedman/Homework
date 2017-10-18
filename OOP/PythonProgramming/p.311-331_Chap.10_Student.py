#Reading p. 311-331
#10/17/17
#Sarah Friedman

#Student Exercise

#Complete the student example. You will need to download the graphics module located in the Object and
# Classes Topic on the Topics page. Make sure that this module is in the same folder or directory as your programs that
# use it so that Python can find it. A description of the graphics module is located in the topics section with the .py
# file for further documentation on how to implement the graphics module.

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split()
    return Student(name, hours, qpoints)

def main():
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    best = makeStudent(infile.readline())

    for line in infile:
        s = makeStudent(line)

        if s.gpa() > best.gpa():
            best = s

    infile.close()

    print("The best student is:", best.getName())
    print("Hours:", best.getHours())
    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
