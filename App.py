# This app needs to meet certain requirments:
	# Add, edit, and delete grades onto a storage medium
	# Subprograms with parameter passing
	# Abstract data types
	# Encapsulation
	# Exception handling
	# Verify valid scores
	# Documentation

# Importing necessary modules
import random


# Student Class
class Student():
	
	# Initializing the student
	def __init__(self, name, courses, grades):
		self.name = name
		self.courses = courses
		self.grades = grades

	# Method to display information about the student
	def show(self):
		print(f"Student Name: {self.name}")
		print(f"Courses: {self.courses}")
		print(f"Grades: {self.grades}\n")

# Function to calculate grade average
def average(dictionary):
	
	# Calculating percentage average
	avg = 0
	for key, val in dictionary.items():
		avg += int(val)
	avg /= len(dictionary)
	
	# Determining letter grade 
	if avg >= 90 and avg <= 100:
		letter_grade = 'A'
	elif avg >= 80 and avg < 90:
		letter_grade = 'B'
	elif avg >= 70 and avg < 80:
		letter_grade = 'C'
	elif avg >= 60 and avg < 70:
		letter_grade = 'D'
	elif avg < 60:
		letter_grade = 'F'

	# Returning the average, and letter grade
	return avg, letter_grade
		

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
	action = input().lower()


	# Adding grades
	if action == 'add':
		print("Enter student name: ") # Student nsme
		stu_name = input().lower()
		print("Enter course: ") # Course title
		course = input().lower()
		print("Enter the homework / test title [In the format, 'hw#' / 'test#': ") # Homework / test title
		title = input()


		print("Enter the number grade: [Must be a whole number]") # Number Grade

		# Exception handling and score verification
		try: # Score must be valid to continue
			grade = int(input())
			if grade >= 0 and grade <= 100: 
				pass
			else: # Stopping the program if the number is less than 0 or greater than 100
				print("\nThe grade needs to be a number between 0 and 100.") 
				print("Restart and enter a valid response.")
				break 
		except ValueError: # Catching ValueError if the user enters any value besides a float
			print("Value must be of type int, or in other words a whole number.") 
			break
		
		# GINA
		if stu_name == 'gina':
			
			# SWE
			if course == 'swe':
				gina_swe_grades[title] = grade
				
				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina SWE grades: {gina_swe_grades}\n")

			# CALC
			elif course == 'calc':
				gina_calc_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina CALC grades: {gina_calc_grades}\n")

			# ENGL
			elif course == 'engl':
				gina_engl_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina ENGL grades: {gina_engl_grades}\n")

		# JAY
		if stu_name == 'jay':
			
			if course =='swe':
				jay_swe_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay SWE grades: {jay_swe_grades}\n")

			elif course == 'sci':
				jay_sci_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay SCI grades: {jay_sci_grades}\n")

			elif course == 'engl':
				jay_engl_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay ENGL grades: {jay_engl_grades}\n")

		# MARK
		if stu_name == 'mark':
			if course == 'swe':
				mark_swe_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark SWE grades: {mark_swe_grades}\n")

			elif course == 'bio':
				mark_bio_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark BIO grades: {mark_bio_grades}\n")

			elif course == 'chem':
				mark_chem_grades[title] = grade

				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark CHEM grades: {mark_chem_grades}\n")


	# Editing grades 
	elif action == 'edit':
		print("Enter the name of the student you'd like to edit: ")
		stu_name = input().lower()
		print("Enter the course for the desired edit: ")
		course = input().lower()

		# GINA
		if stu_name == 'gina':

			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_swe_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				gina_swe_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina's updated SWE grades: {gina_swe_grades}\n")

				print("\nThe grade has been successfully updated.\n")

			# CALC
			elif course == 'calc':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_calc_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				gina_calc_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina's updated CALC grades: {gina_calc_grades}\n")

				print("\nThe grade has been successfully updated.\n")

			# ENGL
			elif course == 'engl':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_engl_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				gina_engl_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina's updated ENGL grades: {gina_engl_grades}\n")

				print("\nThe grade has been successfully updated.\n")

		# JAY
		if stu_name == 'jay':

			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_swe_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				jay_swe_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay's updated SWE grades: {jay_swe_grades}\n")

				print("\nThe grade has been successfully updated.\n")

			# SCI
			elif course == 'sci':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_sci_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				jay_sci_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay's updated SCI grades: {jay_sci_grades}\n")

				print("\nThe grade has been successfully updated.\n")

			# ENGL
			elif course == 'engl':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_engl_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				jay_engl_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay's updated ENGL grades: {jay_engl_grades}\n")

				print("\nThe grade has been successfully updated.\n")

		# MARK
		if stu_name == 'mark':

			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_swe_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()

				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				mark_swe_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark's updated SWE grades: {mark_swe_grades}\n")

				print("\nThe grade has been successfully updated.\n")

			# BIO
			elif course == 'bio':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_bio_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				mark_bio_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark's updated BIO grades: {mark_bio_grades}\n")

				print("\nThe grade has been successfully updated.\n")

			# CHEM
			elif course == 'chem':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_chem_grades}")

				print("Enter the homework / test you'd like to alter: [case for case, no spaces]")
				asm_title = input()
				
				print("Enter the new grade: [Must be a whole number]")

				# Exception handling and score verification
				try: # Score must be valid to continue
					new_grade = int(input())
					if new_grade >= 0 and new_grade <= 100: 
						pass
					else: # Stopping the program if the number is less than 0 or greater than 100
						print("\nThe grade needs to be a number between 0 and 100.") 
						print("Restart and enter a valid response.")
						break 
				except ValueError: # Catching ValueError if the user enters any value besides a float
					print("Value must be of type int, or in other words a whole number.") 
					break

				mark_chem_grades[asm_title] = new_grade # Updating grade

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark's updated CHEM grades: {mark_chem_grades}\n")

				print("\nThe grade has been successfully updated.\n")


	# Deleting grades 
	elif action == 'delete':
		print("Enter the name of the student who's grade you'd like to delete: ")
		stu_name = input().lower()
		print("Enter the course title of the grade you'd like to delete: ")
		course = input().lower()

		# GINA
		if stu_name == 'gina':
			
			# SWE
			if course == 'swe':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_swe_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del gina_swe_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina's SWE grades post deletion: {gina_swe_grades}\n")

				print("\nThe grade has been successfully updated.\n")
			
			# CALC
			elif course == 'calc':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_calc_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del gina_calc_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina's CALC grades post deletion: {gina_calc_grades}\n")

				print("\nThe grade has been successfully updated.\n")
			
			# ENGL
			elif course == 'engl': 
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{gina_engl_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del gina_engl_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Gina's ENGL grades post deletion: {gina_engl_grades}\n")

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

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay's SWE grades post deletion: {jay_swe_grades}\n")

				print("\nThe grade has been successfully updated.\n")
			
			# SCI
			elif course == 'sci':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_sci_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del jay_sci_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay's SCI grades post deletion: {jay_sci_grades}\n")

				print("\nThe grade has been successfully updated.\n")
			
			# ENGL
			elif course == 'engl': 
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{jay_engl_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del jay_engl_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Jay's ENGL grades post deletion: {jay_engl_grades}\n")

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

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark's SWE grades post deletion: {mark_swe_grades}\n")

				print("\nThe grade has been successfully updated.\n")
			
			# BIO
			elif course == 'bio':
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_bio_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del mark_bio_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark's BIO grades post deletion: {mark_bio_grades}\n")

				print("\nThe grade has been successfully updated.\n")
			
			# CHEM
			elif course == 'chem': 
				print(f"\nHere are the grades available for {stu_name} in {course}: \n")
				print(f"{mark_chem_grades}")

				print("\nEnter the homework / test you'd like to delete: [case for case, no spaces]")
				asm_title = input()

				del mark_chem_grades[asm_title]

				# Writing the grades to the text file.
				with open("grades.txt", 'a', encoding = "utf-8") as f:
					f.write(f"Mark's CHEM grades post deletion: {mark_chem_grades}\n")

				print("\nThe grade has been successfully updated.\n")


	# Exiting program when prompted
	elif action == 'x':
		flag = False