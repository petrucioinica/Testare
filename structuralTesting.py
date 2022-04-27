from function import Student, Course, Grade, countPassedStudents
import unittest


class StructuralTests(unittest.TestCase):
    # add functions for structural testing
    # all paths are reachable inside the function

    # basic function with empty values, should return 0
    def test_basic_function(self):
        result = countPassedStudents([], [], [])
        self.assertEqual(result, 0)

    # test for a list with more of the same student
    def test_duplicate_students(self):
        result = countPassedStudents(students + students_2, classes, grades)
        self.assertEqual(result, "DUPLICATE_STUDENTS")

    # one student has a Year value greater than 3
    def test_invalid_year(self):
        result = countPassedStudents(students_2, classes, grades)
        self.assertEqual(result, "INVALID_STUDENT_YEAR")

    # more courses have the same name
    def test_duplicate_course(self):
        result = countPassedStudents(students, classes + classes_2, grades)
        self.assertEqual(result, "DUPLICATE_COURSE")

    # one of the courses has an abnormal number of credits
    def test_invalid_courses_credits(self):
        result = countPassedStudents(students, classes_2, grades)
        self.assertEqual(result, "INVALID_COURSE_CREDIT_NUMBER")

    # an inexistent student has been graded
    def test_grades_inexistent_student(self):
        result = countPassedStudents(students, classes, grades_inexistent_student)
        self.assertEqual(result, "GRADE_STUDENT_DOES_NOT_EXIST")

    # a student has been graded for an inexistent course
    def test_grades_inexistent_course(self):
        result = countPassedStudents(students, classes, grades_inexistent_course)
        self.assertEqual(result, "GRADE_COURSE_DOES_NOT_EXIST")

    # the grade is out of bounds (1, 10)
    def test_grades_invalid_grade(self):
        result = countPassedStudents(students, classes, grades_invalid_grades)
        self.assertEqual(result, "INVALID_GRADE_VALUE")

    # the same student has been graded twice for a course
    def test_grades_same_course_graded_twice(self):
        result = countPassedStudents(students, classes, grades_same_course_graded_twice)
        self.assertEqual(result, "SAME_COURSE_GRADED_TWICE")

    # a student has no grade on at least one course
    def test_grades_not_all_courses_graded(self):
        result = countPassedStudents(students, classes, grades_not_all_courses_graded)
        self.assertEqual(result, "NOT_ALL_COURSES_HAVE_BEEN_GRADED")


# 2 studenti normali
students = [
    Student("Petru", "Cioinica", 3),
    Student("Bogdan", "Staicu", 1)
]


# 2 studenti, copie dupa prima lista dar unul din ei are anul invalid
students_2 = [
    Student("Petru", "Cioinica", 3),
    Student("Bogdan", "Staicu", 6)
]


# 2 cursuri cu structura corecta
classes = [
    Course("OOP", 6),
    Course("LFA", 4),
]


# aceleasi 2 cursuri dar unul are numar gresit de credite
classes_2 = [
    Course("OOP", 6),
    Course("LFA", 9),
]


grades = [
    Grade(students[0], classes[0], 5),
    Grade(students[0], classes[1], 8),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]

grades_inexistent_student = [
    Grade(Student("Andrei", "Popescu", 3), classes[0], 5),
    Grade(students[0], classes[1], 8),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]

grades_inexistent_course = [
    Grade(students[0], classes[0], 5),
    Grade(students[0], Course("DAW", 5), 8),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]

grades_invalid_grades = [
    Grade(students[0], classes[0], 13),
    Grade(students[0], classes[1], -4),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]

grades_same_course_graded_twice = [
    Grade(students[0], classes[0], 8),
    Grade(students[0], classes[0], 7),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]

grades_not_all_courses_graded = [
    Grade(students[0], classes[0], 8),
    Grade(students[1], classes[0], 4),
    Grade(students[1], classes[1], 10)
]