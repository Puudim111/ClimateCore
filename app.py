from flask import Flask, render_template

from routes.main import main_bp
from routes.calculator import calculator_bp
from routes.climate import climate_bp
from routes.emissions import emissions_bp
from routes.ice import ice_bp
from routes.news import news_bp
from routes.impact import impact_bp
from routes.future import future_bp
from routes.solutions import solutions_bp

from services.youtube_api import get_climate_videos


app = Flask(__name__)


@app.route("/")
def home():
    videos = get_climate_videos()

    return render_template(
        "index.html",
        videos=videos
    )


app.register_blueprint(calculator_bp)
app.register_blueprint(climate_bp)
app.register_blueprint(emissions_bp)
app.register_blueprint(ice_bp)
app.register_blueprint(news_bp)
app.register_blueprint(impact_bp)
app.register_blueprint(future_bp)
app.register_blueprint(solutions_bp)


if __name__ == "__main__":
    app.run(debug=True)