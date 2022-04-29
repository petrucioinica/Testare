# student - student
class Student:
    def __init__(self, firstName, lastName, year):
        self.firstName = firstName
        self.lastName = lastName
        self.year = year


# class - materie
class Course:
    def __init__(self, name, noOfCredits):
        self.name = name
        self.noOfCredits = noOfCredits


# clasa grade reprezinta nota unui student la o
class Grade:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade