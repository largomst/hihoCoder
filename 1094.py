# python2

n, k = raw_input().strip().split(' ')
n, k = int(n), int(k)
city_map = []
local_map = []
for n0 in range(n):
    city_map.append(raw_input().strip())
for n0 in range(3):
    local_map.append(raw_input().strip())

value = {'.': 1, 'H': 3, 'S': 5, 'P': 7, 'S': 9, 'G': 11, 'M': 13, 'T': 15}
value_map = [[0] * n for i in range(len(city_map[0]))]
for row in range(len(city_map)):
    for col in range(len(city_map[0])):
        value_map[row][col] = value[city_map[row][col]]

count_map = [[0] * len(city_map[0]) for i in range(n)]

directions = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, -1),
              (0, 1)]

for row in range(1, len(city_map) - 1):
    for col in range(1, len(city_map[0]) - 1):
        for direction in directions:
            count_map[row][col] += value_map[row + direction[0]][col +
                                                                 direction[1]]

goal_value = 0

for direction in directions:
    goal_value += value[local_map[1 + direction[0]][1 + direction[1]]]

for row in range(1, len(city_map) - 1):
    for col in range(1, len(city_map[0]) - 1):
        if goal_value == count_map[row][col]:
            print('%d %d' % (row + 1, col + 1))
            break
