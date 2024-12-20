from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ARTICLES = {"le", "la", "les", "une", "un", "des", "ce", "ces"}
NOMS = {"souris", "fromage", "chat", "chien", "oiseau", "poisson", "voiture", "maison", 
        "livre", "table", "chaise", "ordinateur", "fenêtre", "porte","portes" ,"jardin", "arbre", 
        "fleur", "soleil", "lune", "étoile", "ciel", "mer", "montagne", "rivière",
        "route", "ville", "village", "forêt", "plage", "île", "océan", "colline", "vallée", "champ"}

VERBES = {"mange", "mangent", "voit", "voient", "construit", "construisent", "attrape", "attrapent", 
          "lit", "lisent", "écrit", "écrivent", "ouvre", "ouvrent", "ferme", "ferment", 
          "regarde", "regardent", "écoute", "écoutent", "aime", "aiment",
          "traverse", "traversent", "habite", "habitent", "explore", "explorent"}

def analyser_phrase(tokens):
    tokens = [token.lower() for token in tokens]
    if not tokens:
        return False, "Entrée vide"
    
    tokens_restants, erreur = analyser_sujet(tokens)
    if erreur:
        return False, f"Erreur de sujet: {erreur}"
    
    tokens_restants, erreur = analyser_verbe(tokens_restants)
    if erreur:
        return False, f"Erreur de verbe: {erreur}"
    
    tokens_restants, erreur = analyser_complement(tokens_restants)
    if erreur:
        return False, f"Erreur de complément: {erreur}"
    
    if tokens_restants:
        return False, f"Tokens inattendus: {' '.join(tokens_restants)}"
    
    return True, "Phrase valide"

def analyser_sujet(tokens):
    if not tokens or tokens[0] not in ARTICLES:
        return tokens, "Article attendu"
    tokens = tokens[1:]
    if not tokens or tokens[0] not in NOMS:
        return tokens, "Nom attendu"
    return tokens[1:], None

def analyser_verbe(tokens):
    if not tokens or tokens[0] not in VERBES:
        return tokens, "Verbe attendu"
    return tokens[1:], None

def analyser_complement(tokens):
    if not tokens or tokens[0] not in ARTICLES:
        return tokens, "Article attendu"
    tokens = tokens[1:]
    if not tokens or tokens[0] not in NOMS:
        return tokens, "Nom attendu"
    return tokens[1:], None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyser', methods=['POST'])
def analyser():
    data = request.json
    if not data or "phrase" not in data:
        return jsonify({"erreur": "Manque 'phrase' dans la requête"}), 400
    
    phrase = data["phrase"]
    tokens = phrase.split()
    est_valide, retour = analyser_phrase(tokens)
    
    return jsonify({
        "valide": est_valide,
        "retour": retour
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
