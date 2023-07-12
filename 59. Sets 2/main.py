# 59. Sets 2

initial_my_set = {1, 2, 3, 4, 5}
initial_your_set = {4, 5, 6, 7, 8, 9, 10}

my_set = initial_my_set.copy()
your_set = initial_your_set.copy()

print(my_set.difference(your_set))  # {1, 2, 3}

print(my_set.discard(5))  # None

print(my_set)  # {1, 2, 3, 4}

my_set = initial_my_set.copy()

print(my_set.difference(your_set))  # {1, 2, 3}

print(my_set.difference_update(your_set))  # None

print(my_set)  # {1, 2, 3}

my_set = initial_my_set.copy()

print(my_set.intersection(your_set))  # {4, 5}
print(my_set & your_set)  # {4, 5} (same as above)

print(my_set.isdisjoint(your_set))  # False

my_set = initial_my_set.copy()

print(my_set.union(your_set))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set | your_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (same as above)

my_set = {4, 5} # matching subset
your_set = initial_your_set.copy()

print(my_set.issubset(your_set))  # True

print(my_set.issuperset(your_set))  # False
