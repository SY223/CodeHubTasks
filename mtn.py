"""A data plan subscription script"""
from mtnplans import monthly_plans

def dataPlans():
    print('Below are our list of data plans..')
    
    for i in monthly_plans:
        print('>',i)
    reply = int(input('Enter amount of data needed: '))
    if reply == 0:
        print('Transaction canceled..')
        
    elif reply == 1:
        print('Enter 1 to purchase or 2 to cancel: ')
        authenticate = int(input(f'Are you sure you want to buy {monthly_plans[1]} of data: '))
        if authenticate == 1:
            print(f'You have subscribed to {monthly_plans[1]} data..')
            print('Thank you..')
        else:
            print('You have successfully canceled the operation.')
    elif reply == 2:
        print('Enter 1 to purchase or 2 to cancel: ')
        authenticate = int(input(f'Are you sure you want to buy {monthly_plans[2]} of data: '))
        if authenticate == 1:
            print(f'You have subscribed to {monthly_plans[2]} data..')
            print('Thank you..')
        else:
            print('You have successfully canceled the operation.')
    elif reply == 3:
        print('Enter 1 to purchase or 2 to cancel: ')
        authenticate = int(input(f'Are you sure you want to buy {monthly_plans[3]} of data: '))
        if authenticate == 1:
            print(f'You have subscribed to {monthly_plans[3]} data..')
            print('Thank you..')
        else:
            print('You have successfully canceled the operation.')
    elif reply == 4:
        print('Enter 1 to purchase or 2 to cancel: ')
        authenticate = int(input(f'Are you sure you want to buy {monthly_plans[4]} of data: '))
        if authenticate == 1:
            print(f'You have subscribed to {monthly_plans[4]} data..')
            print('Thank you..')
        else:
            print('You have successfully canceled the operation.')
    else:
        print('Time out for not receiving an answer..')

dataPlans()


        

