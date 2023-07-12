basket = [1, 2, 3, 4, 5]

# Add a new item to the end of the list
basket.append(6)
print(basket)

# Remove the last item from the list
basket.pop()
print(basket)

# Remove the first item from the list
basket.pop(0)
print(basket)

# Insert an item at a specific position
basket.insert(0, 1)
print(basket)

# Remove a specific item from the list
basket.remove(1)
print(basket)

# Remove all items from the list
basket.clear()
print(basket)

# Add multiple items to the end of the list
basket.extend([1, 2, 3, 4, 5])
print(basket)
