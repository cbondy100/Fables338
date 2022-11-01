import stanza
from dalle2 import Dalle2

def imageGeneration(text):
    dalle = Dalle2("sess-q3JpYmKLzWgsiXdbQOAYZpKT5p7jtALHN8zy3DEI")
    file_paths = dalle.generate_and_download(text)

def textProcessing(text):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(text)
    return 

if __name__ == '__main__':
    input_string = str(input())
