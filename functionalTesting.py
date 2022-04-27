from function import Student, Course, Grade, countPassedStudents
import unittest


def tryCountPassedStudents(students, courses, grades):
    try:
        countPassedStudents(students, courses, grades)
    except TypeError:
        raise TypeError


class FunctionalTests(unittest.TestCase):
    # functii pentru partitioanre pe echivalenta
    # C1:  inputuri invalide - nu sunt liste de studenti, cursuri, respectiv note.
    def test_echiv_c1(self):
        with self.assertRaises(TypeError):
            tryCountPassedStudents(1, "sadads", 0)

    # C2: lista goala de studenti, lista goala de cursuri, lista goala de note - va returna 0

    def test_echiv_c2(self):
        result = countPassedStudents([], [], [])
        self.assertEqual(result, 0)

    # C3: lista goala de studenti, lista cu cursuri, lista goala de note - 0
    def test_echiv_c3(self):
        result = countPassedStudents([], [Course("OOP", 6)], [])
        self.assertEqual(result, 0)

    # C4: studenti, fara cursuri, fara note - KeyError
    def test_echiv_c4(self):
        with self.assertRaises(KeyError):
            tryCountPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihai", "Cioinica", 1)], [], [])

    # C5: studenti, cursuri, fara note - NOT_ALL_COURSES_HAVE_BEEN_GRADED
    def test_echiv_c5(self):
        result = countPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihai", "Cioinica", 1)],
                                     [Course("OOP", 6), Course("LFA", 4)],
                                     [Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                      Grade(Student("Mihai", "Cioinica", 3), Course("LFA", 4), 8), ])
        self.assertEqual(result, "NOT_ALL_COURSES_HAVE_BEEN_GRADED")

    # C6: cursuri sau studenti duplicate - DUPLICATE
    def test_echiv_c6(self):
        result = countPassedStudents([Student("Petru", "Cioinica", 3), Student("Petru", "Cioinica", 3)],
                                     [Course("OOP", 6), Course("LFA", 4)], [])
        self.assertRegex(result, "DUPLICATE_[a-zA-Z]*")

    # C7: note cu cursuri sau studenti inexistenti - *_DOES_NOT_EXIST
    def test_echiv_c7(self):
        result = countPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                     [Course("OOP", 6), Course("LFA", 4)],
                                     [Grade(Student("George", "Ionici", 4), Course("OOP", 5), 4)])
        self.assertRegex(result, "[a-zA-Z]*._DOES_NOT_EXIST")

    # C8: mai putine note decat cursuri * studenti - NOT_ALL_COURSES_HAVE_BEEN_GRADED
    def test_echiv_c8(self):
        result = countPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                     [Course("OOP", 6), Course("LFA", 4)], [
                                         Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                         Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                         Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 4)])
        self.assertEqual(result, "NOT_ALL_COURSES_HAVE_BEEN_GRADED")

    # C9: liste cu componente valide - returneaza nr de studenti cu media peste 5
    def test_echiv_c9(self):
        result = countPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                     [Course("OOP", 6), Course("LFA", 4)], [
                                         Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                         Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                         Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 4),
                                         Grade(Student("Mihail", "Cioinica", 3), Course("LFA", 6), 10)])
        print("Result in c8", result)
        self.assertGreaterEqual(result, 0)

    # C10 input cu doua gradeuri care au acelasi curs si acelasi student - SAME_COURSE_GRADED_TWICE
    def test_echiv_c10(self):
        result = countPassedStudents([Student("Petru", "Cioinica", 3), Student("Mihail", "Cioinica", 3)],
                                     [Course("OOP", 6), Course("LFA", 4)], [
                                         Grade(Student("Petru", "Cioinica", 3), Course("OOP", 6), 5),
                                         Grade(Student("Petru", "Cioinica", 3), Course("LFA", 4), 8),
                                         Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 4),
                                         Grade(Student("Mihail", "Cioinica", 3), Course("OOP", 6), 10)])
        print("Result in c8", result)
        self.assertEqual(result, "SAME_COURSE_GRADED_TWICE")
