#
# Cherish
# Try Function 2
#

#define function
def my_add(input):
    sum =0
    for x in input:
        sum+=int(x)
    return sum

# 1. Input
input =[10, 20, 30]

# 2. Process
answer = my_add(input)

# 3. Ouput
print(f'Answer: {answer}')

# 4. Short way to call function
print(f'Answer{my_add([1, 2, 3])}')