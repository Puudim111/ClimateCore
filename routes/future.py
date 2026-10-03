from flask import Blueprint, render_template

future_bp = Blueprint("future", __name__)

@future_bp.get("/futuro")
def future():
    return render_template("future.html")
