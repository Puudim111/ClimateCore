from flask import Blueprint, render_template
from services.emissions_data import get_emissions_data
from services.chart_generator import create_line_chart

emissions_bp = Blueprint("emissions", __name__)

@emissions_bp.get("/emissoes")
def emissions():
    data = get_emissions_data()
    chart = create_line_chart(
        data["years"],
        data["values"],
        "global_co2_emissions"
    )
    return render_template("emissions.html", data=data, chart=chart)
