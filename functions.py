"""function to Convert Celsius to Fahrenheit"""

# a = float(input("Enter a temperature value: "))

# def cels_to_fahr(celsus):
#     bresult = (celsus * 1.8) + 32
#     return bresult

# fahr = cels_to_fahr(a)
# print(f"Your Celsius {a:.2f} is equivalent to {fahr:.2f} degrees Fahrenheit.")


"""Append User Input to List"""

# def four_loop():
#     list1 = []
#     for i in range(1,5):
#         item = input("Enter a word: ")
#         list1.append(item)
#     print(list1)

# four_loop()

"""Populate market items"""

def my_goods():
    goods = [] 
    for marketgoods in range(1,7):
        marketgoods = input('Enter your market items or enter stop to exit: ')
        if marketgoods.lower() == 'stop':
            break
        else:
            goods.append(marketgoods)

    print("These are items you need, thanks.")    
    print(goods)

my_goods()
