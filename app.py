# app.py

from flask import Flask, render_template, request, jsonify
from parser import valider_phrase, charger_verbes, charger_noms, charger_articles


app = Flask(__name__)

verbes = charger_verbes()
noms = charger_noms()
articles = charger_articles()

def valider_phrase(phrase):
    mots = phrase.split()
    if len(mots) < 3:
        return False

    article, nom, verbe = mots[0], mots[1], mots[2]
    if article not in articles or nom not in noms or verbe not in verbes:
        return False

    # Check subject-verb agreement
    if nom.endswith('s') and not verbe.endswith('ent'):
        return False
    if not nom.endswith('s') and verbe.endswith('ent'):
        return False

    return True

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
