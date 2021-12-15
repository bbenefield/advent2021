with open('1a\\depth_gauge.txt', 'r') as fin:
    depth = [int(line.strip()) for line in fin]

count = 0

for idx, value in enumerate(depth):
    if idx < len(depth) - 1 and depth[idx+1] > depth[idx]:
        count += 1

print(count)