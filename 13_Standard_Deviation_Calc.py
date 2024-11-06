#
# Cherish
# Standard Deviation
#

import statistics 
import math

#define function
def my_sd(input):
    print(f'Input: {input}')
    length = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'Mean: {mean}')
    for x in input:
        sum += (int(x)- mean)**2
    sum = sum/length
    SD = math.sqrt(sum)
    return SD

# 1. Input
input =[1, 2, 3]

# 2. Process    
answer = round(my_sd([1,2,3]),2)

# 3. Output
print (f'The Standard Deviation is: {answer}')