
#====================== Number Guessing Game Using Exceptional Handling =============================


import random

secret_number = random.randint(1, 10)

trials = 3

while trials > 0:
    try:
        guess = int(input("Guess the number (1-10): "))

        if guess == secret_number:
            print("Congratulations! You guessed correctly.")
            break

        else:
            trials -= 1
            print("Wrong guess!")
            print("Trials left:", trials)

            if trials == 0:
                raise Exception("No trials left. Game Over!")

    except ValueError:
        print("Please enter a valid number.")

    except Exception as e:
        print(e)
        break

    