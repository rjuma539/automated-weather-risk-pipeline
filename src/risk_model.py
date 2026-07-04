def calculate_risk_score(row):
    """
    Calculate a weather risk score based on temperature, humidity,
    wind speed, and weather condition.

    Score range: 0 to 100
    """

    score = 0

    temperature = row["temperature"]
    humidity = row["humidity"]
    wind_speed = row["wind_speed"]
    weather_main = row["weather_main"].lower()

    # High temperature risk
    if temperature >= 32:
        score += 25
    elif temperature >= 28:
        score += 15

    # High humidity risk
    if humidity >= 80:
        score += 20
    elif humidity >= 70:
        score += 10

    # Wind risk
    if wind_speed >= 8:
        score += 25
    elif wind_speed >= 5:
        score += 10

    # Weather condition risk
    if "rain" in weather_main:
        score += 20

    if "storm" in weather_main or "thunderstorm" in weather_main:
        score += 30

    # Ensure score does not exceed 100
    if score > 100:
        score = 100

    return score


def classify_risk(score):
    """
    Classify the risk score into Low, Medium, or High.
    """

    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"