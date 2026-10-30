import unittest

from student_marks import calculate_average, generate_report, get_grade


class TestStudentMarks(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 90, 70]), 80)

    def test_grade_A(self):
        self.assertEqual(get_grade(95), "A")

    def test_grade_B(self):
        self.assertEqual(get_grade(80), "B")

    def test_grade_C(self):
        self.assertEqual(get_grade(60), "C")

    def test_grade_F(self):
        self.assertEqual(get_grade(40), "F")

    def test_empty_marks(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_average([80, 120])

    def test_negative_marks(self):
        with self.assertRaises(ValueError):
            calculate_average([-10, 80])

    def test_empty_student_name(self):
        with self.assertRaises(ValueError):
            generate_report(" ", [80, 90])

    def test_student_report(self):
        report = generate_report("Kavana", [80, 90, 70])
        self.assertEqual(report["name"], "Kavana")
        self.assertEqual(report["average"], 80)
        self.assertEqual(report["grade"], "B")


if __name__ == "__main__":
    unittest.main(verbosity=2)
