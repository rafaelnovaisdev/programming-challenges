import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Find all rows where salary == max salary in that department
    mask = employee['salary'] == employee.groupby('departmentId')['salary'].transform('max')
    top_employees = employee[mask]

    # Merge only required department info and avoid _x/_y renaming by using suffixes
    top_employees = pd.merge(
        top_employees,
        department[['id', 'name']],
        left_on="departmentId",
        right_on="id",
        how="left",
        validate="many_to_one",
        suffixes=('', '_department')
    )

    # Rename column names
    top_employees.rename(columns={
        'name': 'Employee',
        'name_department': 'Department',
        'salary': 'Salary'
    }, inplace=True)

    return top_employees[['Department', 'Employee', 'Salary']]