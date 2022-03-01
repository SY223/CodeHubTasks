"""Basic arithmetic calculations with python"""
#Take inputs
num_1 = float(input('Enter a number: '))
num_2 = float(input('Enter second number: '))

#Decide operator to process activity
activity = input('Enter your desired operator +,-,/,*: ')

#Conditions to process activity
#Add two numbers
if activity == '+':
    print('Addition results to',num_1 + num_2)
#Subtract two numbers 
elif activity == '-':
    print('Subtraction results to',num_1 - num_2)
#Divide two numbers
elif activity == '/':
    if num_2 == 0:
        print('Denominator cannot be zero.')
    else:
        print('Division results to',num_1 / num_2)
#multiply two numbers
elif activity == '*':
    print('multiplication results to',num_1 * num_2)
else:
    print('invalid')


"""Using the function pattern"""

# def add(num_1, num_2):
#     return num_1 + num_2

# def sub(num_1, num_2):
#     return num_1 - num_2

# def divide(num_1, num_2):
#     return num_1 / num_2

# def mult(num_1, num_2):
#     return num_1 * num_2

# num_1 = float(input('Enter a number: '))
# num_2 = float(input('Enter a number: '))
# activity = input('Enter your desired operator +,-,/,*: ')

# if activity == '+':
#     print(num_1, 'and', num_2, 'produces',add(num_1, num_2))

# elif activity == '-':
#     print(num_1, 'and', num_2, 'produces',sub(num_1, num_2))

# elif activity == '/':
#     if num_2 == 0:
#         print('Denominator cannot be zero.')
#     else:
#         print(num_1, 'and', num_2, 'produces',divide(num_1, num_2))

# elif activity == '*':
#     print(num_1, 'and', num_2, 'produces',mult(num_1, num_2))

# else:
#     print('invalid')








