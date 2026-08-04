import pandas as pd

df = pd.read_csv('data/experiment_results.csv')

# Part A — Load and inspect the data

# The first five rows.
first_five_rows = df.head(5)

# The DataFrame shape.
# df.shape = (11, 5)

# The column names.
columns = df.columns

# The dtype of every column.
# print(df.dtypes) :
# sample_id          int64
# treatment            str
# measurement_1    float64
# measurement_2    float64
# temperature      float64

# The output from .info().
# print(df.info()):
# <class 'pandas.DataFrame'>
# RangeIndex: 11 entries, 0 to 10
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   sample_id      11 non-null     int64  
#  1   treatment      11 non-null     str    
#  2   measurement_1  11 non-null     float64
#  3   measurement_2  9 non-null      float64
#  4   temperature    10 non-null     float64
# dtypes: float64(3), int64(1), str(1)
# memory usage: 572.0 bytes
# None

# A Series containing the number of missing values in each column.
missing_values_per_column = df.isna().sum()

# A single integer containing the number of exactly duplicated rows.
number_duplicates = df.duplicated().sum()


# Part B — Clean the data

# Remove exact duplicate rows.
clean_df = df.copy().drop_duplicates()

# Fill the missing temperature value with the median of the non-missing temperature values.
median_temperature = clean_df['temperature'].median()
clean_df['temperature'] = clean_df['temperature'].fillna(median_temperature)

# Remove every complete row where either measurement_1 or measurement_2 is missing.
clean_df = clean_df.dropna(subset=['measurement_1', 'measurement_2'])


# Part C — Add a derived column

mean_measurement = clean_df[['measurement_1', 'measurement_2']].mean(axis=1)
clean_df = clean_df.assign(mean_result=mean_measurement)


# Part D — Create a grouped summary

group_summary = (
  clean_df
  .groupby(['treatment'], as_index=False)
  .agg(
    sample_count=('sample_id', 'count'),
    mean_result=('mean_result', 'mean'),
    minimum_result=('mean_result', 'min'),
    maximum_result=('mean_result', 'max'),
    mean_temperature=('temperature', 'mean')
  )
)

# removing mean_result for 05 notebook exercise
clean_df = clean_df.drop('mean_result', axis=1)

clean_df.to_csv('clean_experiment_results.csv', index=False)
group_summary.to_csv('group_summary.csv', index=False)


# What is the difference between dropna() and fillna()?
# dropna(subset=[...]) removes dataframe rows that contain missing values for the columns listed in subset
# fillna() allows missing values to to replaced with the value listed in the ()

# Why did the blank numeric CSV cells become NaN rather than empty strings?
# pandas recognises blank CSV fields as missing values by default and represents them as NaN. Because the affected columns 
# otherwise contain numbers, pandas infers them as numeric columns rather than text columns.

# What does groupby() do conceptually?
# Groups rows in a dataframe according to a specified shared column

# Why was it useful to preserve experiment_df and create a separate clean_df?
# To keep the original data untouched to ensure changes made in the program do not mutate the original data

# What is the difference between an exact duplicate row and a duplicated sample_id?
# eaxct duplicate row has duplicated values across each column (which match all the colunms in a previous row), whereas
# a duplicated sample_id does not contain duplicate values for all of its columns, just the sample_id value