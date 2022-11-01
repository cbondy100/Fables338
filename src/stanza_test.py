#Testing the Stanford Stanza API
import stanza

"""
Next Steps:
    - before structural analysis, must replace pronouns with nouns
    - read over dependency relations
    - possible use of constituency relations to remove unnecessary clauses
"""

#stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
doc = nlp("A buck, pursued by hunters, concealed himself among the branches of a vine")

pos_exlude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

#POS tags
#print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')

#depparse
#print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')

#constituency processor
#print(doc.sentences[0].constituency)

class wordNode:
    def __init__(self, word):
        self.word = word
        self.children = []

def newNode(word):
    temp = wordNode(word)
    return temp

def LevelOrderTraversal(root):
 
    if (root == None):
        return;

    q = []  # Create a queue
    q.append(root); # Enqueue root
    while (len(q) != 0):
     
        n = len(q);
        while (n > 0):
            p = q[0]
            q.pop(0);
            print(p.key, end=' ')
            
            for i in range(len(p.child)):
                q.append(p.child[i]);
            n -= 1
   
        print() # Print new line between two levels

for word in doc.sentences[0].words:
    if word.head == 0:
        root = newNode(word)

for word in doc.sentences[0].words:
