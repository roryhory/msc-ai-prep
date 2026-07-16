import main
import pytest


def test_valid_headers():
    main.validate_headers(['sample_id', 'condition', 'replicate', 'measurement', 'run_date'])

def test_empty_headers():
    with pytest.raises(ValueError, match = 'CSV file does not contain a header'):
        main.validate_headers([])

def test_duplicate_id():
    used_ids = {'S001'}

    with pytest.raises(ValueError, match = 'Skip: duplicate sample_id "S001"'):
        main.validate_unique_id('S001', used_ids)

def test_negative_replicate():
    with pytest.raises(ValueError, match = 'Skip: invalid replicate "-1" - value must be an integer from 1 to 6'):
        main.validate_replicate('-1')