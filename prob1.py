import uuid
from datetime import datetime

#student - student
class Student:
    def __init__(self, firstName, lastName, year):
        self.firstName = firstName
        self.lastName = lastName
        self.year= year

#class - materie
class Course:
    def __init__(self, name, noOfCredits):
        self.name = name
        self.noOfCredits = noOfCredits

#clasa grade reprezinta nota unui student la o
class Grade:
    def __init__(self, student, course, grade):
            self.student = student
            self.course = course
            self.grade = grade


#functie care returneaza numarul de studenti care au media peste 5 (media se calculeaza ponderat in functie de nr de credite)
#sau un mesaj de eroare in functie de validitatea datelor.
#functia primeste ca parametrii o lista de studenti, una de cursuri si una de note
  #cerinte pentru ca datele sa fie valide
    #1. toti studentii si toate cursurile din lista de note trebuie sa fie prezente si in listele lor respective
    #2. toate notele sa fie intre 0 si 10
    #3. toti studentii sa aiba note la toate materiile
    #4. toate elementele din lista trebuie sa fie unice
    #5. toti studentii trebuie sa fie intr-un an intre 1 si 4
#Pentru ca un student sa fie trecut trbuie ca media lui sa fie peste 5
def countPassedStudents(students, courses, grades):
    studentsDict = {}
    coursesDict = {}
    studentsScore = {}
    gradedCoursesPerStudent = {}
    noOfPassedStudents = 0
    totalCredits = 0

    for student in students:
        if student.firstName + student.lastName in studentsDict.keys():
            return 'BAD_DATA'
        else:
            if student.year < 1 or student.year > 4:
                return 'BAD_DATA'
            studentsDict[student.firstName + student.lastName] = student
            studentsScore[student.firstName + student.lastName] = 0

    for course in courses:
       if course.name in coursesDict.keys():
           return 'BAD_DATA'
       else:
           if course.noOfCredits < 1 or course.noOfCredits > 6:
               return 'BAD_DATA'
           coursesDict[course.name] = course
           totalCredits+=course.noOfCredits

    for grade in grades:
        if grade.student.firstName + grade.student.lastName not in studentsDict.keys():
            return 'BAD_DATA'
        if grade.course.name not in coursesDict.keys():
            return 'BAD_DATA'
        if grade.grade < 1 or grade.grade > 10:
            return 'BAD_DATA'
        studentsScore[grade.student.firstName + grade.student.lastName] += grade.grade * grade.course.noOfCredits
        if grade.student.firstName + grade.student.lastName not in   gradedCoursesPerStudent.keys():
            gradedCoursesPerStudent[grade.student.firstName + grade.student.lastName] = [grade.course.name]
        else:
            if grade.course.name in gradedCoursesPerStudent[grade.student.firstName + grade.student.lastName]:
                return 'BAD_DATA'
            else:
                gradedCoursesPerStudent.update({grade.student.firstName + grade.student.lastName: [*gradedCoursesPerStudent[grade.student.firstName + grade.student.lastName], grade.course.name]})

    for student in studentsScore.keys():
        if studentsScore[student] / totalCredits >= 5:
            noOfPassedStudents+=1
    return noOfPassedStudents




students = [
    Student("Petru", "Cioinica", 3),
    Student("Mihai", "Cioinica", 1)
]

classes = [
    Course("OOP", 6),
    Course("LFA", 4),
]

grades = [
    Grade(students[0], classes[0], 5),
    Grade(students[0], classes[1], 8),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]


print(countPassedStudents(students,classes,grades))