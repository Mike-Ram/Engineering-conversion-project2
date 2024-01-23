import pytest
from engineering_conversion.conversion_system.conversion import BaseConversion

def test_BaseConversion_class():
    length_conversion_rates = {
         str: int
    }
    result = BaseConversion(length_conversion_rates)
    assert result.conversion_rates == length_conversion_rates
    