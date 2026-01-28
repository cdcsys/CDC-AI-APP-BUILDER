from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')   # looks inside /templates folder

@app.route('/ping')
def ping():
    return jsonify({"message": "Secure-Fin backend is alive!"})

if __name__ == '__main__':
    app.run(debug=True)
