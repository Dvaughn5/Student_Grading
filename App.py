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
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
gina_calc_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
gina_engl_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
gina_grades = {
				'SWE' : average(gina_swe_grades),
			  	'CALC' : average(gina_calc_grades),
			  	'ENGL' : average(gina_engl_grades)
			  }

# Jay
jay_swe_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
jay_sci_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
jay_engl_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
jay_grades = {
				'SWE' : average(jay_swe_grades),
				'SCI' : average(jay_sci_grades),
				'ENGL' : average(jay_engl_grades)
			 }

# Mark
mark_swe_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
mark_bio_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
				  }
mark_chem_grades = {
				   'hw1' : random.randrange(50,100),
				   'hw2' : random.randrange(50,100),
				   'test1' : random.randrange(50,100),
				   'test2' : random.randrange(50,100)
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

		# JAY
		if stu_name == 'jay':
			if course =='swe':
				jay_swe_grades[title] = grade
			elif course == 'sci':
				jay_sci_grades[title] = grade
			elif course == 'engl':
				jay_engl_grades[title] = grade

		# MARK
		if stu_name == 'mark':
			if course == 'swe':
				mark_swe_grades[title] = grade
			elif course == 'bio':
				mark_bio_grades[title] = grade
			elif course == 'chem':
				mark_chem_grades[title] = grade


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

				print("\nThe grade has been successfully updated.\n")

			# CALC
			elif course == 'calc':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_calc_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				gina_calc_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

			# ENGL
			elif course == 'engl':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_engl_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				gina_engl_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

		# JAY
		if stu_name == 'jay':

			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_swe_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				jay_swe_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

			# SCI
			elif course == 'sci':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_sci_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				jay_sci_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

			# ENGL
			elif course == 'engl':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_engl_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				jay_engl_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

		# MARK
		if stu_name == 'mark':

			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_swe_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				mark_swe_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

			# BIO
			elif course == 'bio':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_bio_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				mark_bio_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")

			# CHEM
			elif course == 'chem':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_chem_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				print("Enter the new grade: ")
				new_grade = input()

				mark_chem_grades[asm_title] = new_grade # Updating grade

				print("\nThe grade has been successfully updated.\n")


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

		# JAY
		if stu_name == 'jay':
			
			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_swe_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del jay_swe_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")
			
			# SCI
			elif course == 'sci':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_sci_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del jay_sci_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")
			
			# ENGL
			elif course == 'engl': 
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_engl_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del jay_engl_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")

		# MARK
		if stu_name == 'mark':
			
			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_swe_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del jay_swe_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")
			
			# BIO
			elif course == 'bio':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_bio_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del mark_bio_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")
			
			# CHEM
			elif course == 'chem': 
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_chem_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del mark_chem_grades[asm_title]

				print("\nThe grade has been successfully updated.\n")


	# Exiting program when prompted
	elif action == 'x':
		flag = False