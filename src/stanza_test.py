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
doc = nlp("One of the hunters, attracted by the rustling, turned round and guessing that their prey was there, shot into the bush and killed him. ")

pos_exlude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

#POS tags
#print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')

#depparse
#print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')

#constituency processor
#print(doc.sentences[0].constituency)

final_string_list = []
for word in doc.sentences[0].words:
    if word.upos not in pos_exlude:
        final_string_list.append(word.lemma)

print(' '.join(final_string_list))