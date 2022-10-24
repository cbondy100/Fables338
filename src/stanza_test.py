#Testing the Stanford Stanza API
import stanza

#stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
doc = nlp("Patrick went to the store and bought himself a sandwich")

print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')


"""
Output Structure: For each word, you have the processors applied
Example:
{
    id: location of word in sentence
    text: actual word that was inputed
    lemma: base form of above word
    upos: universal part of speech
    xpos: NOT NEEDED
    feats: universal morphological features
    head: head index of each work
    deprel: dependency relationship between words
    start_char:
    end_char:
}

The "depparse" processor builds a relationship tree
Example:
Sentence: Patrick went to the store and bought himself a sandwich

id: 1   word: Patrick   head id: 2      head: went      deprel: nsubj
id: 2   word: went      head id: 0      head: root      deprel: root 
id: 3   word: to        head id: 5      head: store     deprel: case
id: 4   word: the       head id: 5      head: store     deprel: det
id: 5   word: store     head id: 2      head: went      deprel: obl
id: 6   word: and       head id: 7      head: bought    deprel: cc
id: 7   word: bought    head id: 2      head: went      deprel: conj
id: 8   word: himself   head id: 7      head: bought    deprel: iobj
id: 9   word: a         head id: 10     head: sandwich  deprel: det
id: 10  word: sandwich  head id: 7      head: bought    deprel: obj

"""