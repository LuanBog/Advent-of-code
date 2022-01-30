# Format: [(x1, y1), (x2, y2)]
def get_points_in_between(parsed_coordinate):
    points_in_between = []

    x1, y1 = parsed_coordinate[0]
    x2, y2 = parsed_coordinate[1]

    order_reversed = False

    if x1 == x2 and y1 == y2:
        return []
    elif x2 > x1 or y2 > y1:
        current_point = [x1, y1]
    else:
        current_point = [x2, y2]

        x_temp = x1
        x1 = x2
        x2 = x_temp

        y_temp = y1
        y1 = y2
        y2 = y_temp

        order_reversed = True

    while current_point[0] != x2 - 1 and current_point[1] != y2 - 1:
        if current_point[0] < x2:
            current_point[0] += 1
        elif current_point[0] > x2:
            current_point[0] -= 1
            
        if current_point[1] < y2:
            current_point[1] += 1
        elif current_point[1] > y2:
            current_point[1] -= 1

        points_in_between.append(tuple(current_point.copy()))

    if order_reversed:
        points_in_between = list(reversed(points_in_between))

    return points_in_between

def parse_coordinate(coordinate):
    separated = coordinate.split('->')
    x1, y1 = separated[0].split(',')
    x1 = int(x1)
    y1 = int(y1)

    x2, y2 = separated[1].split(',')
    x2 = int(x2)
    y2 = int(y2)

    return [(x1, y1), (x2, y2)]

def is_horizontal_vertical(parsed_coordinate):
    x1, y1 = parsed_coordinate[0]
    x2, y2 = parsed_coordinate[1]

    return x1 == x2 or y1 == y2

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(width)] for y in range(height)]

        self.points_overlapping = 0

    def place_line(self, line, allow_diagonals=False):
        parsed = parse_coordinate(line)
        
        if is_horizontal_vertical(parsed) or not allow_diagonals:
            print('Placing in the map "{}"'.format(line))
        else:
            print('Cannot place "{}", because it is not horizontol nor vertical'.format(line))
            return

        points_inbetween = get_points_in_between(parsed)

        self.plot_point(parsed[0][0], parsed[0][1])
        self.plot_point(parsed[1][0], parsed[1][1])

        for point in points_inbetween:
            self.plot_point(point[0], point[1])

    def plot_point(self, x, y):
        if self.map[y][x] + 1 == 2:
            self.points_overlapping += 1

        self.map[y][x] += 1

    # For fun
    def display_map(self):
        for y in self.map:
            print(y)
