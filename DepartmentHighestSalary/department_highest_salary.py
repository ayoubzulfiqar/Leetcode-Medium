import pandas as pd

def find_highest_salary_employees(employee_data: list[dict], department_data: list[dict]) -> pd.DataFrame:
    employee_df = pd.DataFrame(employee_data)
    department_df = pd.DataFrame(department_data)

    employee_df['max_dept_salary'] = employee_df.groupby('departmentId')['salary'].transform('max')

    highest_salary_employees = employee_df[employee_df['salary'] == employee_df['max_dept_salary']]

    result_df = pd.merge(
        highest_salary_employees,
        department_df,
        left_on='departmentId',
        right_on='id',
        suffixes=('_emp', '_dept')
    )

    final_output = result_df[[
        'name_dept',
        'name_emp',
        'salary'
    ]]

    final_output = final_output.rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })

    return final_output