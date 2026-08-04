import numpy as np
import pandas as pd

experiment = np.array([
    [101, 48.2, 50.1, 49.5, 22.0],
    [102, 61.4, 59.8, 62.1, 22.5],
    [103, 45.7, 47.2, 46.8, 21.8],
    [104, 72.3, 70.9, 71.5, 23.1],
    [105, 55.6, 54.8, 56.2, 22.4],
    [106, 68.9, 67.5, 69.4, 22.9]
])

columns = [
    'sample_id',
    'replicate_1',
    'replicate_2',
    'replicate_3',
    'temperature'
]

experiment_df = pd.DataFrame(experiment, columns=columns)

# Select the sample_id column.
sample_id_column = experiment_df['sample_id']

# Select all three replicate columns.
replicate_df = experiment_df[['replicate_1', 'replicate_2', 'replicate_3']]

# Return samples with temperature above 22.5.
samples_above_temp = experiment_df.loc[experiment_df['temperature'] > 22.5, 'sample_id']

# Return samples where replicate_1 is above 60.
samples_above_60_rep1 = experiment_df.loc[experiment_df['replicate_1'] > 60, 'sample_id']

# Create a mean_result column.
experiment_df = experiment_df.assign(mean_result=replicate_df.mean(axis=1))

# Create minimum_result and maximum_result columns.
experiment_df = experiment_df.assign(minimum_result=replicate_df.min(axis=1), maximum_result=replicate_df.max(axis=1))

# Sort the DataFrame by mean_result.
sorted_result = experiment_df.sort_values('mean_result')

# Save it to a CSV without the DataFrame index.
sorted_result.to_csv('summary_df.csv', index=False) 

# Explain:
# the difference between a Series and DataFrame;
# the difference between .loc and .iloc;
# why pandas is useful for labelled tabular data.

# A series is a one-dimensional data structure, similar to a column or a list. 
# A dataframe is a two-dimensional data structure consisting of rows and columns

# .loc used for label-based selection
# .iloc used for position-based selection

# pandas associates values with meaningful row and column labels, allowing columns to be selected by name rather than numeric position.