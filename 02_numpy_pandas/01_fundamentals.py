import numpy as np

results = np.array([
    [12, 15, 18],
    [10, 14, 20],
    [13, 17, 19],
    [11, 16, 21]
])

mean_all = results.mean()
mean_rows = results.mean(axis=1)
mean_cols = results.mean(axis=0)
mask = results > 16

print(f'shape: {results.shape}')
print(f'2nd row: {results[1]}')
print(f'3rd column: {results[:,2]}')
print(f'mean of all values: {mean_all}')
print(f'mean of each row: {mean_rows}')
print(f'mean of each column: {mean_cols}')
print(f'Boolean mask identifying values greater than 16: \n{mask}')

