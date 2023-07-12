selfish = 'me me me'
        #  01234567

print(selfish[0]) # m

# [start:stop]
print(selfish[0:4]) # me m

# [start:stop:stepover]
print(selfish[0:8:2]) # m em

# [start:]
print(selfish[6:]) # me

# [:stop]
print(selfish[:5]) # me me

# [::stepover]
print(selfish[::1]) # me me me

# [-2]
print(selfish[-2]) # m
