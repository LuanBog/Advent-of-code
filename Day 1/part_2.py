#!/usr/bin/env python

data = []

# Gets the data from data.txt
with open('./data.txt', 'r') as file:
    for current_number in file.readlines():
        data.append(int(current_number))

# Makes a new dataset with by 3s of the elements and then they're summed
sums = []

e = len(data) - 2

for i in range(e):
    sums.append(sum(data[0:3]))
    del data[0]

# Increases increase_count if current_number is greater than prev_number
increase_count = 0
prev_number = 0

for index, current_number in enumerate(sums):
    current_number = int(current_number)
    
    if index == 0:
        prev_number = current_number
        continue

    if current_number > prev_number:
        increase_count += 1

    prev_number = current_number

# Output
print(increase_count)
