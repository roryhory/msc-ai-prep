import csv
import sys
from datetime import datetime

input_file = 'baseline_experimental_results.csv'
output_file = 'processed_results.csv'

SAMPLE_ID = 'sample_id'
CONDITION = 'condition'
REPLICATE = 'replicate'
MEASUREMENT = 'measurement'
RUN_DATE = 'run_date'

required_columns = [
    SAMPLE_ID,
    CONDITION,
    REPLICATE,
    MEASUREMENT,
    RUN_DATE
]
required_conditions = [
    'Control', 
    'Treatment_A', 
    'Treatment_B', 
    'Treatment_C'
]


def validate_headers(headers):
    if len(headers) == 0 or headers is None:
        raise ValueError('CSV file does not contain a header')

    for column in required_columns:
        if column not in headers:
            raise ValueError(f'"{column}" is missing from CSV header')
    

def validate_field(field, col):
    if field.strip() == '':
        raise ValueError(f'Skip: missing required field "{col}"')


def validate_unique_id(sample_id, used_ids):
    if sample_id in used_ids:
        raise ValueError(f'Skip: duplicate sample_id "{sample_id}"')


def validate_condition(condition):
    if condition not in required_conditions:
        raise ValueError(f'Skip: invalid condition "{condition}"')


def validate_replicate(value):
    try:
        replicate_number = int(value)
    except ValueError:
        raise ValueError(f'Skip: invalid replicate "{value}" - value must be an integer')
  
    if replicate_number < 1 or replicate_number > 6:
        raise ValueError(f'Skip: invalid replicate "{replicate_number}" - value must be an integer from 1 to 6')


def validate_measurement(value):
    try:
        measurement_number = float(value)
    except ValueError:
        raise ValueError(f'Skip: invalid measurement "{value}" - measurement must be numeric')
  
    if measurement_number < 0 or measurement_number > 150:
        raise ValueError(f'Skip: invalid measurement "{measurement_number}" - measurement must be between 0 and 150')

def validate_run_date(value):
    try:
        parsed_date = datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f'Skip: invalid date "{value}" - date must be in YYYY-MM-DD format')
    
    if parsed_date.strftime('%Y-%m-%d') != value:
        raise ValueError(f'Skip: invalid date "{value}" - date must be in YYYY-MM-DD format')

    
def validate_row(row, used_ids):
    for column in required_columns:
        validate_field(row[column], column)
  
    validate_unique_id(row[SAMPLE_ID], used_ids)
    validate_condition(row[CONDITION] )
    validate_replicate(row[REPLICATE])
    validate_measurement(row[MEASUREMENT])
    validate_run_date(row[RUN_DATE])

  
def group_results(row, used_ids, grouped_results):
    if row[CONDITION] not in grouped_results:
        grouped_results[row[CONDITION]] = []
  
    grouped_results[row[CONDITION]].append(row)
    # Also add ID to used IDs
    used_ids.add(row[SAMPLE_ID])


def summarise_results(key, results, data):
    count = len(results)
    total = 0
    minimum = maximum = None

    for result in results:
        x = float(result[MEASUREMENT])
        total += x
        if minimum is None or x < minimum: minimum = x
        if maximum is None or x > maximum: maximum = x

    mean = round(total / count, 2)
    row = {'condition': key, 'count': count, 'mean': mean, 'minimum': minimum, 'maximum': maximum}
    data.append(row)


def write_results(data):
    with open(output_file, 'w', newline='') as f:
        fieldnames = ['condition', 'count', 'mean', 'minimum', 'maximum']
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    used_ids = set()
    grouped_results = {}
    data = []

    with open(input_file, 'r', newline = '') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        try:
            validate_headers(headers)
        except ValueError as error:
            print(error)
            sys.exit(1)
        
        for row in reader:
            try: 
                validate_row(row, used_ids)
            except ValueError as error:
                print(error)
            else:
                group_results(row, used_ids, grouped_results)

    for key in grouped_results:
        summarise_results(key, grouped_results[key], data)

    write_results(data)


if __name__ == '__main__':
    main()
