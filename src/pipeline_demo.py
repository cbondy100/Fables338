import stanza
from dalle2 import Dalle2
import os

class imageGenerator:

    pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

    @classmethod
    def imageGeneration(cls, text):
        dalle = Dalle2("sess-q3JpYmKLzWgsiXdbQOAYZpKT5p7jtALHN8zy3DEI")
        images = dalle.generate(text)
        print(images)
        file_paths = dalle.download(images)
        return file_paths

    @classmethod
    def textProcessing(cls, text):
        #very basic processing
        nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        doc = nlp(text)

        final_strings = []

        for sentence in doc.sentences:
            cur_string = []
            for word in sentence.words:
                if word.upos not in set(cls.pos_exclude):
                    cur_string.append(word.text)
            cur_string = ' '.join(cur_string)
            final_strings.append(cur_string)

        return final_strings

    @classmethod
    def print_file_paths(cls, file_paths):
        for path in file_paths:
            print(path + "\n")

    @classmethod
    def main(cls, input_string, input_style):
        processed_text = cls.textProcessing(input_string)
        parent_file_paths = []
        for input in processed_text:
            input = input + ' ' + input_style + ' style'
            file_paths = cls.imageGeneration(input)
            parent_file_paths.append(file_paths)

        print("Your generated images are at these paths:\n")
        cls.print_file_paths(file_paths)