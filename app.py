from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy data (can also load from data.json)
dummy_data = {
    "name": "Shubham Yadav",
    "referral_code": "shubham2025",
    "donations": 5200
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=dummy_data)

@app.route('/api/data')
def get_data():
    return jsonify(dummy_data)

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

if __name__ == '__main__':
    app.run(debug=True)
