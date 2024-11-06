#
# Cherish
# Interest Calculator
#

# Define Function
def calculate_interest(principal, rate, time):
    interest = (principal*rate*time)/100
    return interest

# 1. Input

# 2. Process
y = calculate_interest(1000, 5, 2)

# 3. Output
print(f'The interest is {y}')