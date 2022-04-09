"""make a while loop spell out letters"""

# a = "ifiok"
# item = 0

# while item < len(a):
#     print("letter", a[item])
#     item += 1

"""Add market items"""

def addorders():
    mktlst = []
    total_items = 7 #script will accept six items only

    while total_items > 1:
        orders = input("Enter an item name needed or enter stop to exit: ")
        if orders ==  'stop' or orders == 'STOP':
            break
        else:
            mktlst.append(orders)
            total_items -= 1
    print("These are items you need, thanks.")
    print(mktlst)
        
addorders()