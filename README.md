# Student_Grading
This application has the resources to add, edit, and delete student grades onto a storage medium.
- Program functionality is prodominately acheived through conditional statements. 
- At each step through the program, various checks and exceptions are handled to verify that only valid information is being entered.

## Python Program
### Libraries:
- Random: Used to intialize a random value for the homework, and tests initialized in each student's 'Grades' dictionary.

### Classes, Methods, and Functions:
Student class:
- Contructed with a name, the courses they're taking, and their grades for each class.
  + Name = string
  + Courses = list
  + Grades = Dictionary
- Show():
  + This method is used to display information about the students at runtime.
  + Displays the student's name, the courses they're taking, and their grade for each class. 

Average Function:
- Accepts a dictionary as a paramter, that dictionary being the same 'grades' dictionary being passed to the Student class upon construction.
- This function loops through the dictionary using the .items() method to add all values (grades) and divide by the length of the dictionary to compute an average.

### Program Flow
- The program's lifetime is based on a flag, by default set to 'True'. When prompted, the user can type 'x' and hit 'enter' on the keyboayd, and the flag will be set to 'False'
- Besides explicitly calling for an exit point, exception handling creates additional exit points. 
  + If the user enters an invalid grade the program will close, and the grade will not be added to the text document. 
+ If the user enters all valid information, the respective data will be written to a text document called 'grades.txt'
