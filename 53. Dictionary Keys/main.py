dictionary = {
    123: [1, 2, 3],
    True: "hello",
    "a": 1,
}

# Dicts must have immutable keys (e.g. numbers, strings, tuples) 
# but can have mutable values (e.g. lists, dicts)

# So this is valid:
test_dictionary = {
    "a": [1, 2, 3],
    "b": {
        "c": 1,
        "d": 2,
    },
}

# But this is not:
# test_dictionary = {
#     ["a"]: 1,
#     ["b"]: 2,
# }
