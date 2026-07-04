import pandas as pd
from risk_model import calculate_risk_score, classify_risk


def transform_weather_data(weather_records):
    """
    Convert a list of weather records into a clean DataFrame
    and add risk score and risk level.
    """

    if not weather_records:
        raise ValueError("No weather records provided for transformation.")

    df = pd.DataFrame(weather_records)

    df["risk_score"] = df.apply(calculate_risk_score, axis=1)
    df["risk_level"] = df["risk_score"].apply(classify_risk)

    return df