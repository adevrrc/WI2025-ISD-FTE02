from course.course import Course
from department.department import Department
from student.student import Student

class LectureCourse(Course):
    
    def __init__(self, name: str, department: Department, credit_hours: int,
                 capacity: int, current_enrollment: int, lecture_hall: str):
        super().__init__(name, department, credit_hours, capacity, current_enrollment)

        # TODO
        # Validate lecture hall argument (not blank)

        self.__lecture_hall = lecture_hall

    def enroll_student(self, student: Student) -> str:
        """Enrolls the specified student in this course.
        
        Args:
            student (Student): The student being add to this course.
        
        Returns:
            str: The enrollment status.
        """

        allowable_enrollment = int(self._capacity + (self._capacity * .1))

        if self._current_enrollment < allowable_enrollment:
            self._current_enrollment += 1

            enrollment_status = (f"{student.name} has been successfully"
                                 f" enrolled in {self.name}.")
        else:
            enrollment_status = (f"{student.name} has NOT been enrolled in "
                                 f"lecture: {self.name} due to insufficient "
                                 "capacity.")

        return enrollment_statusa
