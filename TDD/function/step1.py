# Step 1: Write Test
import pytest

def test_calculate_rectangle_area():
    # Define test cases with inputs and expected outputs
    test_cases = [
        (5, 3, 15),  # Width: 5, Height: 3, Expected Area: 15
        (4, 4, 16),  # Width: 4, Height: 4, Expected Area: 16
        (0, 10, 0),  # Width: 0, Height: 10, Expected Area: 0
        (-1, 8, 0),  # Width: -1, Height: 8, Expected Area: 0 (Negative width)
        (6, -3, 0)   # Width: 6, Height: -3, Expected Area: 0 (Negative height)
    ]

    # Iterate through test cases
    for width, height, expected_area in test_cases:
        # Call the function under test and assert the result
        assert calculate_rectangle_area(width, height) == expected_area

if __name__ == "__main__":
    # Call the run_tests function when the script is executed
    test_calculate_rectangle_area()
