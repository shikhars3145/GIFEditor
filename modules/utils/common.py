import re

def numerical_sort(value):
    """Sort strings numerically based on the number in the filename."""
    numbers = re.findall(r'\d+', value)
    return int(numbers[0]) if numbers else 0