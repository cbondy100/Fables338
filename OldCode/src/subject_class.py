# import necessary libraries up here
import stanza
import os

# not sure if we need any of this file still

pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

#Use a scene class instead
# Steps:
# - store whole sentence in doc in class
# - pull out the noun and proper noun pairings
# - pull our attributes (adjectives) store in list
# - pull out action verbs?

# Thoughts:
# - may have to store "nouns" in dictionary with noun as key and list of adjectives as value
# - can do this using the dependency relation tree
# - each adjective's head should be associated noun

class Scene:
    # initialize noun pairings, attributes
    def __init__(self, doc):
        self.doc = doc
        self.subject = getSubject(doc)
        self.propernoun = properNouns(doc)
        self.attributes = getAttributes(doc)

    def hasProperNoun(self):
        #print(self.propernoun)
        if self.propernoun.id < self.subject.id:
            #this means that we see a proper noun before any subject is defined, replacement needed
            return True
        return False

    def replace(self, rword):
        print("replacing: " + self.propernoun.text + " with: " + rword.text)
        for word in self.doc:
            if word == self.propernoun:
                index = self.doc.index(word)
                self.doc[index] = rword

    def getText(self):
        word_list = []
        for word in self.doc:
            word_list.append(word.text)
        return " ".join(word_list)


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

def findMatch(scene, pnoun):
    if scene.propernoun.text == pnoun.text:
        return scene.subject

def replaceProper(scene_list):
    for i, scene in enumerate(scene_list):
        #if scene.hasProperNoun():
            #replacement needed
        print("replace")
        for s in scene_list[0:i]:

            noun_match = findMatch(s, scene.propernoun)
            scene.replace(noun_match)

def printSceneText(scenes):
    for s in scenes:
        print(s.getText()+ '\n')

if __name__ == "__main__":
    input_string = "There once was a small green ogre named Jefferey. Jefferey lived in a big wet swamp. Jeffery was very sad because he was stinky."
    processes_scenes = textProcessing(input_string)
    replaceProper(processes_scenes)
    printSceneText(processes_scenes)