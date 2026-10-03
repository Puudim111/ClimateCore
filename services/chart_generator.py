from pathlib import Path
import uuid
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GENERATED_DIR = Path("static/generated")
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

def _cleanup_old():
    for path in GENERATED_DIR.glob("*.png"):
        try:
            path.unlink()
        except OSError:
            pass

def create_line_chart(x_values, y_values, prefix):
    _cleanup_old()
    filename = f"{prefix}_{uuid.uuid4().hex}.png"
    output = GENERATED_DIR / filename

    plt.figure(figsize=(10, 4.8))
    plt.plot(x_values, y_values, marker="o")
    plt.title(prefix.replace("_", " ").title())
    plt.xlabel("Ano")
    plt.ylabel("Valor")
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(output, dpi=160)
    plt.close()

    return f"/static/generated/{filename}"

def create_bar_chart(values, prefix):
    _cleanup_old()
    filename = f"{prefix}_{uuid.uuid4().hex}.png"
    output = GENERATED_DIR / filename

    labels = list(values.keys())
    numbers = list(values.values())

    plt.figure(figsize=(9, 4.8))
    plt.bar(labels, numbers)
    plt.title("Emissões estimadas por categoria")
    plt.ylabel("kg CO₂")
    plt.xticks(rotation=15)
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()
    plt.savefig(output, dpi=160)
    plt.close()

    return f"/static/generated/{filename}"
