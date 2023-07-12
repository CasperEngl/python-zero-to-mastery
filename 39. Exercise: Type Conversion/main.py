from datetime import datetime

name = input('What is your name? ')
birth_year = input('What year were you born? ')

age = datetime.now().year - int(birth_year)

print(f'Hello {name}! You are {age} years old.')
