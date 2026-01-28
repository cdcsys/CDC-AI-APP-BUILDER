from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# --- Serve the frontend (index.html) ---
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# --- Upload Bank Statement ---
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

# --- Add Expense ---
@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    return jsonify({
        "message": f"Added {data.get('amount')} ({data.get('category')}) on {data.get('date')}"
    })

# --- Set Budget ---
@app.route('/set_budget', methods=['POST'])
def set_budget():
    data = request.json
    return jsonify({
        "message": f"Budget set: {data.get('category')} - {data.get('limit')} ({data.get('period')})"
    })

# --- Create Savings Goal ---
@app.route('/create_goal', methods=['POST'])
def create_goal():
    data = request.json
    return jsonify({
        "message": f"Goal created: {data.get('name')} - Target {data.get('target')}"
    })

# --- Add Contribution ---
@app.route('/add_contribution', methods=['POST'])
def add_contribution():
    data = request.json
    return jsonify({
        "message": f"Contribution added: {data.get('amount')} on {data.get('date')