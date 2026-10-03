from flask import Blueprint, render_template

impact_bp = Blueprint("impact", __name__)

@impact_bp.get("/impactos")
def impacts():
    return render_template("impacts.html")
