# This project allows the user to view, enter, and manipulate student grades.
# This pov of the individual using this program, would be the instructor. 

# Gui stuff
#import PySimpleGUI as psg 
#psg.Window(title="Student Grading", layout=[[]], margins=(350, 250)).read()

# Creating file to store assignments / grades if it doesn't already exist 
f = open("StuGrades.txt","w")


# Defining a class for Students
class Student:
	def __init__(self, f_name, l_name, course, gpa = 4.0):
		self.f_name = f_name
		self.l_name = l_name
		self.course = course
		self.gpa = gpa
	
	def get_info(self):
		print(self.f_name, self.l_name)
		print(self.course)
		print(self.gpa)


# Defining Assignments, the class respo
class Assignments():
	def __init__(self, student = ' ', course=' ', level=' ', grade = 'A'):
		self.student = student
		self.course = course
		self.level = level
		self.grade = grade

	def add_grade(self, grade):
		ls.append(self.grade)

	def edit_grade(self):
		pass
	def del_grade(self):
		pass

	def print_grade(self):
		print(ls)

# Homework subclass inheriting from Assignments 
class Homework(Assignments):
	def __init__(self, grade):
		super().__init__(grade)

# Test subclass inheriting from Assignments 
class Test(Assignments):
	def __init__(self, student, course, level, grade):
		pass

# Function for average grade
def average_grade(lists):
    val = 0 # initializing value
    for i in lists:
        val = val + i          

    avg = val / len(lists)
    return avg

