# import necessary libraries up here
import stanza
import os

class Subject:
    # initialize noun pairings, attributes
    def __init__(self, nouns, attributes):
        self.nouns = nouns
        self.attributes = attributes

    def getSubject():
        pass


def textProcessing(text):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(text)
    print(doc.sentences)

if __name__ == "__main__":
    input_string = "There once was a green ogre named Jefferey"
    processed_text = text_processing(input_string)
