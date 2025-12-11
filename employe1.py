def employee_details(name, emp_id, dept, salary):
    return (
        f"Employee Name:{name}\n"
        f"Employee ID:{emp_id}\n"
        f"Department:{dept}\n"
        f"salary:{salary}"
    )
    return result
if __name__=="__main__":
    name="Nagaveni"
    emp_id="E1001"
    department="IT"
    salary=55000
    print(employee_details(name,emp_id,department,salary))
