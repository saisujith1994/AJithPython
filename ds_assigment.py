"""
list- append(), pop(), insert(), remove(), reverse()
tuple- append(), pop()
set - add(), remove()
dictionary - keys, values, get, items
"""
students={}
recent=[]
departments=set()

def add_student(students, recent, departments, sid, name, dept, marks):
    students[sid]=(name,dept,marks)
    recent.append(sid)
    departments.add(dept)
    print("added student id:",sid)
def remove_student(students, recent,sid):
    students.pop(sid)
    recent.remove(sid)
    print(f"Removed the student {sid}\n")
def get_student(students,sid):
    return students.get(sid,'Not found')
def show_departments(departments):
    return departments
def reverse_recent(recent):
    return recent[::-1]
def display_all(students):
    for sid, info in students.items():
        print(f"Student id: {sid} \n Info: {info}")
add_student(students,recent,departments,'12',"sai",120,98)
add_student(students,recent,departments,'13',"siri",120,88)
add_student(students,recent,departments,'14',"sai ram",122,78)
add_student(students,recent,departments,'15',"sirisha",123,95)
add_student(students,recent,departments,'11',"om",122,89)
add_student(students,recent,departments,'10',"rizwan",121,79)
print("Departments: ",show_departments(departments))
print("Most recent studnets: ",reverse_recent(recent))
display_all(students)
print("student details are: ",get_student(students,'11'))