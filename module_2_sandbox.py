class Employee:

    def __init__(self, employee_id: int):
        self.__employee_id = employee_id

    @property
    def employee_id(self) -> int:
        return self.__employee_id
    
    def __str__(self) -> str:
        return "Employee"
    
class HourlyEmployee(Employee):
    
    def __init__(self, employee_id: int, hours: int, rate: float):

        super().__init__(employee_id)
        
        self.__hours = hours
        self.__rate = rate

    def __str__(self):
        # HourlyEmployee
        return "Hourly" + super().__str__()

def main():
    employee = Employee(123)
    print(employee.employee_id)

    print(employee)

    employee = HourlyEmployee(234, 40, 10)
    print(employee.employee_id)

    print(type(employee))

    print(isinstance(employee, HourlyEmployee))
    print(isinstance(employee, Employee))

    # These statements would produce errors
    # print(employee.__employee_id)
    # print(employee.__hours)
    # print(employee.__rate)

    print(employee)

    output = str(employee)
    print(output)

    print(repr(employee))

if __name__ == "__main__":
    main()
