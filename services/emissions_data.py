import io
import requests
import pandas as pd

# Our World in Data oferece um CSV público com emissões de CO2.
# O download é feito pelo backend; nenhum JavaScript é necessário.
OWID_URL = (
    "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
)

def get_emissions_data():
    try:
        response = requests.get(OWID_URL, timeout=30)
        response.raise_for_status()

        df = pd.read_csv(io.BytesIO(response.content))

        world = df[df["country"] == "World"][["year", "co2"]].dropna()
        world = world.tail(20)

        return {
            "years": world["year"].astype(int).tolist(),
            "values": world["co2"].astype(float).round(2).tolist(),
            "unit": "milhões de toneladas de CO₂",
            "source": "Our World in Data / Global Carbon Project",
        }
    except Exception:
        # Fallback mínimo para o site não quebrar.
        return {
            "years": [],
            "values": [],
            "unit": "dados indisponíveis",
            "source": "Our World in Data / Global Carbon Project",
        }
