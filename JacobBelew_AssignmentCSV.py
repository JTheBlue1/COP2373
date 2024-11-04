##An instructor teaches a class in which each student takes three exams. The instructor would
## like to store this information in a file named grades.csv for later use. Create a program that
## allows an instructor to input how many students they want to enter.
## Then enter each student’s first name and last name as strings and the student’s three exam
## grades as integers. Use the csv module to write each record into the grades.csv file and
## have a header of First Name, Last Name, Exam 1, Exam 2 and Exam3. Each student should be
## a record in the grades.csv file.
##Once the file is created, create a separate program to read the grades.csv file and display
# the data in tabular format. Implement the with keyword. You may need to refer back to
# Chapter 5 for formatting.

import csv

#Function that stores the student's grades onto a CSV file
def store_student_grades():

    #Gather amount of students
    num_students = int(input('Enter total amount of students. '))

    #Assign a name to the file
    f_name = 'studentgrades.csv'

    #Open the CSV file in writing mode
    with open(f_name, mode='w', newline='') as file:
        write = csv.writer(file)

        #Create header
        write.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        #Gather and write each students information
        for _ in range(num_students):
            first_name = input("Enter the first name of the student.")
            last_name = input("Enter the last name of the student.")
            ex1 = int(input("Enter the score of Exam 1."))
            ex2 = int(input("Enter the score of Exam 2."))
            ex3 = int(input("Enter the score of Exam 3."))
            write.writerow([first_name, last_name, ex1, ex2, ex3])

    print(f'\nInformation has been inputted to {f_name}')

#Run function
if __name__ == '__main__':
        store_student_grades()

#Function that obtains the students' information from the CSV file then displays the information
def read_grades():

    f_name = 'studentgrades.csv'

    #Read CSV file
    with open(f_name, mode='r') as file:
        read = csv.reader(file)
        header = next(read)

        #Display header
        print(f"\n{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")

        #Display each of the student's grades in rows
        for row in read:
            print(f"\n{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")

#Run function
if __name__ == '__main__':
    read_grades()


