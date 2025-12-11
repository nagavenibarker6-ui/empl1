from employeeee import employee_details
def test_employee_details():
    expected_output=(
        "Employee Name:Nagaveni\n"
        "Employee ID:E1001\n"
        "Department:IT\n"
        "salary:55000"
    )
    assert employee_details("Nagaveni","E1001","IT",55000)==expected_output