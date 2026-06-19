#=================  Library Fine Calculator ====================
# input : students name ,days late
# Fine rules: 1-5 days -> 5 rupees/day, 6-10 days -> 10 rupees/day, >10 days -> 20 rupees/day
# Display : individual fine, total fine, highest fine, avg fine

# def lib_fine(students_name, fine_days):
#     fine = 0
#     total_fine = []

#     for k in range(len(students_name)):

#         i = students_name[k]
#         j = fine_days[k]

#         if 1 <= j <= 5:
#             fine = j * 5
#             total_fine.append(fine)

#         elif 6 <= j <= 10:
#             fine = j * 10
#             total_fine.append(fine)

#         elif j > 10:
#             fine = j * 20
#             total_fine.append(fine)

#         else:
#             fine = 0
#             total_fine.append(fine)

#         print(f"Hello ! {i} Your Total Fine days are : {j}")
#         print(f"Individual Fine : {fine}")

#     highest_fine = max(total_fine)
#     average_fine = sum(total_fine) / len(total_fine)
#     total_fine = sum(total_fine)

#     print("\n",end="=====================================================================\n\n")

#     print(f"Total Fine : {total_fine}")
#     print(f"Average Fine : {average_fine}")
#     print(f"Highest Fine : {highest_fine}")
#     print(f"THANK YOU ! .....")

# student_list = []
# fine_list = []

# students_size = int(input("enter total no. students to enter the data : "))

# for i in range(students_size):
#     students_name = str(input("enter your Name : "))
#     student_list.append(students_name)

#     fine_days = int(input("enter the no. days delayed  : "))
#     fine_list.append(fine_days)

# lib_fine(student_list, fine_list)






#==========================LAMBDA FUNCTIONS =================================

