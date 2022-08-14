import os
import numpy as np
import pandas as pd


students = []

def Home():
  begining = 0
  print('='*50)
  print('Student Information Management System in Computer Science Department.')
  print('>> 1. Add student information')
  print('>> 2. Delete student information')
  print('>> 3. Modify student information')
  print('>> 4. Show all student information')
  print('>> 5. save data')
  print('>> 6. Exit system')
  print('='*50)

  while not begining:
    begining = int(input('\nPlease choose an option from 1 - 6>> '))
    if begining<=0 or begining >6:
      print('invalid option... \nPlease choose option from 1 - 5. Press 6 to exit...')
      begining= 0
  return begining

  print('='*30)

def add_student():
    while 1:
        os.system("cls")
        student =[]
        print("\nEnter the following details: ")
        student_name = input("Please enter student name:")
        student_id = input("Please enter student ID:")
        student_sex = input("Please enter student gender (M - for male, F - female):")
        student_age = input("Please enter the age of the student:")
        student_ph = input('Please enter student phone number:\n')
        student_csc101_score = (input('Please enter CSC 101 score:\n'))
        student_csc102_score = (input('Please enter CSC 102 score:\n'))
        student_csc103_score = (input('Please enter CSC 103 score:\n'))
        student.append(student_name)
        student.append(student_id)
        student.append(student_sex)
        student.append(student_age)
        student.append(student_ph)
        student.append(student_csc101_score)
        student.append(student_csc102_score)
        student.append(student_csc103_score)
        students.append(student)

        print('Student infromation has been successful added!\n')

        n = input("Do you want to continue adding? y or n:\n".lower())
        if n =="n":
            break
          

def delete_student():
    while 1:
          delete_student_id = input("Please enter the student ID to be deleted:")
          for student in students:
            if student[1] == delete_student_id:
              del student
              print('Student record for ID number {} has been deleted'.format(delete_student_id))
              break
            else:
              print('Student record for ID number {} is not found'.format(delete_student_id))
          n = input("Do you want to continue deleting? y or n:")
          if n =="n":
            break

def update_student():
    while 1:
          update_student_id = input("Please enter the student ID you want to change:")
          for student in students:
            if student[1] == update_student_id:
                flag = input('Select the student information you want to change: \n>> 1. Name \n>> 2. Student ID \n>> 3. Gender \n>> 4. Age \n>> 5. phone \n>> 6. CSC 101 \n>> 7. CSC 102 \n>> 8. CSC 103:\n')
                if flag == 1:
                  name = input("Please enter the name you want to replace:")
                  student[0]= name
                elif flag == 2:
                  student_id =input("Please enter the student ID you want to change:")
                  student[1]= student_id
                elif flag == 3:
                  student_sex =input("Please enter the gender you want to change to:")
                  student[2]= student_sex
                elif flag == 4:
                  student_sex =input("Please enter the gender you want to change to:")
                  student[3]= student_age
                elif flag == 5:
                  student_age =input("Please enter the gender you want to change to:")
                  student[4]= student_ph
                elif flag == 6:
                  student_CSC101_score =input("Please enter the age you want to replace:")
                  student[5]= student_CSC101_score
                elif flag == 7:
                  student_CSC102_score =input("Please enter the phone you want to change to:")
                  student[6]= student_CSC102_score
                elif flag == 8:
                  student_CSC103_score =input("Please enter the gender you want to change to:")
                  student[7]= student_CSC103_score
            else:
               print("ID not found. Try again.") 
               return

          n =input("Do you want to continue updating? y or n:")
          if n =="n":
            break

def view_students():
    if students == ' ':
      print('the list is empty.')
    else:
      print("\nstudent information")
      print("Name, Student ID, Sex, Age, Phone Number, CSC 101, CSC 102, CSC103")
      for student in students:
        print(student[0]+" "+student[1]+" "+student[2]+" "+student[3]+" "+student[4]+" "+student[5]+" "+student[6]+" "+student[7]) 
        os.system("pause")

def save_file():
  while 1:
    with open('student_information_data.txt','w')as s:
      for student in students:
        print(student[0]+" "+student[1]+" "+student[2]+" "+student[3]+" "+student[4]+" "+student[5]+" "+student[6]+" "+student[7])
        s.write("\n".join(str(student)))
      print("Done")

def main():
  Option = Home()
  while Option:
    if Option == 1:
      add_student()
      Option = Home()
    elif Option == 2:
      delete_student()
      Option = Home()
    elif Option == 3:
      update_student()
      Option = Home()
    elif Option == 4:
      view_students()
      Option = Home()
    elif Option == 5:
      save_file()
      Option = Home()
    elif Option == 6:
      print('\n Thank you for your time!')
      return
    else:
      print("Please enter a valid number from 1-6")
      return 
if __name__ =='__main__': main()