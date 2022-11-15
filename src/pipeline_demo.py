import stanza
from dalle2 import Dalle2
import os
import requests

class imageGenerator:

    pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']
#sess-Y5PgcdYxRMvqfK8YMUvGVpZdGNTrNNVDi3UJfau5
#sess-q3JpYmKLzWgsiXdbQOAYZpKT5p7jtALHN8zy3DEI
    @classmethod
    def imageGeneration(cls, text):
        #dalle = Dalle2("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")
        #images = dalle.generate(text)
        text = text[0]
        url = "https://api.openai.com/v1/images/generations"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer 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"}
        data = {"prompt": text, "n": 4, "size": "1024x1024"}
        images = requests.post(url, json = data, headers = headers)
        print(images)
        returned = images.json()
        print(returned)
        output_url = returned['data'][0]['url']
        #file_paths = dalle.download(images)
        return output_url

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
        for file in os.listdir(os.getcwd()):
            if file.endswith('.webp'):
                os.remove(file)
        processed_text = cls.textProcessing(input_string)
        return cls.imageGeneration(processed_text)

if __name__ == '__main__':
    print(imageGenerator.main('car', 'comic'))