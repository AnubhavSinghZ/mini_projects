"""
STUDENT PERFORMANCE TRACKER
A step up from basic mini project. It Introduces:
* Classes and objects (OOP)
* Saving / loading data with JSON
* Input validation with try/except
* The statistics module (mean, median)
* An optional chart with matplotlib

It also stores each student's daily study hour. Later you can use that data : predicting marks from study hours.

"""
import json
import os
import statistics

DATA_FILE= os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.join")
SUBJECTS=["MATHS","SCIENCE", "ENGLISH", "HINDI", "COMPUTER"]
PASS_MARK=33


#-----The Student Class-----
class Student:
    def __init__(self, roll_no, name, study_hours, marks=None):
        self.roll_no=roll_no
        self.name=name
        self.study_hours=study_hours  # average hour study per day
        self.marks=marks or {}  # e.g. {Maths:85, Science:89}

    def total(self):
        return sum(self.marks.value())
    
    def average(self):
        return self.total() / len(self.marks) if self.marks else 0
    def grade(self):
        avg=self.average()
        if avg>=90:
            return "A+"
        if avg>=80:
            return "A"
        if avg>=70:
            return  "B"
        if avg>=60:
            return "C"
        if avg>=PASS_MARK:
            return "D"
        return "F"
    def has_passed(self):
        """Pass only if every subject is at or above the pass mark."""
        return bool(self.marks) and all(m>= PASS_MARK for m in self.marks.values())
    def to_dict(self):
        return{
                "roll_no": self.roll_no,
                "name": self.name,
                "study_hours": self.study_hours,
                "marks": self.marks,
            }
    @staticmethod
    def from_dict(data):
        return Student(data["roll_no"], data["name"], data["study_hours"], data["marks"])
    
          # ---- SAVING AND LOADING----
    
def load_students():
    if not os.path.exists(DATA_FILE):
        return[]
    try:
        with open(DATA_FILE, "r",encoding="utf-8") as f:
            return[Student.from_dict(d) for d in json.load(f)]
    except(json.JSONDecodeError, KeyError, OSError):
        print("Could not read the data file. Starting with an empty list.")
        return[]

def save_students(students):
    try:
        with open(DATA_FILE,"w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in students],f, indent=4)
    except OSError:
            print("Error: could not save your data.")   

# ---- Input Helpers----
def get_number(prompt,low, high,as_int=False):
    """"Keep asking until the user enters a number between low and high."""
    while True:
        try:
            value=int(input(prompt)) if as_int else float(input(prompt))
            if low<=value<=high:
                return value
            print(f"Enter a value between {low} and {high}.")
        except ValueError:
            print("Please enter a valid Number.")

def find_student(students,roll_no):
    for s in students:
        if s.roll_no==roll_no:
            return s
        return None

def ask_marks():
    marks={}
    for subject in SUBJECTS:
        marks[subject]=get_number(f"{subject} marks (0=100):" , 0, 100, as_int=True)
    return marks

# ---- Features---

def add_student(students):
    print("\n --- Add Student ---")
    roll_no=get_number("Roll Number:", 1,99999, as_int=False)
    if find_student(students,roll_no):
        print("A student with this roll number already exixts.")
        return
    name =input("Name: ").strip()
    if not name:
        print("Name cannot be empty")
        return
    hours=get_number("Average study hours per day (0-16): ", 0,16)
    print("Enter Marks: ")
    marks=ask_marks()

    students.append(Student(roll_no,name,hours, marks))
    save_students(students)
    print((f"\nAdded {name}"))

def update_marks(students):
    print("\n ---Update Marks ----")
    roll_no=get_number("Roll number: ", 1, 99999, as_int=True)
    student=find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return
    print(f"Updating marks fot {student.name}:")
    student.marks=ask_marks()
    save_students(students)
    print("Mark Updated.")

def delete_student(students):
    print("\n --- Delete Student ---")
    roll_no=get_number("Roll Number: ", 1, 99999, as_int=True)
    student = find_student(students, roll_no)
    if not  student:
        print("Student not found. ")
        return
    students.remove(student)
    save_students(students)
    print(f"Deleted {student.name}")




    
            
                    
                    
    