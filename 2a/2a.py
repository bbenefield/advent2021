import numpy as np

with open('directions.txt', 'r') as fin:
    directions = [line.strip().split(' ') for line in fin]

position = np.ndarray(shape=(1,2))
position[0][0] = 0
position[0][1] = 0
aim = 0

for direction in directions:
    if direction[0] == 'forward':
        position[0][0] += int(direction[1])
        position[0][1] += int(direction[1]) * aim
    elif direction[0] == 'down':
        aim += int(direction[1])
    elif direction[0] == 'up':
        aim -= int(direction[1])
    else:
        print('Do not know that direction')

print(position[0][0] * position[0][1])
