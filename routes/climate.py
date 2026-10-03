from flask import Blueprint, render_template, request
from services.weather_api import geocode_city, current_weather, historical_weather
from services.chart_generator import create_line_chart

climate_bp = Blueprint("climate", __name__)

@climate_bp.route("/clima-local", methods=["GET", "POST"])
def climate():
    weather = None
    history = None
    chart = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Digite uma cidade."
        else:
            try:
                location = geocode_city(city)
                if not location:
                    error = "Cidade não encontrada."
                else:
                    weather = current_weather(location["latitude"], location["longitude"])
                    history = historical_weather(location["latitude"], location["longitude"])
                    chart = create_line_chart(
                        history["years"],
                        history["temperatures"],
                        "temperature_history"
                    )
                    weather["city"] = location["name"]
                    weather["country"] = location.get("country", "")
            except Exception:
                error = "Não foi possível obter os dados climáticos agora. Tente novamente."

    return render_template(
        "climate.html",
        weather=weather,
        history=history,
        chart=chart,
        error=error,
        city=city
    )
