dictionary = {
    "a": 1,
    "b": 2,
}

print(dictionary) # {'a': 1, 'b': 2}
print(dictionary["a"]) # 1 (value)

dictionary["c"] = 3 # Add a new key-value pair

print(dictionary) # {'a': 1, 'b': 2, 'c': 3}

print(dictionary.get("c", 10)) # 3 (value)
print(dictionary.get("d", 10)) # 10 (default value)
