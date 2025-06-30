import collections

def getNthHighestSalary(n: int, employees: list[dict]) -> int | None:
    """
    Finds the nth highest distinct salary from a list of employee dictionaries.

    Args:
        n: The desired rank (e.g., 1 for highest, 2 for second highest).
        employees: A list of dictionaries, where each dictionary represents an employee
                   and has 'id' and 'salary' keys.

    Returns:
        The nth highest distinct salary, or None if there are fewer than n distinct salaries.
    """
    if not employees:
        return None

    salaries = set()
    for employee in employees:
        salaries.add(employee['salary'])

    distinct_salaries = sorted(list(salaries), reverse=True)

    if n <= 0:
        return None # Invalid n

    if n > len(distinct_salaries):
        return None
    else:
        return distinct_salaries[n - 1]

# Example Usage (as per problem description's example format, though not part of the function itself)
# This part is for demonstration and testing, not part of the required function output.
# If this were a LeetCode problem, the function would be called by their test harness.

# Example 1:
# employees1 = [
#     {'id': 1, 'salary': 100},
#     {'id': 2, 'salary': 200},
#     {'id': 3, 'salary': 300}
# ]
# n1 = 2
# result1 = getNthHighestSalary(n1, employees1)
# print(f"getNthHighestSalary({n1}) -> {result1}") # Expected: 200

# Example 2:
# employees2 = [
#     {'id': 1, 'salary': 100}
# ]
# n2 = 2
# result2 = getNthHighestSalary(n2, employees2)
# print(f"getNthHighestSalary({n2}) -> {result2}") # Expected: None

# Example with duplicate salaries:
# employees3 = [
#     {'id': 1, 'salary': 100},
#     {'id': 2, 'salary': 200},
#     {'id': 3, 'salary': 200},
#     {'id': 4, 'salary': 300},
#     {'id': 5, 'salary': 100}
# ]
# n3 = 2
# result3 = getNthHighestSalary(n3, employees3)
# print(f"getNthHighestSalary({n3}) -> {result3}") # Expected: 200 (Distinct salaries: 300, 200, 100)

# n4 = 1
# result4 = getNthHighestSalary(n4, employees3)
# print(f"getNthHighestSalary({n4}) -> {result4}") # Expected: 300

# n5 = 3
# result5 = getNthHighestSalary(n5, employees3)
# print(f"getNthHighestSalary({n5}) -> {result5}") # Expected: 100

# n6 = 4
# result6 = getNthHighestSalary(n6, employees3)
# print(f"getNthHighestSalary({n6}) -> {result6}") # Expected: None

# Example with empty employee list:
# employees_empty = []
# n_empty = 1
# result_empty = getNthHighestSalary(n_empty, employees_empty)
# print(f"getNthHighestSalary({n_empty}) -> {result_empty}") # Expected: None

# Example with n=0 or negative n:
# employees_pos = [{'id': 1, 'salary': 100}]
# n_zero = 0
# result_zero = getNthHighestSalary(n_zero, employees_pos)
# print(f"getNthHighestSalary({n_zero}) -> {result_zero}") # Expected: None

# n_neg = -1
# result_neg = getNthHighestSalary(n_neg, employees_pos)
# print(f"getNthHighestSalary({n_neg}) -> {result_neg}") # Expected: None