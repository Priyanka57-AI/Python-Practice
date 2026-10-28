class Student:
    def __init__(self):
        self.__name = ""
        self.__rollno = 0

    def setterMethod(self, name, rollno):
        self.__name = name
        self.__rollno = rollno

    def getterMethod(self):
        return self.__name, self.__rollno


student = Student()

name = input("Enter your name: ")
rollno = int(input("Enter your roll number: "))

student.setterMethod(name, rollno)

name, rollno = student.getterMethod()

print("Name:", name)
print("Roll number:", rollno)