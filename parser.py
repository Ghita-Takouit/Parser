# parse.py

# Fonction pour charger les mots 
def charger_mots(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        return set(mot.strip() for mot in fichier.readlines())

# Charger les composants grammaticaux
articles = charger_mots('articles.txt')
verbes = charger_mots('verbes.txt')
noms = charger_mots('noms.txt')

# Parseur descendant récursif
class Parseur:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def correspondre(self, attendu):
        if self.pos < len(self.tokens) and self.tokens[self.pos] in attendu:
            self.pos += 1
            return True
        return False

    def parse_sujet(self):
        return self.correspondre(articles) and self.correspondre(noms)

    def parse_complement(self):
        return self.correspondre(articles) and self.correspondre(noms)

    def parse_phrase(self):
        if self.parse_sujet() and self.correspondre(verbes) and self.parse_complement():
            return True
        return False

# Fonction principale pour valider une phrase
def valider_phrase(phrase):
    tokens = phrase.lower().split()
    parseur = Parseur(tokens)
    return parseur.parse_phrase()
