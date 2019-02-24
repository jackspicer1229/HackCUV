import spacy
nlp = spacy.load('en_core_web_lg') #python -m spacy download en_core_web_lg

apples = nlp(u'Look at ground')
oranges = nlp(u'Talk to phil')

ay = apples.similarity(oranges)

print(ay)
