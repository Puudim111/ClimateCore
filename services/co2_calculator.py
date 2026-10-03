from data.emission_factors import (
    FUEL_FACTORS,
    FUEL_EFFICIENCY,
    ELECTRICITY_FACTOR,
    FOOD_FACTORS,
)

def _non_negative(value):
    return max(float(value), 0.0)

def calculate_co2(distance, trips, fuel, electricity, food):
    distance = _non_negative(distance)
    trips = _non_negative(trips)
    electricity = _non_negative(electricity)
    food = _non_negative(food)

    factor = FUEL_FACTORS.get(fuel, FUEL_FACTORS["gasoline"])
    efficiency = FUEL_EFFICIENCY.get(fuel, FUEL_EFFICIENCY["gasoline"])

    # Distância mensal -> litros -> kg CO2.
    transport = (distance * trips / efficiency) * factor
    energy = electricity * ELECTRICITY_FACTOR

    # Entrada de alimentação simplificada em kg CO2e/mês.
    food_emissions = food * FOOD_FACTORS["medium"]

    categories = {
        "Transporte": round(transport, 2),
        "Energia": round(energy, 2),
        "Alimentação": round(food_emissions, 2),
        "Outros": 0.0,
    }

    monthly = round(sum(categories.values()), 2)
    yearly = round(monthly * 12, 2)

    percentages = {}
    for name, value in categories.items():
        percentages[name] = round((value / monthly * 100), 1) if monthly else 0

    return {
        "monthly": monthly,
        "yearly": yearly,
        "categories": categories,
        "percentages": percentages,
        "note": (
            "Estimativa educativa. Os fatores de emissão variam conforme "
            "combustível, matriz elétrica, hábitos e metodologia adotada."
        ),
    }
