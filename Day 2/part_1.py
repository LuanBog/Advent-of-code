#!/usr/bin/env python

commands = []

# Gets the command from data.txt
with open('./data.txt', 'r') as file:
    for current_number in file.readlines():
        commands.append(current_number)

# Parses the commands
position = {'x': 0, 'y': 0}

for command in commands:
    direction, amount = command.split()

    if direction == 'forward':
        position['x'] += int(amount)
    elif direction == 'up':
        position['y'] -= int(amount)
    elif direction == 'down':
        position['y'] += int(amount)

final_position = position['x'] * position['y']

# Output
print(final_position)