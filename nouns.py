import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

noun = []

def pos(text_file):
    with open(text_file, encoding='utf8', errors='ignore') as f:
        text = noun(f.read())
        for token in text:
                if token.pos_ == "NOUN":
                    noun.append(token.text)
                if token.pos_ == "PROPN":
                    noun.append(token.text)


noun('user.txt')
