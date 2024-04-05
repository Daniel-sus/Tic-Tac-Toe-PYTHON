import pytest
import re


# Test input validation for a valid username
def test_valid_username():
    assert validate_username("user123") == True


# Test input validation for a username containing special characters
def test_username_special_characters():
    with pytest.raises(ValueError):
        validate_username("user';--")


# Test input validation for a valid password
def test_valid_password():
    assert validate_password("StrongPassword123!") == True


# Test input validation for a password containing SQL injection attempts
def test_password_sql_injection():
    with pytest.raises(ValueError):
        validate_password("Password' OR '1'='1")


# Test input validation for other user attributes (e.g., email)
def test_valid_email():
    assert validate_email("user@example.com") == True

