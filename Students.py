
# Students overall grades 
Dorian = {'SoftwareEngineering' : 92,
					'Calculus' : 89,
					'ReportWriting' : 95,
					'Java' : 86,
					'Algebra' : 77}

Kyra = {'SoftwareEngineering' : 98,
					'Calculus' : 92,
					'ReportWriting' : 86,
					'Java' : 89,
					'Algebra' : 83}

Saleh = {
		 1 : {'HW1': 92},
		 'SWE': {'HW3': 89},
		 'Calc': {'HW1': 97},
		 'English': {'HW4': 77},
		 'Algebra': {'HW7':81},
		 'PSY' : [27,86,42,32]
		}

kyra_SWE_grades = {
					'HW1':87,
					'Test2':89,
					'HW2': 94
					}

def average(dictionary):
	avg = 0
	for key, val in dictionary.items():
		avg += int(val)
	avg /= len(dictionary)
	print(avg)

courses = ['SWE', 'Calc', 'English', 'Algebra']
#print(Saleh['PSY'])

#for course in courses:
#	if course in Saleh:
#		print(course)

print('Enter the HW Title')
hw = input()

print('Enter the grade')
grade = input()

kyra_SWE_grades[hw] = grade

for key, val in kyra_SWE_grades.items():
	print(f"Homework: {key}")
	print(f"Grade: {val}")

average(kyra_SWE_grades)
