#!/usr/bin/env python

# Reads binaries from data.txt
binaries = []
with open('./data.txt', 'r') as file:
    for binary in file.readlines():
        binaries.append(binary.replace('\n', ''))        

# Gets gamma rate and epsilon rate
gamma_rate = ''
epsilon_rate = ''

def compare_bits(binaries, index):
    result = {'0': 0, '1': 0}

    for binary in binaries:
        result[binary[index]] += 1

    return result

for i in range(len(binaries[0])):
    result = compare_bits(binaries, i)
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)} # Sorts from greatest to least
    result = list(result) # Makes it a list, so it's easy to access

    gamma_rate += result[0]
    epsilon_rate += result[1]

# Converts binary to decimal then multiplies
power = int(gamma_rate, 2) * int(epsilon_rate, 2)

# Outputs
print(power)
