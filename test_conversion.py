import pytest
from engineering_conversion.conversion_system.conversion import BaseConversion

def test_BaseConversion_class():
    # Test 1: Check if the instance is created with the correct conversion_rates
    length_conversion_rates = {
        str: float
    }
    result = BaseConversion(length_conversion_rates)
    assert result.conversion_rates == length_conversion_rates

    # Test 2: Check if the convert method works as expected
    # Assuming you are converting meters to feet
    input_value = 5.0  # Some input value in meters
    expected_result = input_value * length_conversion_rates[str]
    converted_value = result.convert(input_value, str)
    assert converted_value == expected_result


  
