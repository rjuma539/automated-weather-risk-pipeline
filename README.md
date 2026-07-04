# Automated Kenya County Weather Risk Pipeline

## Project Overview

This project is a Python-based automation pipeline that collects live weather data from the OpenWeather API for Kenyan counties, processes the data, calculates weather risk scores, and generates automated CSV and text reports.

The project demonstrates API integration, secure API key handling, automation, data transformation, risk scoring, error handling, and analytics reporting.

## Business Problem

Field operations, logistics teams, monitoring teams, and digital strategy teams often need timely weather intelligence to support planning and reduce operational risks.

Manually checking weather conditions county by county is repetitive, slow, and prone to inconsistency.

## Solution

This project automates the process by fetching live weather data for Kenyan counties, calculating weather risk levels, and generating structured outputs for decision-making.

## Key Features

- Connects to OpenWeather API using an API key
- Uses `.env` for secure API key management
- Collects weather data for Kenyan counties
- Uses representative county locations for weather lookup
- Calculates weather risk scores
- Classifies counties as Low, Medium, or High risk
- Generates CSV outputs
- Generates text-based risk reports
- Handles failed API requests without stopping the full pipeline
- Saves failed locations separately for review

## Tech Stack

- Python
- Requests
- Pandas
- Python-dotenv
- Git
- GitHub

## Project Structure

```text
automated-weather-risk-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── src/
│   ├── config.py
│   ├── fetch_weather.py
│   ├── risk_model.py
│   ├── transform_data.py
│   ├── report_generator.py
│   └── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md