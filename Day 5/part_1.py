#!/usr/bin/env python

from map import Map

new_map = Map(1000, 1000)

with open('./data.txt', 'r') as file:
    for coordinate in file.readlines():
        coordinate = coordinate.replace('\n', '')

        new_map.place_line(coordinate, allow_diagonals=False)

print('\nPoints overlapping: ' + str(new_map.points_overlapping))

# print(new_map.display_map())
