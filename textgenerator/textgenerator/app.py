# app.py
from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_TOKEN = os.getenv("HF_TOKEN")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def predict(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    try:
        return response.json()[0]["generated_text"]
    except Exception as e:
        print("Error:", e)
        return "Sorry, there was an error. Please try again."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        text = request.form["text"]
        sentiment = predict(text)
        return render_template("result.html", text=text, sentiment=sentiment)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
