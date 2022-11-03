import stanza
from dalle2 import Dalle2
import os

pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

#patrick is very smart

# asdf

def imageGeneration(text):
    dalle = Dalle2("sess-q3JpYmKLzWgsiXdbQOAYZpKT5p7jtALHN8zy3DEI")
    images = dalle.generate(text)
    print(images)
    file_paths = dalle.download(images)
    return file_paths

def textProcessing(text):
    #very basic processing
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(text)

    final_strings = []

    for sentence in doc.sentences:
        cur_string = []
        for word in sentence.words:
            if word.upos not in set(pos_exclude):
                cur_string.append(word.text)
        cur_string = ' '.join(cur_string)
        final_strings.append(cur_string)

    return final_strings

def print_file_paths(file_paths):
    for path in file_paths:
        print(path + "\n")

if __name__ == '__main__':
    print("Please input a one sentence scene of a story")
    input_string = str(input())
    print("What style would you link your art in? (comic, digital art, drawing)")
    input_style = str(input())

    processed_text = textProcessing(input_string)
    parent_file_paths = []
    for input in processed_text:
        input = input + ' ' + input_style + ' style'
        file_paths = imageGeneration(input)
        parent_file_paths.append(file_paths)

    print("Your generated images are at these paths:\n")
    print_file_paths(file_paths)