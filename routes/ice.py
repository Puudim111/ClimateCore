from flask import Blueprint, render_template

ice_bp = Blueprint("ice", __name__)

@ice_bp.get("/calotas")
def ice():
    return render_template("ice.html")
