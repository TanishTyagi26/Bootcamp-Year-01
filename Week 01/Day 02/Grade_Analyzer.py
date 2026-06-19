#=================  Grade Analyzer for students ====================
# accept : marks for maths , phys , chem ,eng , comp . sci.
# Calculations : Total , avg , Percentage .
# Grading System  : A for >=90 ,B for >=80 ,C for >= 70 ,D for >=60 ,F for < 60.
#extension : display Highest and lowest Marks .

print("welcome to the GRADE ANALYZER")
print("======================================================================")

print("Please enter marks for your subjects respectively : ")
print("======================================================================")
marks_list = []
maths_marks = float (input("enter your maths Marks : "))
phys_marks = float (input("enter your physics Marks : "))
chem_marks = float (input("enter your chemistry Marks : "))
eng_marks = float (input("enter your english Marks : "))
comp_sci_marks = float (input("enter your computer science Marks : "))
while True :

    marks_list.append(maths_marks)
    marks_list.append(phys_marks)
    marks_list.append(chem_marks)
    marks_list.append(eng_marks)
    marks_list.append(comp_sci_marks)


    print("1. Total Marks")
    print("2. Average")
    print("3. Percentage")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        total_marks = sum(marks_list)
        print(f"Total Marks are : {total_marks}")
        print("===================================")

    elif choice == 2:
        avg = total_marks/5
        print(f"Average of the Marks is : {avg}")
        print("===================================")

    elif choice == 3:
        percentage = (total_marks/500)*100
        print(f"Percentage of the Marks is : {percentage}")
        print("===================================")

    elif choice == 4:
        print(f"Exiting the program ....")
        print(f"THANK YOU for using  the SMART GRADE ANALYZER ....")
        print("===================================")
        break 

    else :
        print(f"Invalid Choice ")
        print("===================================")
