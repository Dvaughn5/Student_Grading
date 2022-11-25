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
				   'HW1' : 83,
				   'HW2' : 77,
				   'Test1' : 79,
				   'Test2' : 92,
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



# TRUE BEGINNING OF PROGRAM #

flag = True # Setting a flag to determine the lifespan of the program.

while flag:
	
	# Displaying all students
	print("\nCurrently enrolled students: \n")
	for student in stu:
		student.show()

	# Prompting for action
	print("\nWhat action would you like to complete? [add, edit, or delete grades]")
	print("If you'd like to exit, type x ") # Exit point prompt
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
		
		# GINA
		if stu_name == 'gina':
			if course == 'swe':
				gina_swe_grades[title] = grade
			elif course == 'calc':
				gina_calc_grades[title] = grade
			elif course == 'engl':
				gina_engl_grades[title] = grade


	# Editing grades 
	elif action == 'edit':
		print("Enter the name of the student you'd like to edit: ")
		stu_name = input()
		print("Enter the course for the desired edit: ")
		course = input()

		# GINA
		if stu_name == 'gina':

			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_swe_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				gina_swe_grades[asm_title] = new_grade # Updating grade


	# Deleting grades 
	elif action == 'delete':
		print("Enter the name of the student who's grade you'd like to delete: ")
		stu_name = input()
		print("Enter the course title of the grade you'd like to delete: ")
		course = input()

		# GINA
		if stu_name == 'gina':
			
			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_swe_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del gina_swe_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")
			
			# CALC
			elif course == 'calc':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_calc_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del gina_calc_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")
			
			# ENGL
			elif course == 'engl': 
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_engl_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del gina_engl_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")

	# Exiting program when prompted
	elif action == 'x':
		flag = False

