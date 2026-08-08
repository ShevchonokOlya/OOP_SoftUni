import unittest
from project.senior_student import SeniorStudent
# import copy

class  TestSeniorStudent(unittest.TestCase):
    def setUp(self):
        self.testingStudent = SeniorStudent("SS01", "Petya Ivanova", 10.0)

    def test_Student_initialization(self):
        self.assertEqual("SS01", self.testingStudent.student_id)
        self.assertEqual("Petya Ivanova", self.testingStudent.name)
        self.assertEqual(10.0, self.testingStudent.student_gpa)
        self.assertEqual(0, len(self.testingStudent.colleges))
        self.assertEqual(set, type(self.testingStudent.colleges))

    def test_set_incorrect_student_id(self):
        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("  01", "Petya Ivanova", 10.0)
        self.assertEqual("Student ID must be at least 4 digits long!", str(exception_context.exception))

        with self.assertRaises(ValueError) as exception_context1:
            self.newStudent = SeniorStudent("    ", "Petya Ivanova", 10.0)
        self.assertEqual("Student ID must be at least 4 digits long!", str(exception_context1.exception))

        with self.assertRaises(ValueError) as exception_context2:
            self.newStudent = SeniorStudent("", "Petya Ivanova", 10.0)
        self.assertEqual("Student ID must be at least 4 digits long!", str(exception_context2.exception))

        # with self.assertRaises(Exception) as exception_context3:
        #     self.newStudent = SeniorStudent("       1   b     ", "Petya Ivanova", 10.0)
        # self.assertEqual("Student ID must be ONLY digits!", str(exception_context3.exception))

        # with self.assertRaises(Exception) as exception_context4:
        #     self.newStudent = SeniorStudent(None, "Petya Ivanova", 10.0)
        # self.assertEqual("Student ID must be at least 4 digits long!", str(exception_context4.exception))

        # with self.assertRaises(Exception) as exception_context5:
        #     self.newStudent = SeniorStudent("NNNN", "Petya Ivanova", 10.0)
        # self.assertEqual("Student ID must have digits!", str(exception_context5.exception))

    def test_set_correct_student_id(self):
        self.newStudent = SeniorStudent("4    5", "Petya Ivanova", 10.0)
        self.assertEqual("4    5", self.newStudent.student_id)

        self.newStudent = SeniorStudent("1234", "Petya Ivanova", 10.0)
        self.assertEqual("1234", self.newStudent.student_id)

        self.newStudent = SeniorStudent("1234   ", "Petya Ivanova", 10.0)
        self.assertEqual("1234", self.newStudent.student_id)

        self.newStudent = SeniorStudent("  1234", "Petya Ivanova", 10.0)
        self.assertEqual("1234", self.newStudent.student_id)

        self.newStudent = SeniorStudent("   1234   ", "Petya Ivanova", 10.0)
        self.assertEqual("1234", self.newStudent.student_id)

        self.newStudent = SeniorStudent("12345", "Petya Ivanova", 10.0)
        self.assertEqual("12345", self.newStudent.student_id)

        self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 10.0)
        self.assertEqual("12B34", self.newStudent.student_id)

        self.newStudent = SeniorStudent("WORD", "Petya Ivanova", 10.0)
        self.assertEqual("WORD", self.newStudent.student_id)

        self.newStudent = SeniorStudent("WORD@_%", "Petya Ivanova", 10.0)
        self.assertEqual("WORD@_%", self.newStudent.student_id)

    def test_set_correct_student_name(self):
        self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 10.0)
        self.assertEqual("Petya Ivanova", self.newStudent.name)

        self.newStudent = SeniorStudent("12B34", " 0 ", 10.0)
        self.assertEqual(" 0 ", self.newStudent.name)

        self.newStudent = SeniorStudent("12B34", "1234", 10.0)
        self.assertEqual("1234", self.newStudent.name)

        self.newStudent = SeniorStudent("12B34", "12\n34", 10.0)
        self.assertEqual("12\n34", self.newStudent.name)

        self.newStudent = SeniorStudent("12B34", "Petya", 10.0)
        self.assertEqual("Petya", self.newStudent.name)

        self.newStudent = SeniorStudent("12B34", "   Petya   ", 10.0)
        self.assertEqual("   Petya   ", self.newStudent.name)

    def test_set_incorrect_student_name(self):
        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("12B34", "          ", 10.0)
        self.assertEqual("Student name cannot be null or empty!", str(exception_context.exception))

        # with self.assertRaises(ValueError) as exception_context:
        #     self.newStudent = SeniorStudent("12B34", None, 10.0)
        # self.assertEqual("Student name cannot be null or empty!", str(exception_context.exception))

    def test_set_correct_student_gpa(self):
        self.newStudent = SeniorStudent("12B34", "Petya Ivanova", float('inf'))
        self.assertEqual(float('inf'), self.newStudent.student_gpa)

        self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 5)
        self.assertEqual(5.0, self.newStudent.student_gpa)

        self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 105)
        self.assertEqual(105.0, self.newStudent.student_gpa)



    def test_set_incorrect_student_gpa(self):
        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 1.0)
        self.assertEqual("Student GPA must be more than 1.0!", str(exception_context.exception))

        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 0.5)
        self.assertEqual("Student GPA must be more than 1.0!", str(exception_context.exception))

        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("12B34", "Petya Ivanova", -0.5)
        self.assertEqual("Student GPA must be more than 1.0!", str(exception_context.exception))

        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("12B34", "Petya Ivanova", 0)
        self.assertEqual("Student GPA must be more than 1.0!", str(exception_context.exception))


        with self.assertRaises(ValueError) as exception_context:
            self.newStudent = SeniorStudent("12B34", "Petya Ivanova", -float('inf'))
        self.assertEqual("Student GPA must be more than 1.0!", str(exception_context.exception))




    def test_correct_applying_to_college(self):

        self.assertEqual(0, len(self.testingStudent.colleges))

        result = self.testingStudent.apply_to_college(2.0, "")

        self.assertEqual(1, len(self.testingStudent.colleges))
        self.assertEqual("", list(self.testingStudent.colleges)[0])
        self.assertEqual(result, f'Petya Ivanova successfully applied to .')

        result = self.testingStudent.apply_to_college(0.0, " ")

        self.assertEqual(2, len(self.testingStudent.colleges))
        self.assertEqual(result, f'Petya Ivanova successfully applied to  .')
        self.assertTrue(' ' in self.testingStudent.colleges)


        result = self.testingStudent.apply_to_college(5.0, "Amherst College")

        self.assertEqual(3, len(self.testingStudent.colleges))
        self.assertEqual('Petya Ivanova successfully applied to Amherst College.', result)
        self.assertTrue('AMHERST COLLEGE' in self.testingStudent.colleges)

        result = self.testingStudent.apply_to_college(10.0, "Babson College")

        self.assertEqual(4, len(self.testingStudent.colleges))
        self.assertEqual( 'Petya Ivanova successfully applied to Babson College.', result)
        self.assertTrue('BABSON COLLEGE' in self.testingStudent.colleges)

        result = self.testingStudent.apply_to_college(2.0, "Babson College")

        self.assertEqual(4, len(self.testingStudent.colleges))
        self.assertEqual('Petya Ivanova successfully applied to Babson College.' , result)



    def test_incorrect_applying_to_college(self):
        # with self.assertRaises(ValueError) as exception_context:
        #     self.testingStudent.apply_to_college(2.0, None)
        # self.assertEqual('Application failed!', str(exception_context.exception))

        self.assertEqual(0, len(self.testingStudent.colleges))

        result = self.testingStudent.apply_to_college(20.0, "Amherst College")
        self.assertEqual('Application failed!', result)
        self.assertFalse('AMHERST COLLEGE' in self.testingStudent.colleges)

        self.assertEqual(0, len(self.testingStudent.colleges))


        result = self.testingStudent.apply_to_college(10.1, "Amherst College")
        self.assertEqual('Application failed!', result)

        self.assertEqual(0, len(self.testingStudent.colleges))

    def test_correct_update_gpa(self):

        self.assertEqual(10.0, self.testingStudent.student_gpa)
        result = self.testingStudent.update_gpa(30.0)
        self.assertEqual(30.0, self.testingStudent.student_gpa)
        self.assertEqual('Student GPA was successfully updated.', result)

        self.assertEqual(30.0, self.testingStudent.student_gpa)
        result = self.testingStudent.update_gpa(10.0)
        self.assertEqual(10.0, self.testingStudent.student_gpa)
        self.assertEqual('Student GPA was successfully updated.', result)



    def test_incorrect_update_gpa(self):

        self.assertEqual(10.0, self.testingStudent.student_gpa)
        result = self.testingStudent.update_gpa(1.0)
        self.assertEqual(10.0, self.testingStudent.student_gpa)
        self.assertEqual('The GPA has not been changed!', result)

        self.assertEqual(10.0, self.testingStudent.student_gpa)
        result = self.testingStudent.update_gpa(0.0)
        self.assertEqual(10.0, self.testingStudent.student_gpa)
        self.assertEqual('The GPA has not been changed!', result)

        self.assertEqual(10.0, self.testingStudent.student_gpa)
        result = self.testingStudent.update_gpa(-float('inf'))
        self.assertEqual(10.0, self.testingStudent.student_gpa)
        self.assertEqual('The GPA has not been changed!', result)

    def test_dandere_method_of_equaling(self):
        student_a = SeniorStudent("12BN", "Alice", 4.0)
        student_b = SeniorStudent("12BO", "Bob", 4.0)

        self.assertFalse(student_a is student_b)
        self.assertTrue(student_a == student_b)

        student_c = SeniorStudent("12BN", "Alice", 4.0)
        student_c.update_gpa(3.5)
        self.assertFalse(student_a == student_c)

        # student_e = copy.copy(student_a)
        # self.assertFalse(student_a is student_e)
        # self.assertTrue(student_a == student_e)
        # student_e.update_gpa(3.5)
        # self.assertFalse(student_a == student_e)


if __name__ == "__main__":
    unittest.main()
