def activity_suggestion(forecast, temperature, wind_speed):
    """
    Suggest an activity based on the weather forecast, temperature, and wind speed.
    """
    print(f"Inputs -> forecast: {forecast}, temperature: {temperature}, wind_speed: {wind_speed}")

    if forecast == "sunny" and temperature > 20 and wind_speed < 15:
        return "It's a perfect day to go outside!"

    elif forecast == "cloudy":
        if 15 < temperature <= 25 and wind_speed < 20:
            return "You can go outside, but bring a jacket!"
        return "Better to stay inside. It's not ideal weather."

    elif forecast == "rainy" or wind_speed > 30 or temperature <= 10:
        return "Better to stay inside. It's not ideal weather."

    elif forecast == "snowy":
        # Corrected condition for snowy weather
        if temperature <= 0 and wind_speed <= 25:
            return "It's snowy, but you can enjoy outdoor activities if you dress warmly!"
        elif temperature > 0 and wind_speed <= 25:
            return "The weather is unpredictable. Decide based on your mood!"
        else:
            return "Better to stay inside. It's not ideal weather."

    return "The weather is unpredictable. Decide based on your mood!"
