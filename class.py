# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage

# firstcar = Car('blue', 20000)
# secondcar = Car('red', 30000)
# print(f'The {firstcar.color} car can thread {firstcar.mileage:,} miles.')
# print(f'But the {secondcar.color} car can thread {secondcar.mileage:,} miles.')


class Citizen:
    def __init__(self, full_name,age, sor, bvn, phone_number):
        self.full_name = full_name
        self.age = age
        self.sor = sor
        self.bvn = bvn
        self.phone_number = phone_number
    
    def get_user(self):
        userinfo = self.full_name + str(self.age) + self.sor + str(self.bvn) + self.phone_number
        return userinfo.title()

userone = Citizen("Kunle babs",27,"Ondo",212512765,"0803-543-8876")
print("User details below..")
print(userone.get_user())
#print(f"Full Name -> {userone.full_name.title()}\nAge -> {userone.age}\nOrigin -> {userone.sor} State\nBVN Number -> {userone.bvn}\nPhone Number -> {userone.phone_number}")