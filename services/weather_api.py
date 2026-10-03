from datetime import date, timedelta
import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city):
    response = requests.get(
        GEOCODING_URL,
        params={
            "name": city,
            "count": 1,
            "language": "pt",
            "format": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    results = response.json().get("results", [])
    return results[0] if results else None

def current_weather(latitude, longitude):
    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,relative_humidity_2m,"
                "apparent_temperature,precipitation,"
                "wind_speed_10m,surface_pressure"
            ),
            "timezone": "auto",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["current"]

def historical_weather(latitude, longitude):
    end = date.today() - timedelta(days=1)
    start = end.replace(year=end.year - 20)

    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            "daily": "temperature_2m_mean",
            "timezone": "auto",
        },
        timeout=20,
    )
    response.raise_for_status()
    daily = response.json()["daily"]

    # Calcula uma média anual a partir dos dados diários retornados.
    by_year = {}
    for day, temp in zip(daily["time"], daily["temperature_2m_mean"]):
        if temp is None:
            continue
        year = int(day[:4])
        by_year.setdefault(year, []).append(temp)

    years = sorted(by_year)
    temperatures = [
        round(sum(by_year[year]) / len(by_year[year]), 2)
        for year in years
    ]

    return {
        "years": years,
        "temperatures": temperatures,
        "start": start.isoformat(),
        "end": end.isoformat(),
    }
