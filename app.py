from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/upload_statement', methods=['POST'])
def upload_statement():
    from_date = request.form.get('from_date')
    to_date = request.form.get('to_date')
    file = request.files.get('file_name')
    if file:
        return jsonify({
            "message": f"Imported transactions from {from_date} to {to_date} from {file.filename}"
        })
    else:
        return jsonify({"error": "No file uploaded"}), 400

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    return jsonify({
        "message": f"Added {data.get('amount')} ({data.get('category')}) on {data.get('date')}"
    })

@app.route('/set_budget', methods=['POST'])
def set_budget():
    data = request.json
    return jsonify({
        "message": f"Budget set: {data.get('category')} - {data.get('limit')} ({data.get('period')})"
    })

@app.route('/create_goal', methods=['POST'])
def create_goal():
    data = request.json
    return jsonify({
        "message": f"Goal created: {data.get('name')} - Target {data.get('target')}"
    })

@app.route('/add_contribution', methods=['POST'])
def add_contribution():
    data = request.json
    return jsonify({
        "message": f"Contribution added: {data.get('amount')} on {data.get('date')}"
    })

@app.route('/spending_trends/<int:user_id>', methods=['GET'])
def spending_trends(user_id):
    return jsonify({
        "Jan 2026": 1200,
        "Feb 2026": 950
    })

@app.route('/category_breakdown/<int:user_id>', methods=['GET'])
def category_breakdown(user_id):
    return jsonify({
        "Dining": 400,
        "Transport": 200,
        "Utilities": 300
    })

@app.route('/get_coaching/<int:user_id>', methods=['GET'])
def get_coaching(user_id):
    return jsonify([
        "Reduce dining by 10% to accelerate savings goals.",
        "Increase monthly savings contributions by $50."
    ])

@app.route('/simulate_scenario', methods=['POST'])
def simulate_scenario():
    data = request.json
    return jsonify({
        "scenario": data.get('scenario_name'),
        "projected_savings": 40
    })

@app.route('/analyse/<int:user_id>', methods=['GET'])
def analyse(user_id):
    return jsonify({
        "trend": "Jan 2026 - $1200 spent",
        "categories": {"Dining": 400, "Transport": 200, "Utilities": 300},
        "coaching": "Reduce dining by 10% and increase savings contributions by $50."
    })

if __name__ == '__main__':
    app.run(debug=True)
