#
# Cherish
# BMI Calculator
#

while True:
    weight = int(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))
    BMI = weight/(height*height)
    print(f'Your BMI is {BMI}')
    
    temp = input('Do you want continue?(yes/no) ')
    if temp == 'no':
        break
