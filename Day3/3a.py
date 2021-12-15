import numpy as np

with open('binary.txt', 'r') as fin:
    binary = [list(line.strip()) for line in fin]

output = np.array(binary).astype(int)

output_count = np.count_nonzero(output == 1, axis=0)

gamma = [1 if val > 500 else 0 for val in output_count]
eps = [0 if val > 500 else 1 for val in output_count]

gamma_str = ''.join(str(val) for val in gamma)
eps_str = ''.join(str(val) for val in eps)

gamma_dec = int(gamma_str, 2)
eps_dec = int(eps_str, 2)

print(gamma_dec, eps_dec)

print(gamma_dec * eps_dec)