#!/usr/bin/env python

increase_count = 0
prev_number = 0

# Gets the data from data.txt
with open('./data.txt', 'r') as file:
    # Increases increase_count if current_number is greater than prev_number
    for index, current_number in enumerate(file.readlines()):
        if index == 0:
            continue

        current_number = int(current_number)

        if current_number > prev_number:
            increase_count += 1

        prev_number = current_number

# Output
print(increase_count)
