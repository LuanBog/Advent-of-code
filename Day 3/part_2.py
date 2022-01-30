#!/usr/bin/env python

# Reads binaries from data.txt
binaries = []
with open('./data.txt', 'r') as file:
    for binary in file.readlines():
        binaries.append(binary.replace('\n', ''))

# Finds oxygen (oxygen_generator) and co (co2 scrubber) 
oxygen = binaries
co = binaries

def seperate_bits(binaries, index):
    result = {'0': [], '1': []}

    for binary in binaries:
        result[binary[index]].append(binary)

    return result

# For oxygen generator
while len(oxygen) > 1:
    for i in range(len(oxygen[0])):
        if len(oxygen) == 1:
            break

        binaries_separated = seperate_bits(oxygen, i)

        if len(binaries_separated['0']) > len(binaries_separated['1']):
            oxygen = binaries_separated['0']
        elif len(binaries_separated['0']) < len(binaries_separated['1']):
            oxygen = binaries_separated['1']
        else:
            oxygen = binaries_separated['1']

oxgeyn = oxygen[0]

# For co2 scrubber generator
while len(co) > 1:
    for i in range(len(co[0])):
        if len(co) == 1:
            break

        binaries_separated = seperate_bits(co, i)

        if len(binaries_separated['0']) > len(binaries_separated['1']):
            co = binaries_separated['1']
        elif len(binaries_separated['0']) < len(binaries_separated['1']):
            co = binaries_separated['0']
        else:
            co = binaries_separated['0']

# Calculates the life support rating
life_support_rating = int(oxygen[0], 2) * int(co[0], 2)

# Output
print(life_support_rating)
