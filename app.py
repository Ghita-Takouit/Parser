# app.py

from flask import Flask, render_template, request, jsonify
from parser import valider_phrase  


app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def valider():
    data = request.json
    phrase = data.get("sentence", "")
    est_valide = valider_phrase(phrase)
    return jsonify({"valid": est_valide})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
