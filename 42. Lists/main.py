my_list = [
    'apple',
    'banana',
    'orange',
    'pineapple',
    'grape',
]

print(my_list[0]) # apple

print(my_list[1]) # banana

# print all items and put "or" between the last two items
# e.g. apple, banana, orange, pineapple or grape
print(*my_list, sep=", ", end=" or " + my_list[-1])
