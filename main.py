from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store passenger location
passenger_location = None

@app.route('/')
def home():
    return "Welcome! Use /passenger or /driver to access the respective pages."

@app.route('/passenger', methods=['GET', 'POST'])
def passenger():
    global passenger_location
    if request.method == 'POST':
        # Get passenger location from the request
        passenger_location = request.json
        return jsonify({"message": "Location received successfully!"})
    return render_template('passenger.html')

@app.route('/driver')
def driver():
    global passenger_location
    return render_template('driver.html', location=passenger_location)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
