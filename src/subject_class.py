# import necessary libraries up here
import stanza
import os

pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

#Use a scene class instead
# Steps:
# - store whole sentence in doc in class
# - pull out the noun and proper noun pairings
# - pull our attributes (adjectives) store in list
# - pull out action verbs?

class Scene:
    # initialize noun pairings, attributes
    def __init__(self, doc):
        self.doc = doc
        self.subject = getSubject(doc)
        self.propernoun = properNouns(doc)
        self.attributes = getAttributes(doc)

def properNouns(doc):
    for word in doc:
        if word.upos == "PROPN":
            return word
        
def getSubject(doc):
    for word in doc:
        if word.upos == "NOUN":
            return word

def getAttributes(doc):
    attributes = []
    for word in doc:
        if word.upos in ["ADJ"]:
            attributes.append(word)
    return attributes

def textProcessing(text):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    scenes = []
    doc = nlp(text)
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.upos in set(pos_exclude):
                sentence.words.remove(word)
        new_doc = sentence.words
        new_scene = Scene(new_doc)
        scenes.append(new_scene)
    return scenes


if __name__ == "__main__":
    input_string = "There once was a small green ogre named Jefferey. Jefferey lived in a big wet swamp."
    processes_scenes = textProcessing(input_string)
    print(processes_scenes[1].doc)
