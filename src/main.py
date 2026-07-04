import os
from datetime import datetime

from config import COUNTY_LOCATIONS
from fetch_weather import fetch_location_weather
from transform_data import transform_weather_data
from report_generator import generate_summary_report


def main():
    """
    Main automation pipeline:
    1. Fetch weather data for all 47 Kenyan counties
    2. Transform data
    3. Calculate risk scores
    4. Save CSV output
    5. Generate text report
    """

    print("Starting Kenya county weather risk automation pipeline...")

    weather_records = []
    failed_locations = []

    for item in COUNTY_LOCATIONS:
        county = item["county"]
        location = item["location"]

        try:
            print(f"Fetching weather data for {county} using {location}...")
            record = fetch_location_weather(county, location)
            weather_records.append(record)

        except Exception as error:
            print(f"Failed to fetch data for {county} using {location}. Error: {error}")
            failed_locations.append({
                "county": county,
                "location": location,
                "error": str(error)
            })

    if not weather_records:
        raise ValueError("No weather data was fetched. Please check API key or internet connection.")

    df = transform_weather_data(weather_records)

    today = datetime.now().strftime("%Y-%m-%d")

    processed_path = f"../data/processed/kenya_county_weather_risk_{today}.csv"
    report_path = f"../data/reports/kenya_county_weather_risk_report_{today}.txt"
    failed_path = f"../data/reports/failed_locations_{today}.txt"

    os.makedirs("../data/processed", exist_ok=True)
    os.makedirs("../data/reports", exist_ok=True)

    df.to_csv(processed_path, index=False)

    report = generate_summary_report(df)

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    if failed_locations:
        with open(failed_path, "w", encoding="utf-8") as file:
            file.write("Failed Weather API Locations\n")
            file.write("============================\n\n")

            for item in failed_locations:
                file.write(f"County: {item['county']}\n")
                file.write(f"Location: {item['location']}\n")
                file.write(f"Error: {item['error']}\n")
                file.write("------------------------------------\n")

    print("\nPipeline completed successfully.")
    print(f"Successful locations: {len(weather_records)}")
    print(f"Failed locations: {len(failed_locations)}")
    print(f"Processed data saved to: {processed_path}")
    print(f"Report saved to: {report_path}")

    if failed_locations:
        print(f"Failed locations saved to: {failed_path}")

    print(report)


if __name__ == "__main__":
    main()