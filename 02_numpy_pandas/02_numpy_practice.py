import numpy as np

# Exercies 1 - NumPy refresh
results = np.array([
    [12, 15, 18],
    [10, 14, 20],
    [13, 17, 19],
    [11, 16, 21]
])

mean = results.mean()
row_mean = results.mean(axis=1)
col_mean = results.mean(axis=0)
mask = results > 16
values_above_16 = results[mask]

# print(f'mean of all values: {mean}')
# print(f'mean of each row: {row_mean}')
# print(f'mean of each column: {col_mean}')
# print(f'Boolean mask identifying values greater than 16: \n{mask}')
# print(f'values greater than 16: \n{values_above_16}')


# What does axis=0 remove?
# Removes the row axis, therefore calculating one value per column

# What does axis=1 remove?
# Removes the column axis, therefore calculating one value per row

# What is the difference between:
# second = results
# second = results.copy()
# second = results.copy() creates an independent copy of the array, so changes to second do not affect results,
# whereas second = results makes both names refer to the same array, so chnages made through either name affect the same underlying data



# Exercise 2 - Main exercise

# Columns: sample ID, replicate 1, replicate 2, replicate 3, temperature
experiment = np.array([
    [101, 48.2, 50.1, 49.5, 22.0],
    [102, 61.4, 59.8, 62.1, 22.5],
    [103, 45.7, 47.2, 46.8, 21.8],
    [104, 72.3, 70.9, 71.5, 23.1],
    [105, 55.6, 54.8, 56.2, 22.4],
    [106, 68.9, 67.5, 69.4, 22.9]
])

# 2.1 Shape, dtype and selection

# Print ndim, shape, size, and dtype.
print(f'ndim: {experiment.ndim}, shape: {experiment.shape}, size: {experiment.size}, dtype {experiment.dtype}')

# Select all sample IDs.
sample_ids = experiment[:,0]

# Select only the three replicate columns.
replicates = experiment[:,1:4]

# Select the temperature column.
temperature = experiment[:,-1]

# Select the row belonging to sample 104.
sample_id_is_104 = sample_ids == float(104)
sample_id_104_row = experiment[sample_id_is_104,:]

# Select the final three samples.
final_3_samples = experiment[-3:,:]

# Predict each output shape before printing it.
# Sample Ids shape: (6,)
# Replicate columns shape: (6, 3)
# Temperature column shape: (6,)
# Sample 104 row shape: (1, 5)
# Final three samples shape: (3, 5)


# 2.2 Aggregations
# Using only the replicate columns:

# Calculate the mean for each sample.
replicates_mean_per_sample = replicates.mean(axis=1)

# Calculate the mean for each replicate column.
replicates_mean_per_column = replicates.mean(axis=0)

# Calculate the minimum and maximum for each sample.
replicates_min_per_sample = replicates.min(axis=1)
replicates_max_per_sample = replicates.max(axis=1)

# Calculate the overall standard deviation.
replicates_stddev = replicates.std()

# Find the sample ID with the highest mean result.
sample_with_highest_mean = sample_ids[np.argmax(replicates_mean_per_sample)]


# 2.3 Boolean masks

# Create a mask identifying replicate measurements above 60.
mask_above_60 = replicates > 60

# Return all replicate measurements above 60.
values_above_60 = replicates[mask_above_60]

# Return the rows whose mean replicate result is above 60.
rows_with_means_above_60 = experiment[replicates_mean_per_sample > 60]

# Return the sample IDs whose temperature is above 22.5.
sample_ids_above_temperature = sample_ids[temperature > 22.5]

# Count how many individual replicate measurements are above 60.
count_replicates_above_60 = (replicates > 60).sum()


# 2.4 Reshaping and transposition

# Print the shape of the replicate data.
print(replicates.shape)

# Transpose it.
replicates_transpose = replicates.T

# Print the new shape.
print(replicates_transpose.shape)

# Flatten it into one dimension.
replicates_1d = replicates_transpose.flatten()

# Reshape the flattened data back to its original dimensions.
reshaped_replicates = replicates_1d.reshape(replicates_transpose.shape).T



# Exercise 3 - Broadcasting

replicates = experiment[:, 1:4]

offsets = np.array([1.0, -0.5, 2.0])

adjusted = replicates + offsets

sample_offsets = np.array([
    [0],
    [1],
    [2],
    [3],
    [4],
    [5]
])

replicates + sample_offsets

bad_offsets = np.array([1, 2])

# What are the shapes of replicates and offsets?
# replicates shape = (6, 3), offsets shape = (3,)

# Why can NumPy add them?
# Because their shapes are compatible, or the shape of offsets matches that of each row in replicates
# NumPy compares dimensions from right to left - the final dimensions both have size 3, so the offsets can be broadcast across all 6 rows

# Which offset will be applied to each column?
# 1.0 will be added to the replicate 1 column, -0.5 will be added to the replicate 2 column, and 2.0 will be added to the replicate 3 column

# What shape will adjusted have?
# adjusted.shape = (6, 3)

# Explain why replicates + sample_offsets adds one value to every replicate within a row.
# sample_offset.shape = (6, 1) therefore the value for each row of sample_offset will be added to the values in all columns of each row when applying replicates + sample_offsets
# since replcates has the same number of rows as sample_offsets

# Deliberately try an incompatible shape:
# bad_offsets = np.array([1, 2])
# Read the resulting traceback and write one sentence explaining why broadcasting failed
# bad_offsets cannot be broadcast together with replicates as these arrays have incompatible shapes: replicates has shape (6, 3), bad_offsets has shape (2,).
# The trailing dimensions are 3 and 2 - they are neither equal nor is either one 1, so the broadcasting fails



# Exercise 4 — Mini independent challenge
# Use the existing experiment array to create a new NumPy array with these five columns:
# sample ID, mean result, minimum result, maximum result, temperature

results = np.array([sample_ids, replicates_mean_per_sample, replicates_min_per_sample, replicates_max_per_sample, temperature]).T

sorted_results = results[results[:,1].argsort()]

print(sorted_results)

np.savetxt(
  'summary.csv', 
  sorted_results, 
  delimiter=',', 
  fmt=["%.0f", "%.2f", "%.2f", "%.2f", "%.2f"],
  header='sample_id,mean,min,max,temperature',
  comments=''
)