from flask import Flask, render_template, request

app = Flask(__name__)

# Function to analyze AQI
def analyze_aqi(aqi):
    if aqi < 0 or aqi > 500:
        return "Invalid", "Invalid AQI value.", "Please enter a valid AQI.", ""

    if 0 <= aqi <= 50:
        return "GOOD", "No health risk.", "Enjoy outdoor activities.", ""
    elif 51 <= aqi <= 100:
        return "SATISFACTORY", "Minor discomfort for sensitive people.", "Be cautious.", ""
    elif 101 <= aqi <= 200:
        return "MODERATE", "Breathing discomfort possible.", "Limit outdoor activities.", ""
    elif 201 <= aqi <= 300:
        return "POOR", "Lung and heart issues possible.", "Wear mask and avoid outdoors.", ""
    elif 301 <= aqi <= 400:
        return "VERY POOR", "Serious respiratory issues.", "Stay indoors.", ""
    else:
        return "SEVERE", "Health emergency!", "Avoid going outside.", ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    city = request.form["city"]
    aqi = int(request.form["aqi"])
    source = request.form["source"]

    category, health, prevention, _ = analyze_aqi(aqi)

    return render_template(
        "result.html",
        city=city,
        aqi=aqi,
        category=category,
        health=health,
        prevention=prevention,
        source=source
    )

if __name__ == "__main__":
    app.run(debug=True)
