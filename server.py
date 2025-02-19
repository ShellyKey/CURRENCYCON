from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Exchange rates (sample values, ideally fetch from an API)
exchange_rates = {
    "INR": {"JPY": 1.80, "KRW": 15.2, "AUD": 0.018, "NPR": 1.6, "AED": 0.044, "EUR": 0.011, "GBP": 0.0095, "MXN": 0.22, "USD": 0.012, "INR": 1.0},
    "JPY": {"INR": 0.55, "KRW": 8.5, "AUD": 0.010, "NPR": 0.89, "AED": 0.024, "EUR": 0.0061, "GBP": 0.0053, "MXN": 0.12, "USD": 0.0067, "JPY": 1.0},
    "KRW": {"INR": 0.066, "JPY": 0.12, "AUD": 0.00081, "NPR": 0.058, "AED": 0.0028, "EUR": 0.00072, "GBP": 0.00061, "MXN": 0.015, "USD": 0.00076, "KRW": 1.0},
    "AUD": {"INR": 55.0, "JPY": 100.0, "KRW": 1235.0, "NPR": 88.5, "AED": 2.68, "EUR": 0.60, "GBP": 0.51, "MXN": 12.3, "USD": 0.66, "AUD": 1.0},
    "NPR": {"INR": 0.62, "JPY": 1.12, "KRW": 17.1, "AUD": 0.011, "AED": 0.027, "EUR": 0.006, "GBP": 0.005, "MXN": 0.13, "USD": 0.0075, "NPR": 1.0},
    "AED": {"INR": 22.3, "JPY": 41.2, "KRW": 355.0, "AUD": 0.37, "NPR": 37.2, "EUR": 0.25, "GBP": 0.21, "MXN": 5.3, "USD": 0.27, "AED": 1.0},
    "EUR": {"INR": 91.2, "JPY": 164.0, "KRW": 1389.0, "AUD": 1.68, "NPR": 105.3, "AED": 3.67, "GBP": 0.86, "MXN": 20.5, "USD": 1.1, "EUR": 1.0},
    "GBP": {"INR": 104.5, "JPY": 189.0, "KRW": 1600.0, "AUD": 1.96, "NPR": 120.6, "AED": 4.25, "EUR": 1.16, "MXN": 24.1, "USD": 1.28, "GBP": 1.0},
    "MXN": {"INR": 4.5, "JPY": 8.1, "KRW": 65.0, "AUD": 0.081, "NPR": 4.9, "AED": 0.19, "EUR": 0.049, "GBP": 0.042, "USD": 0.053, "MXN": 1.0},
    "USD": {"INR": 83.0, "JPY": 150.0, "KRW": 1300.0, "AUD": 1.52, "NPR": 109.0, "AED": 3.67, "EUR": 0.91, "GBP": 0.78, "MXN": 18.9, "USD": 1.0},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    amount = float(data.get("amount", 0))
    from_currency = data.get("from_currency")
    to_currency = data.get("to_currency")

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        return jsonify({"converted_amount": round(converted_amount, 2)})
    else:
        return jsonify({"error": "Invalid currency"}), 400

if __name__ == "__main__":
    app.run(debug=True)
