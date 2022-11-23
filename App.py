# This app needs to meet certain requirments.


# Importing necessary modules 
import json
import random


# Student Class
class Student():
	def __init__(self, name, courses, grades):
		self.name = name
		self.courses = courses
		self.grades = grades

	def show(self):
		print(f"Student Name: {self.name}")
		print(f"Courses: {self.courses}")
		print(f"Grades: {self.grades}\n")

def average(dictionary):
	avg = 0
	for key, val in dictionary.items():
		avg += int(val)
	avg /= len(dictionary)
	return avg


# DEFINING STUDENTS

# Student courses
gina_courses = ['SWE', 'CALC', 'ENGL']
jay_courses = ['SWE', 'SCI', 'ENGL']
mark_courses = ['SWE', 'BIO', 'CHEM']

# Student grades per class

# Gina
gina_swe_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
gina_calc_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
gina_engl_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
gina_grades = {
				'SWE' : average(gina_swe_grades),
			  	'CALC' : average(gina_calc_grades),
			  	'ENGL' : average(gina_engl_grades)
			  }

# Jay
jay_swe_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
jay_sci_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
jay_engl_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
jay_grades = {
				'SWE' : average(jay_swe_grades),
				'SCI' : average(jay_sci_grades),
				'ENGL' : average(jay_engl_grades)
			 }

# Mark
mark_swe_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
mark_bio_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
mark_chem_grades = {
				   'HW1' : random.randrange(50,100),
				   'HW2' : random.randrange(50,100),
				   'Test1' : random.randrange(50,100),
				   'Test2' : random.randrange(50,100)
				  }
mark_grades = {
				'SWE' : average(mark_swe_grades),
				'BIO' : average(mark_bio_grades),
				'CHEM' : average(mark_chem_grades)
			  }
			
# Student creation
gina = Student('Gina', gina_courses, gina_grades)
jay = Student('Jay', jay_courses, jay_grades)
mark = Student('Mark', mark_courses, mark_grades)

# List holding students 
stu = []
stu.append(gina)
stu.append(jay)
stu.append(mark)



# BEGINNING OF PROGRAM #

flag = True # Setting a flag to determine the lifespan of the program.

while flag:
	
	# Displaying all students
	print("Currently enrolled students: \n")
	for student in stu:
		student.show()

	# Prompting for action
	print("What action would you like to complete? [add, edit, or delete grades]")
	print("If you'd like to exit, type x ") # Exit point
	action = input()


	# Adding grades
	if action == 'add':
		print("Enter student name: ")
		stu_name = input()
		print("Enter course: ")
		course = input()
		print("Enter the homework / test title: ")
		title = input()
		print("Enter the number grade: ")
		grade = input()
		# Leaving point

	# Editing grades 
	elif action == 'edit':
		pass

	# Deleting grades 
	elif action == 'delete':
		pass

	# Exiting
	elif action == 'x':
		flag = False

