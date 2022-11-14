#Testing dictionary usage
import stanza
import os

pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

noun_list = []

def textProcessing(text):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(text)
    new_doc = []
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.upos in set(pos_exclude):
                sentence.words.remove(word)
        new_doc.append(sentence.words)
    return new_doc

def addToDict(doc):
    attr_list = []
    mydict = {}
    for word in doc:
        if word.upos == "NOUN" and word.deprel == "nsubj":
            #print("noun found")
            mydict['noun'] = word.text
        if word.upos == "PROPN":
            #only want to do this if the pronoun comes after a noun?
            #print("pronoun found")
            mydict['pnoun'] = word.text
        if word.upos == "ADJ":
            #print("adjective found")
            attr_list.append(word.text)
            #print(attr_list)
            mydict['attr'] = attr_list
            #print(mydict)
    noun_list.append(mydict)
    #it is currently replacing the old noun when it sees a new one,
    # have to only add attributes whose "head" is equal to the noun
    

if __name__ == "__main__":
    input_string = "A Fox one day spied a beautiful bunch of ripe grapes hanging from a vine trained along the branches of a tree. The grapes seemed ready to burst with juice, and the Fox's mouth watered as he gazed longingly at them."
    proc_doc = textProcessing(input_string)
    print(proc_doc)
    for doc in proc_doc:
        addToDict(doc)
    print(noun_list)
