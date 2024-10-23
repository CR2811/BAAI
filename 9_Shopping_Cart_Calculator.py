#
# Cherish
# Shopping Cart Calculator
#

# 1. Input
n = int(input('How many items do you want to buy?  ')) 
print ('')
total  = 0
subtotal = 0

# 2. Process
# Repeat the input amount spent
for i in range (n):
    item = input(f'Enter the name of item {i+1}: ')
    cost = int(input(f'Enter the price of {item}: '))
    m = int(input(f'Enter the quantity of {item}:'))
    subtotal = cost*m
    print(f'The total cost for {item}: {subtotal}')
    total = total + subtotal
    print('')

# 3. Output
print(f'The total cost of your shopping cart: {total}')