# app.py

from flask import Flask, render_template, request, jsonify
from parser import validate_sentence  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    sentence = data.get("sentence", "")
    is_valid = validate_sentence(sentence)
    return jsonify({"valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
