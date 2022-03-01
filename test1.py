'''Write a program that adds 1000 to a user input '''

aput = int(input('Enter a number below a thousand: '))

if aput < 1000:
    result = aput + 1000
    print('Your magic number is', result)
else:
    print('Your input is above a thousand')



# def magic_add(aput, bput=1000):    
#     if aput < 1000:
#         result = aput + bput
#         print('Your magic number is', result)
#     else:
#         print('Your input is above a thousand')

# aput = int(input('Enter a number below a thousand: '))
# magic_add(aput)