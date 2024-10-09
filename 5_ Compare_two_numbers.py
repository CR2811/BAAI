#
# Cherish
# Compare two numbers and print which the bigger one

# 1. Input
n1 = int(input('First number: ')) 
n2 = int(input('Second Number '))

# 2. Process
# Compare 2 numbers
if (n1 < n2):
    big = f"The bigger number is {n2}"
elif (n1 > n2):
    big = f"The bigger number is {n1}"
else:
    big = f"Both are same numbers"

# 3. Output
print(big)