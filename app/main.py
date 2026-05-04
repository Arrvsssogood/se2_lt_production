from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

FOODS = [
    "Fried Chicken", "Sinigang", "Pizza", "Pancit Inulas",
    "Adobo", "Burger", "Sushi", "Spaghetti na Matigsum", "Pares sa Atubangan kan School", "Tinola",
    "Siomai-Rice", "Pancit Canton", "Harvey's Lechon"
]

@app.route("/")
def index():
    food = random.choice(FOODS)
    return render_template("index.html", food=food)

@app.route("/pick")
def pick():
    food = random.choice(FOODS)
    return jsonify({"food": food})

if __name__ == "__main__":
    app.run(debug=True)
