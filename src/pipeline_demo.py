import stanza
from dalle2 import Dalle2

#patrick is fucking retarted sometimes

pos_exlude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']

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

    final_string_list = []
    for word in doc.sentences[0].words:
        if word.upos not in set(pos_exlude):
            final_string_list.append(word.text)

    return " ".join(final_string_list)

def print_file_paths(file_paths):
    for path in file_paths:
        print(path + "\n")

if __name__ == '__main__':
    print("Please input a one sentence scene of a story")
    input_string = str(input())
    print("What style would you link your art in? (comic, digital art, drawing)")
    input_style = str(input())

    processed_text = textProcessing(input_string)
    processed_text = processed_text + " " + input_style + " style"
    print(processed_text)
    file_paths = imageGeneration(processed_text)
    print("Your generated images are at these paths:\n")
    print_file_paths(file_paths)