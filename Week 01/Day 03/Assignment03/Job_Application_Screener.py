#wap for job interview screener using  nested (if -else- elif): :
#conditions : age must between 21-40,----------degre can be either b.tech or mca ,--------- cgpa >=7.0 if all these 3 conditions are fulfilled then print(INterview Shortlisted)////////////// otherwise give reason for rejection


def interview_screener(age,degree,cgpa):
    if age>=21:
        if age <=40:
            if degree.lower() == "b.tech"or "mca" :
                if cgpa >=7.0:
                    print(f"congratulations !You're Shortlisted for Interview ")
                else:
                    print("your cgpa is lower than expected")   
            else:
                print(f"your degree is {degree} , but only 'B.Tech' or 'MCA' is required for this job")
        else:
            print("sorry but you're older enough for this job")
    else:
        print("You're younger for this job")
while True :
    age= int(input("enter your age: "))
    cgpa=float(input("enter your cgpa : "))
    degree=str(input("enter your degree :"))
    interview_screener(age,degree,cgpa)
