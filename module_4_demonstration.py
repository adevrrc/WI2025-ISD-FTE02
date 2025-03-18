"""This module is used to demonstrate concepts from module 4."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

import sys
from user_interface.student_listing import StudentListing
from PySide6.QtWidgets import QApplication
from user_interface.grade_point_average_calculator import GradePointAverageCalculator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = StudentListing()

    # TEST
    #mainWindow = GradePointAverageCalculator("99999", "Damien")

    mainWindow.show()
    sys.exit(app.exec())