import pytest
from shorturl.settings import Settings  # Import your Settings class

def test_default_values():
    settings = Settings()

    assert settings.DBHOST == "redis"
    assert settings.DBPORT == 6379
    assert settings.DBUSER is None
    assert settings.DBPASS is None
    assert settings.KEYLEN == 8

def test_custom_values():
    custom_values = {
        "DBHOST": "localhost",
        "DBPORT": 1234,
        "DBUSER": "test_user",
        "DBPASS": "test_pass",
        "KEYLEN": 10,
    }
    settings = Settings(**custom_values)

    assert settings.DBHOST == "localhost"
    assert settings.DBPORT == 1234
    assert settings.DBUSER == "test_user"
    assert settings.DBPASS == "test_pass"
    assert settings.KEYLEN == 10

def test_invalid_type():
    with pytest.raises(ValueError):
        invalid_values = {
            "DBHOST": 123,  # Should be a string
            "DBPORT": "1234",  # Should be an int
            "DBUSER": "test_user",
            "DBPASS": "test_pass",
            "KEYLEN": 10,
        }
        Settings(**invalid_values)

def test_optional_fields():
    custom_values = {
        "DBHOST": "localhost",
        "DBPORT": 1234,
        "KEYLEN": 10,
    }
    settings = Settings(**custom_values)

    assert settings.DBUSER is None
    assert settings.DBPASS is None
