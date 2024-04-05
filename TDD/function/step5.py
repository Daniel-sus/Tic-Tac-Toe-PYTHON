# Step 1: Write Test
import pytest


# NEW TESTS
# Test cases for calculate_rectangle_area function with input validation
def test_calculate_rectangle_area_with_invalid_input():
    # Test with non-number inputs
    with pytest.raises(ValueError):
        calculate_rectangle_area("a", 5)
    with pytest.raises(ValueError):
        calculate_rectangle_area(5, "b")
    # Test with negative inputs
    with pytest.raises(ValueError):
        calculate_rectangle_area(-3,  4)
    with pytest.raises(ValueError):
        calculate_rectangle_area(3, -4)
    # Test with zero inputs
    with pytest.raises(ValueError):
        calculate_rectangle_area(0, 5)
    with pytest.raises(ValueError):
        calculate_rectangle_area(5, 0)


# Step 5: Refactor (Optional)
# Updated calculate_rectangle_area function with input validation
def calculate_rectangle_area(width, height):
    # Check if width and height are numbers
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Width and height must be numbers")
    # Check if width and height are positive
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers")
    # Calculate and return the area of the rectangle
    return width * height



