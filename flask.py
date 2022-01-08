from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
    "inputs": 5,
    "category": "Sport",
    "word": "Chess",
  },
  {
    "inputs": 5,
    "category": "Food Item",
    "word": "Pizza",
  },
  {
    "inputs": 9,
    "category": "Indin State",
    "word": "Telengana",
  }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(templates)
    })

if __name__ == "__main__":
    app.run(debug=True)

    