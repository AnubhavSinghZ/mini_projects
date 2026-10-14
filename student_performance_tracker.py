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
        