import pytest
from module.weather import activity_suggestion


@pytest.mark.parametrize(
    "forecast, temperature, wind_speed, expected",
    [
        # Sunny day tests
        ("sunny", 25, 10, "It's a perfect day to go outside!"),
        ("sunny", 18, 10, "The weather is unpredictable. Decide based on your mood!"),
        ("sunny", 30, 20, "The weather is unpredictable. Decide based on your mood!"),

        # Cloudy day tests
        ("cloudy", 20, 10, "You can go outside, but bring a jacket!"),
        ("cloudy", 10, 10, "Better to stay inside. It's not ideal weather."),
        ("cloudy", 20, 25, "Better to stay inside. It's not ideal weather."),

        # Rainy day tests
        ("rainy", 15, 10, "Better to stay inside. It's not ideal weather."),
        ("rainy", 8, 10, "Better to stay inside. It's not ideal weather."),

        # Snowy day tests
        ("snowy", -5, 10, "It's snowy, but you can enjoy outdoor activities if you dress warmly!"),
        ("snowy", 5, 10, "The weather is unpredictable. Decide based on your mood!"),
        ("snowy", -5, 30, "Better to stay inside. It's not ideal weather."),

        # Edge cases
        ("unknown", 25, 10, "The weather is unpredictable. Decide based on your mood!"),
        ("cloudy", 15, 10, "Better to stay inside. It's not ideal weather."),
    ]
)
def test_activity_suggestion(forecast, temperature, wind_speed, expected):
    """
    Test the activity_suggestion function with various weather conditions.
    """
    result = activity_suggestion(forecast, temperature, wind_speed)
    assert result == expected
