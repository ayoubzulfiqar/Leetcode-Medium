class Solution:
    def deductSalaries(self, employees: list[dict], deduction_percentage: float) -> list[dict]:
        deduction_factor = 1 - (deduction_percentage / 100.0)
        
        deducted_employees = []
        for employee in employees:
            updated_employee = employee.copy() 
            
            new_salary = updated_employee['salary'] * deduction_factor
            rounded_salary = round(new_salary, 2)
            
            updated_employee['salary'] = rounded_salary
            deducted_employees.append(updated_employee)
            
        return deducted_employees

if __name__ == '__main__':
    solution = Solution()

    # Example 1: Basic deduction
    employees1 = [
        {"id": 1, "name": "Alice", "salary": 1000.0},
        {"id": 2, "name": "Bob", "salary": 2500.50},
        {"id": 3, "name": "Charlie", "salary": 500.0}
    ]
    deduction_percentage1 = 10.0
    result1 = solution.deductSalaries(employees1, deduction_percentage1)
    print(result1)

    # Example 2: Different deduction percentage
    employees2 = [
        {"id": 10, "name": "David", "salary": 1500.75},
        {"id": 20, "name": "Eve", "salary": 3000.0}
    ]
    deduction_percentage2 = 5.0
    result2 = solution.deductSalaries(employees2, deduction_percentage2)
    print(result2)

    # Example 3: Empty employee list
    employees3 = []
    deduction_percentage3 = 15.0
    result3 = solution.deductSalaries(employees3, deduction_percentage3)
    print(result3)

    # Example 4: Zero deduction
    employees4 = [
        {"id": 1, "name": "Frank", "salary": 100.0}
    ]
    deduction_percentage4 = 0.0
    result4 = solution.deductSalaries(employees4, deduction_percentage4)
    print(result4)

    # Example 5: Salary requiring precise rounding
    employees5 = [
        {"id": 1, "name": "Grace", "salary": 99.999}
    ]
    deduction_percentage5 = 10.0
    result5 = solution.deductSalaries(employees5, deduction_percentage5)
    print(result5)