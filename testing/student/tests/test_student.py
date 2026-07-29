from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.test_student = Student("Student", {"Python": ["Fundamental", "OOP", "Advanced"], "DataBases": ["Django"]})

    def test_initialization_with_course_information(self) -> None:
        self.assertEqual("Student", self.test_student.name)
        self.assertEqual(2, len(self.test_student.courses))
        self.assertEqual(("Python", "DataBases"), tuple(self.test_student.courses.keys()))
        self.assertEqual(["Fundamental", "OOP", "Advanced"], self.test_student.courses["Python"])
        self.assertEqual(["Django"], self.test_student.courses["DataBases"])

    def test_initialization_without_course_information(self) -> None:
        new_student = Student("Student")
        self.assertEqual("Student", new_student.name)
        self.assertEqual({}, new_student.courses)

    def test_enroll_with_course_name_which_already_in_dict(self) -> None:
        course_name = "Python"
        notes = ["Course note 1", "Course note 2", "Course note 3"]

        expected_notes = self.test_student.courses[course_name] + notes
        result_string = self.test_student.enroll(course_name, notes)
        self.assertEqual(expected_notes, self.test_student.courses[course_name])
        self.assertEqual("Course already added. Notes have been updated.", result_string)

    def test_enroll_with_course_name_which_already_in_dict_and_empy_notes(self) -> None:
        course_name = "Python"
        notes = []
        # add_course_notes: str = "Y"
        expected_notes = self.test_student.courses[course_name]
        result_string = self.test_student.enroll(course_name, notes)
        self.assertEqual(expected_notes, self.test_student.courses[course_name])
        self.assertEqual("Course already added. Notes have been updated.", result_string)

    def test_enroll_with_new_course_name_add_notes_is_fulled_course_notes_is_empy_or_Y(self) -> None:
        course_name = "C#"
        expected_notes = ["Course note C# 1", "Course note C# 2", "Course note C# 3"]
        add_course_notes: str = ""
        self.assertEqual(2, len(self.test_student.courses))

        result_string = self.test_student.enroll(course_name,expected_notes, add_course_notes)

        self.assertEqual(3, len(self.test_student.courses))
        self.assertEqual(["Python", "DataBases","C#"], list(self.test_student.courses))
        self.assertEqual(expected_notes, self.test_student.courses[course_name])
        self.assertEqual("Course and course notes have been added.", result_string)

        course_name_2 = "C++"
        expected_notes = ["Course note C++ 1", "Course note C++ 2", "Course note C++ 3"]
        add_course_notes: str = "Y"
        self.assertEqual(3, len(self.test_student.courses))

        result_string = self.test_student.enroll(course_name_2, expected_notes, add_course_notes)

        self.assertEqual(4, len(self.test_student.courses))
        self.assertEqual(["Python", "DataBases", "C#", "C++"], list(self.test_student.courses))
        self.assertEqual(expected_notes, self.test_student.courses[course_name_2])
        self.assertEqual("Course and course notes have been added.", result_string)

    def test_enroll_with_new_course_name_add_notes_is_fulled_course_notes_is_N_or_yes_or_y(self) -> None:
        course_name = "C#"
        notes = ["Course note C# 1", "Course note C# 2", "Course note C# 3"]
        add_course_notes: str = "N"
        self.assertEqual(2, len(self.test_student.courses))

        result_string = self.test_student.enroll(course_name, notes, add_course_notes)

        self.assertEqual(3, len(self.test_student.courses))
        self.assertEqual(["Python", "DataBases", "C#"], list(self.test_student.courses))
        self.assertEqual([], self.test_student.courses[course_name])
        self.assertEqual("Course has been added.", result_string)

        course_name_2 = "C++"
        notes: list[str] = ["Course note C++ 1", "Course note C++ 2", "Course note C++ 3"]
        add_course_notes: str = "yes"
        self.assertEqual(3, len(self.test_student.courses))

        result_string = self.test_student.enroll(course_name_2, notes, add_course_notes)

        self.assertEqual(4, len(self.test_student.courses))
        self.assertEqual(["Python", "DataBases", "C#", "C++"], list(self.test_student.courses))
        self.assertEqual([], self.test_student.courses[course_name_2])
        self.assertEqual("Course has been added.", result_string)

        course_name_3 = "C"
        notes: list[str] = ["Course note C 1", "Course note C 2", "Course note C 3"]
        add_course_notes: str = "y"
        self.assertEqual(4, len(self.test_student.courses))

        result_string = self.test_student.enroll(course_name_3, notes, add_course_notes)

        self.assertEqual(5, len(self.test_student.courses))
        self.assertEqual(["Python", "DataBases", "C#", "C++", "C"], list(self.test_student.courses))
        self.assertEqual([], self.test_student.courses[course_name_3])
        self.assertEqual("Course has been added.", result_string)




    def test_enroll_with_new_course_name_notes_add_is_Y(self) -> None:
        course_name = "C#"
        expected_notes = ["Course note 1", "Course note 2", "Course note 3"]
        add_course_notes: str = "Y"
        self.assertEqual(2, len(self.test_student.courses))

        result_string = self.test_student.enroll(course_name, expected_notes, add_course_notes)

        self.assertEqual(3, len(self.test_student.courses))
        self.assertEqual(["Python", "DataBases", "C#"], list(self.test_student.courses))
        self.assertEqual(expected_notes, self.test_student.courses[course_name])
        self.assertEqual("Course and course notes have been added.", result_string)

    def test_add_notes_course_name_is_already_in_list(self) -> None:
        course_name = "Python"
        notes = "Course note 1"

        expected_notes =  ["Fundamental", "OOP", "Advanced", "Course note 1"]
        result_string = self.test_student.add_notes(course_name, notes)
        self.assertEqual(expected_notes, self.test_student.courses[course_name])
        self.assertEqual("Notes have been updated", result_string)

    def test_add_notes_course_name_is_not_in_list(self) -> None:
        course_name = "C#"
        notes = "Course note 1"
        self.assertEqual(2, len(self.test_student.courses))
        with self.assertRaises(Exception) as context:
            self.test_student.add_notes(course_name, notes)
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))
        self.assertEqual(2, len(self.test_student.courses))


    def test_add_notes_course_name_is_NONE(self) -> None:
        course_name = None
        notes = "Course note 1"
        self.assertEqual(2, len(self.test_student.courses))
        with self.assertRaises(Exception) as context:
            self.test_student.add_notes(course_name, notes)
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))
        self.assertEqual(2, len(self.test_student.courses))


    def test_add_notes_course_name_is_empty_string(self) -> None:
        course_name = "Python"
        notes = ""
        expected_notes = ["Fundamental", "OOP", "Advanced", ""]
        result_string = self.test_student.add_notes(course_name, notes)
        self.assertEqual(expected_notes, self.test_student.courses[course_name])
        self.assertEqual("Notes have been updated", result_string)

    def test_leave_course_correct(self) -> None:
        course_name = "Python"

        expected_course_list = ["DataBases"]

        self.assertEqual(2, len(self.test_student.courses.keys()))
        result_string = self.test_student.leave_course(course_name)

        self.assertEqual(expected_course_list, list(self.test_student.courses.keys()))
        self.assertEqual("Course has been removed", result_string)
        self.assertEqual(1, len(self.test_student.courses.keys()))

    def test_leave_INCORRECT_course_name(self) -> None:
        course_name = "C"



        self.assertEqual(2, len(self.test_student.courses.keys()))
        self.assertEqual(["Python", "DataBases"], list(self.test_student.courses.keys()))

        with self.assertRaises(Exception) as context:
            self.test_student.leave_course(course_name)


        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))
        self.assertEqual(2, len(self.test_student.courses.keys()))
        self.assertEqual(["Python", "DataBases"], list(self.test_student.courses.keys()))


if __name__ == '__main__':
    main()
