"""use the get method to output value of 'model' """

car = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964,
}

maker = car.get("model")
print(f"The model of my car is {maker}.")


"""Question 2 Answer: A given object may appear in a list more than once."""



"""Question 3: A dictionary that holds information of a twitter user profile"""
user_profile = {
    "name": "Sheriff Armani",
    "bio": "I'm here for the violence..",
    "location": "Colorado Springs,CO",
    "website": "",
    "birth-date": "January 29,1989.",
    "standard-account": True,
    "professional-account": False,
    "tips": False,
}

print(user_profile)