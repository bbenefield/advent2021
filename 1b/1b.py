from numpy.lib.stride_tricks import sliding_window_view

with open('depth_gauge.txt', 'r') as fin:
    depth = [int(line.strip()) for line in fin]

count = 0

depth_3w = sliding_window_view(depth, 3)

for idx, val in enumerate(depth_3w):
    if idx < len(depth_3w) - 1 and (sum(depth_3w[idx+1]) > sum(depth_3w[idx])):
        count += 1

print(count)
