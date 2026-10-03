from flask import Blueprint, render_template
from services.news_api import get_climate_news


news_bp = Blueprint("news", __name__)


@news_bp.route("/noticias")
def news():
    articles = get_climate_news()

    return render_template(
        "news.html",
        articles=articles
    )