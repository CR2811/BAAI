#
# Cherish
# Tip Calculator
#

# 1. Input
n = int(input('How many people are dining: ')) 
sum  = 0

# 2. Process
# Repeat the input amount spent
for i in range (n):
    cost = int(input(f'Enter the amount spent by person {i+1}: '))
    sum = sum + cost
tip = int(input('Enter the tip percentage: '))
total = sum + sum*tip/100

# 3. Output
print(f'The total bill including the tip is: ${total}')