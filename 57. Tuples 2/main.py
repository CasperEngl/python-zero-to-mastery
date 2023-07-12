# 57. Tuples 2

my_tuple = (1, 2, 3, 4, 5, 5)

x = my_tuple[0]
y = my_tuple[1]

x, y, z, *other = my_tuple

print(x, y, z, other)

print(my_tuple.count(5))

print(my_tuple.index(5))

print(len(my_tuple))
