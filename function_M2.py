"""
Functia de countPassedStudentsM1 este un mutant al functiei countPassedStudents, un n-order-mutant, n = 3
avand ca modificari la linia 26, (student.year < 1 or student.year > 4)  -> student.year < 1
la linia 45, grade.grade < 1  -> grade.grade < 9
la linia 58,  !=  ->  ==
Rezultatul este acesta: 9 teste omoara mutantul acesta, dintre care 8 dau FAIL, iar unul Eroare din cauza valorilor
schimbate in functie ca urmare a mutatiei, facand astfel diferenta intre programul initial si cel mutant.

Programul nu este doar adus pe alta ramura a acestuia, rezultatul returnat este complet diferit din cauza mutatiei,
rezultanda ca mutatia countPassedStudentsM2 este una puternica (Strong Mutation).
"""


def countPassedStudentsM2(students, courses, grades):
    studentsDict = {}
    coursesDict = {}
    studentsScore = {}
    gradedCoursesPerStudent = {}
    noOfPassedStudents = 0
    totalCredits = 0

    for student in students:
        if student.firstName + student.lastName in studentsDict.keys():
            return 'DUPLICATE_STUDENTS'
        else:
            if student.year < 1:
                return 'INVALID_STUDENT_YEAR'
            studentsDict[student.firstName + student.lastName] = student
            studentsScore[student.firstName + student.lastName] = 0

    for course in courses:
        if course.name in coursesDict.keys():
            return 'DUPLICATE_COURSE'
        else:
            if course.noOfCredits < 1 or course.noOfCredits > 6:
                return 'INVALID_COURSE_CREDIT_NUMBER'
            coursesDict[course.name] = course
            totalCredits += course.noOfCredits

    for grade in grades:
        if grade.student.firstName + grade.student.lastName not in studentsDict.keys():
            return 'GRADE_STUDENT_DOES_NOT_EXIST'
        if grade.course.name not in coursesDict.keys():
            return 'GRADE_COURSE_DOES_NOT_EXIST'
        if grade.grade < 9 or grade.grade > 10:
            return 'INVALID_GRADE_VALUE'
        studentsScore[grade.student.firstName + grade.student.lastName] += grade.grade * grade.course.noOfCredits
        if grade.student.firstName + grade.student.lastName not in gradedCoursesPerStudent.keys():
            gradedCoursesPerStudent[grade.student.firstName + grade.student.lastName] = [grade.course.name]
        else:
            if grade.course.name in gradedCoursesPerStudent[grade.student.firstName + grade.student.lastName]:
                return 'SAME_COURSE_GRADED_TWICE'
            else:  # adds grade course to list of courses the student has been graded on
                gradedCoursesPerStudent.update({grade.student.firstName + grade.student.lastName: [
                    *gradedCoursesPerStudent[grade.student.firstName + grade.student.lastName], grade.course.name]})

    for student in studentsScore.keys():
        if len(gradedCoursesPerStudent[student]) == len(courses):
            return 'NOT_ALL_COURSES_HAVE_BEEN_GRADED'
        if studentsScore[student] / totalCredits >= 5:
            noOfPassedStudents += 1
    return noOfPassedStudents
