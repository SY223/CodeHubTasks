'''
Check if a drinker is above 18 years old. If drinker is below 18, display you cant drink
alcohol, if user is above 18 display cheers
'''
#user enter birth year
birth_year = int(input('Kindly enter your year of birth: '))
#user age is determined
decide = 2022 - birth_year
#condition ouputs user results
if decide < 18:
    print('Your age is', decide,',you do not qualify to be a drunkard.')
else:
    print('Cheers you are a qualified drunkard.')
