#
# Cherish
# Grade Calculator
#

# 1. Input
n = int(input('How many subject do you have: ')) 
sum  = 0
i = 0

# 2. Process
# Repeat the grade input
while (i < n):
    subject = input(f'Enter the name of subject {i+1}: ')
    grade = int(input(f'Enter the grade for {subject}: '))
    sum = sum + grade
    i = i+1
average = sum/n

# 3. Output
print(f'Your average grade is: {average}')