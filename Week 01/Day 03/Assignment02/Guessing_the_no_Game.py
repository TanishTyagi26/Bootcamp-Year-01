#wap to ask the user to guess a no. . 
#give hints for wrong answers : if the no.by user is too high or low give hints how much far did he guessed the no.




def guess_no(number):
    if number!= 26 :
        if number>26:
            big= number-26
            print(f"Your answer is {big} digit bigger than the answer .")
        else :
            small = 26-number
            print(f"Your answer is {small} digit smaller than the answer .")
    else :
        print(f"hurray !!!")
        print(f"you guessed the correct answer : {number}")


number=int(input("enter positive integral value : "))
guess_no(number)