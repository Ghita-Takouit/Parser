# parse.py

# Fonction pour charger les mots 
def load_words(filename):
    with open(filename, 'r') as file:
        return set(word.strip() for word in file.readlines())

# Charger les composants grammaticaux
articles = load_words('articles.txt')
verbs = load_words('verbs.txt')
nouns = load_words('nouns.txt')

# Parseur descendant récursif
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected):
        if self.pos < len(self.tokens) and self.tokens[self.pos] in expected:
            self.pos += 1
            return True
        return False

    def parse_subject(self):
        return self.match(articles) and self.match(nouns)

    def parse_complement(self):
        return self.match(articles) and self.match(nouns)

    def parse_sentence(self):
        if self.parse_subject() and self.match(verbs) and self.parse_complement():
            return True
        return False

# Fonction principale pour valider une phrase
def validate_sentence(sentence):
    tokens = sentence.lower().split()
    parser = Parser(tokens)
    return parser.parse_sentence()
