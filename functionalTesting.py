from classes import Course, Student, Grade
from function import countPassedStudents
import unittest

from tryFunction import tryCountPassedStudents


class FunctionalTests(unittest.TestCase):
    # functii pentru partitioanre pe echivalenta
    # C1:  inputuri invalide - nu sunt liste de studenti, cursuri, respectiv note.
    def test_echiv_c1(self):
        with self.assertRaises(TypeError):
            tryCountPassedStudents(1, "sadads", 0)

    # C2: lista goala de studenti, lista goala de cursuri, lista goala de note - va returna 0

    def test_echiv_c2(self):
        result = tryCountPassedStudents([], [], [])
        self.assertEqual(result, 0)

    # C3: lista goala de studenti, lista cu cursuri, lista goala de note - 0
    def test_echiv_c3(self):
        result = tryCountPassedStudents([], [Course("OOP", 6)], [])
        self.assertEqual(result, 0)

    # C4: studenti, fara cursuri, fara note - KeyError
    def test_echiv_c4(self):
        with self.assertRaises(KeyError):
            tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihai", "Cioinica", 1)], [], [])

    # C5: studenti, cursuri, fara note - NOT_ALL_COURSES_HAVE_BEEN_GRADED
    def test_echiv_c5(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihai", "Cioinica", 1)],
                                        [Course("OOP", 6), Course("LFA", 4)],
                                        [Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                         Grade(Student("Mihai", "Cioinica", 3), Course("LFA", 4), 8), ])
        self.assertEqual(result, "NOT_ALL_COURSES_HAVE_BEEN_GRADED")

    # C6: cursuri sau studenti duplicate - DUPLICATE
    def test_echiv_c6(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Petru", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)], [])
        self.assertRegex(result, "DUPLICATE_[a-zA-Z]*")

    # C7: note cu cursuri sau studenti inexistenti - *_DOES_NOT_EXIST
    def test_echiv_c7(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)],
                                        [Grade(Student("George", "Ionici", 4), Course("OOP", 5), 4)])
        self.assertRegex(result, "[a-zA-Z]*._DOES_NOT_EXIST")

    # C8: mai putine note decat cursuri * studenti - NOT_ALL_COURSES_HAVE_BEEN_GRADED
    def test_echiv_c8(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                            Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 4)])
        self.assertEqual(result, "NOT_ALL_COURSES_HAVE_BEEN_GRADED")

    # C9: liste cu componente valide - returneaza nr de studenti cu media peste 5
    def test_echiv_c9(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                            Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 4),
                                            Grade(Student("Mihail", "Cioinica", 3), Course("LFA", 6), 10)])
        self.assertGreaterEqual(result, 0)

    # C10 input cu doua gradeuri care au acelasi curs si acelasi student - SAME_COURSE_GRADED_TWICE
    def test_echiv_c10(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                            Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 4),
                                            Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 10)])
        self.assertEqual(result, "SAME_COURSE_GRADED_TWICE")

    # urmatoarele teste sunt pentru boundry value analysis

    # toate listele goale
    def test_boundry_1(self):
        result = tryCountPassedStudents([], [], [])
        self.assertEqual(result, 0)

    # nota mai mare de 10
    def test_boundry_2(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 255),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                        ])
        self.assertEqual(result, "INVALID_GRADE_VALUE")

    # nota mai mica de 1
    def test_boundry_3(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 3)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 0),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                        ])
        self.assertEqual(result, "INVALID_GRADE_VALUE")

    # student cu an mai mare decat 4
    def test_boundry_4(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 12)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                        ])
        self.assertEqual(result, "INVALID_STUDENT_YEAR")

    # student cu an mai mic decat 1
    def test_boundry_5(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 0)],
                                        [Course("OOP", 6), Course("LFA", 4)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                        ])
        self.assertEqual(result, "INVALID_STUDENT_YEAR")

    # curs cu numar de credite mai mare decat 6
    def test_boundry_6(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 1)],
                                        [Course("OOP", 6), Course("LFA", 20)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                        ])
        self.assertEqual(result, "INVALID_COURSE_CREDIT_NUMBER")

    # curs cu numar de credite mai mic decat 1
    def test_boundry_7(self):
        result = tryCountPassedStudents([Student("Petru", "Cioinica", 1)],
                                        [Course("OOP", 6), Course("LFA", 0)], [
                                            Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                            Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                        ])
        self.assertEqual(result, "INVALID_COURSE_CREDIT_NUMBER")
