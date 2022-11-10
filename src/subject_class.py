# import necessary libraries up here
import stanza
import os

pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']


class Subject:
    # initialize noun pairings, attributes
    def __init__(self, nouns, attributes):
        self.nouns = nouns
        self.attributes = attributes

    def getSubject():
        pass

def getAttributes(doc):
    for word in doc.sentences[0].words:
        pass

def textProcessing(text):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(text)
    for word in doc.sentences[0].words:
        if word.upos in set(pos_exclude):
            doc.sentences[0].words.remove(word)
        if word.upos == "NOUN":
            subject = Subject(word.lemma, )
    new_doc = doc.sentences[0].words

if __name__ == "__main__":
    input_string = "There once was a green ogre named Jefferey"
    processed_text = textProcessing(input_string)
