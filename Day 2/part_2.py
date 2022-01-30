#!/usr/bin/env python

commands = []

# Gets the command from data.txt
with open('./data.txt', 'r') as file:
    for current_number in file.readlines():
        commands.append(current_number)

# Parses the commands
position = {'x': 0, 'y': 0, 'aim': 0}

for command in commands:
    direction, amount = command.split()

    if direction == 'forward':
        position['x'] += int(amount)
        position['y'] += int(amount) * position['aim']
    elif direction == 'up':
        position['aim'] -= int(amount)
    elif direction == 'down':
        position['aim'] += int(amount)

final_position = position['x'] * position['y']

# Output
print(final_position)