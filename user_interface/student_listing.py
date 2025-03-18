"""This module defines the StudentListing class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt, Slot
from student.student import Student
from department.department import Department
from demo_superclasses.listing import Listing
from user_interface.grade_point_average_calculator import GradePointAverageCalculator

class StudentListing(Listing):
    """Represents a window which displays student data.

    Inherited from Listing which provides the gui design.
    """

    def __init__(self):
        """Initialize a new instance of the StudentListing class."""

        super().__init__()

        self.students = []
        self.students.append(Student("Janine Wharton", Department.COMPUTER_SCIENCE))
        self.students.append(Student("Freddie Jeffries", Department.MEDICINE))
        self.students.append(Student("Paul Thompson", Department.COMPUTER_SCIENCE))
        self.students.append(Student("Suzanne Marchand", Department.EDUCATION))
        
        self.student_table.setRowCount(len(self.students))

        row = 0

        for student in self.students:
            student_number_item = QTableWidgetItem(str(student.student_number))

            name_item = QTableWidgetItem(student.name)

            grade_point_average_item = QTableWidgetItem(f"{student.grade_point_average:.2f}")

            grade_point_average_item.setTextAlignment(Qt.AlignRight)

            self.student_table.setItem(row, 0, student_number_item)

            self.student_table.setItem(row, 1, name_item)

            self.student_table.setItem(row, 2, grade_point_average_item)

            row += 1

        self.student_table.resizeColumnsToContents()

        self.student_table.cellClicked.connect(self.__on_select_student)

    @Slot(int, int)
    def __on_select_student(self, row: int, column: int):
        """Obtain values from a clicked row.

        Connected to the cellClicked event of a QTable and therefore 
        has row/column arguments.

        Args:
            row (int): Row that has been clicked on.
            column(int): Column that has been clicked on.
        """
        
        student_number = self.student_table.item(row, 0).text()
        name = self.student_table.item(row, 1).text()

        calculator_window = GradePointAverageCalculator(student_number, name)

        calculator_window.exec_()

    def __update_grade_point_average(self, student_number: str, grade_point_average: float):
        """Updates the GPA value based on updates made in another 
        window. The other window sends a signal upon updating, and this 
        slot receives the signal.

        Args:
            student_number (str): The impacted student number.
            gpa (float): The updated gpa value.
        """

        pass
