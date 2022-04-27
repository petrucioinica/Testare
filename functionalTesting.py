from function import Student, Course, Grade, countPassedStudents
import unittest

class FunctionalTests(unittest.TestCase):
    #add functions (2 for functional testing, 3 for structural testing)
   def test_function(self):
       result =countPassedStudents([], [], [])
       self.assertEqual(result, 0)


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
