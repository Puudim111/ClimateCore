from flask import Blueprint, render_template

solutions_bp = Blueprint("solutions", __name__)

@solutions_bp.get("/solucoes")
def solutions():
    return render_template("solutions.html")
