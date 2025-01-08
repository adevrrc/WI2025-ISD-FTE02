"""This module defines the Course class."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

from department.department import Department

class Course:
    """Represents a course at an educational institution."""

    def __init__(self, name: str, department: Department, credit_hours: int):
        """Initializes a new instance of the Course class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is 
                delivered.
            credit_hours (int): The number of credit hours.

        Raises:
            TODO
        """

        name = name.strip()
        
        if len(name) == 0:
            raise ValueError("Name cannot be blank.")
        
        # TODO: need to speak to Damien about this.
        # if department not in Department:
        #     raise ValueError("Department is not valid.")

        if not isinstance(credit_hours, int):
            raise ValueError("Credit Hours must be numeric.")

        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours

    @property
    def name(self) -> str:
        """TODO"""

        return self.__name
    
    @property
    def department(self) -> Department:
        return self.__department
    
    @property
    def credit_hours(self) -> int:
        return self.__credit_hours
    
    def __str__(self) -> str:
        """TODO"""

        string_representation = f"Course: {self.name}\n" \
            f"Department: {self.department.name.replace("_", " ").title()}\n" \
            f"Credit Hours: {self.credit_hours}"

        return string_representation
