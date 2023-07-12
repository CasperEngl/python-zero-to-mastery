# 55. Dictionary Methods 2
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user_2 = user.copy()

print('basket' in user.keys())

print('hello' in user.values())

print(user.items())

user.clear()

print(user)

print(user_2)

print(user_2.pop('age'))

print(user_2)

print(user_2.popitem())

print(user_2)

print(user_2.update({'age': 55}))

print(user_2)

print(user_2.update({'ages': 55}))

print(user_2)
