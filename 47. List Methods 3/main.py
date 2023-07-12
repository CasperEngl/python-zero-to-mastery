basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# Sort the list
basket.sort()
print(basket)

# Reverse the list
basket.reverse()
print(basket)

# Create a new sorted list
print(sorted(basket))

# Create a new reversed list 
print(list(reversed(basket)))
# Q: Why do I use list(reversed(basket)) instead of reversed(basket)?
# A: reversed(basket) returns a reverse iterator, not a list.
