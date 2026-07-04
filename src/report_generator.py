def generate_summary_report(df):
    """
    Generate a simple text-based Kenya county weather risk summary report.
    """

    total_locations = len(df)
    high_risk_count = len(df[df["risk_level"] == "High"])
    medium_risk_count = len(df[df["risk_level"] == "Medium"])
    low_risk_count = len(df[df["risk_level"] == "Low"])

    report = f"""
=========================================
KENYA COUNTY WEATHER RISK REPORT
=========================================

Total counties successfully monitored: {total_locations}

Risk Summary:
- High Risk: {high_risk_count}
- Medium Risk: {medium_risk_count}
- Low Risk: {low_risk_count}

County-Level Details:
"""

    for _, row in df.iterrows():
        report += f"""
-----------------------------------------
County: {row['county']}, {row['country']}
Location Used: {row['location_used']}
Temperature: {row['temperature']}°C
Feels Like: {row['feels_like']}°C
Humidity: {row['humidity']}%
Pressure: {row['pressure']} hPa
Wind Speed: {row['wind_speed']} m/s
Weather: {row['weather_description']}
Risk Score: {row['risk_score']}
Risk Level: {row['risk_level']}
Timestamp: {row['timestamp']}
"""

    return report