#Natural Language Processing for our projects
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


import spacy
import neuralcoref
from spacy.cli import download
from string import punctuation

input_string = "A cat, grown feeble with age and no longer able to hunt mice as she once did, thought to herself how she might entice them within reach of her paw. Thinking that she might pass herself off for a bag or for a dead cat at least, she suspended herself by the hind legs from a peg, in the hope that the mice would no longer be afraid to come near her."

#download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")
#neuralcoref.add_to_pipe(nlp)
#doc = nlp(input_string)

#print(doc._.coref_resolved)


def pronoun_coref(text):
    doc = nlp(text)
    pronouns = [(tok, tok.i) for tok in doc if (tok.tag_ == "PRP")]
    names = [(ent.text, ent[0].i) for ent in doc.ents if ent.label_ == 'PERSON']
    doc = [tok.text_with_ws for tok in doc]
    for p in pronouns:
        replace = max(filter(lambda x: x[1] < p[1], names),
                      key=lambda x: x[1], default=False)
        if replace:
            replace = replace[0]
            if doc[p[1] - 1] in punctuation:
                replace = ' ' + replace
            if doc[p[1] + 1] not in punctuation:
                replace = replace + ' '
            doc[p[1]] = replace
    doc = ''.join(doc)
    return doc


print(pronoun_coref(input_string))