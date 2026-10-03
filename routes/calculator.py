from flask import Blueprint, render_template, request
from services.co2_calculator import calculate_co2
from services.chart_generator import create_bar_chart

calculator_bp = Blueprint("calculator", __name__)

@calculator_bp.route("/calculadora", methods=["GET", "POST"])
def calculator():
    result = None
    chart = None
    error = None

    if request.method == "POST":
        try:
            distance = float(request.form.get("distance", 0))
            trips = float(request.form.get("trips", 0))
            fuel = request.form.get("fuel", "gasoline")
            electricity = float(request.form.get("electricity", 0))
            food = float(request.form.get("food", 0))

            result = calculate_co2(distance, trips, fuel, electricity, food)
            chart = create_bar_chart(result["categories"], "co2_categories")
        except (ValueError, TypeError):
            error = "Preencha os campos com valores numéricos válidos."

    return render_template(
        "calculator.html",
        result=result,
        chart=chart,
        error=error
    )
