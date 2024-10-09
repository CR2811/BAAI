#
# Cherish
# repeat 3 times
#

max_lap = 3
curr_lap = 1

while (curr_lap <= max_lap):
    # 1. Input
    n1 = int(input('First number: ')) 
    n2 = int(input('Second number: '))

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
    curr_lap = curr_lap + 1