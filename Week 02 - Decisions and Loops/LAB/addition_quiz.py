"""
Addition quiz

Step 1: Generate two single-dgit integers for number 1 (e.g., 4) and number 2 (e.g., 5)
Step 2: Prompt the student to answer, "what is 4 + 5?" (use input)
Step 3: Check wether the student's answer is correct.
"""

num1 = 4
num2 = 5

answer = int(input(f"What is {num1} + {num2}?"))

if answer == num1 + num2:
     print("Correct!")
else:
    print(f"Incorrect. Try again!")


while True:
    num1 = 4
    num2 = 5

    answer = int(input(f"What is {num1} + {num2}?"))

    if answer == num1 + num2:

        print("Correct!")
        break
    else:
        print(f"Incorrect. Try again!")



import random

while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Incorrect. Try again!")




