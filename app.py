from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUOTES_PATH = os.path.join(BASE_DIR, "quotes.txt")

def load_quotes():
    quotes = {}
    with open(QUOTES_PATH, "r") as file:
        for line in file:
            if "|" in line:
                category, text = line.strip().split("|", 1)
                quotes.setdefault(category, []).append(text)
    return quotes

@app.route("/")
def home():
    quotes_by_category = load_quotes()

    selected_category = request.args.get("category", "motivation")

    if selected_category not in quotes_by_category:
        selected_category = "motivation"

    quote = random.choice(quotes_by_category[selected_category])

    return render_template(
        "index.html",
        quote=quote,
        selected_category=selected_category
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
