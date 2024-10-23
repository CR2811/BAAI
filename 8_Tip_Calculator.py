#
# Cherish
# Tip Calculator
#

# 1. Input
n = int(input('How many people are dining: ')) 
print('')
subtotal  = 0

# 2. Process
# Repeat the input amount spent
for i in range (n):
    amount = int(input(f'Enter the amount spent by person {i+1}: '))
    subtotal = subtotal + amount 
print('')
tip = int(input('Enter the tip percentage: '))
total = subtotal + subtotal*tip/100
print('')

# 3. Output
print(f'The total bill including the tip is: ${total}')