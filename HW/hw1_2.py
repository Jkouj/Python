#Joseph Koumjian
#due 1/31
#hw1_2.py

homework = float(input("Enter Homework grade: "))*0.45
midterm = float(input("Enter Midterm grade: "))*0.25
final_exam = float(input("Enter Final Exam grade: "))*0.3

final_grade = homework + midterm + final_exam

print("Your final grade is: ", round(final_grade,2))
