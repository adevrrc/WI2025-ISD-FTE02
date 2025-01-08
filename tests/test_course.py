"""The module defines the TestCourse class.

Example:
    $ python -m unittest tests/test_course.py
"""

__author__ = "COMP-2327 Faculty, Damien Altenburg"
__version__ = "1.1.2025"

import unittest
from department.department import Department
from course.course import Course

class TestCourse(unittest.TestCase):
    """TODO"""

    def test_init_object_initialized_to_correct_state(self):
        # Arrange
        name = "intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        # Act
        course = Course(name, department, credit_hours)

        # Assert
        self.assertEqual("intermediate software development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(90, course._Course__credit_hours)

if __name__ == "__main__":
    unittest.main()
