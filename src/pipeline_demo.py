import stanza
from dalle2 import Dalle2
import os
import requests

class imageGenerator:

    pos_exclude = ['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X']
#sess-Y5PgcdYxRMvqfK8YMUvGVpZdGNTrNNVDi3UJfau5
#sess-q3JpYmKLzWgsiXdbQOAYZpKT5p7jtALHN8zy3DEI
    @classmethod
    def imageGeneration(cls, text, style):
        #dalle = Dalle2("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")
        #images = dalle.generate(text)
        #text = text[0]
        url = "https://api.openai.com/v1/images/generations"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer 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"}
        
        url_list = []

        for scene in text:
            data = {"prompt": scene, "n": 4, "size": "1024x1024"}
            images = requests.post(url, json = data, headers = headers)
            print(images)
            returned = images.json()
            print(returned)
            output_url = returned['data'][0]['url']
            url_list.append(output_url)
        #file_paths = dalle.download(images)
        return url_list

    @classmethod
    def textProcessing(cls, text):
        #very basic processing
        nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        doc = nlp(text)

        final_proc_strings = []

        for sentence in doc.sentences:
            cur_string = []
            for word in sentence.words:
                if word.upos not in set(cls.pos_exclude):
                    cur_string.append(word.text)
            cur_string = ' '.join(cur_string)
            final_proc_strings.append(cur_string)

        return final_proc_strings

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
        #return cls.imageGeneration(processed_text)
        return cls.imageGeneration(processed_text, input_style)

if __name__ == '__main__':
    print(imageGenerator.main('a blue car going really fast', 'monet'))
    print(imageGenerator.main('Using the following context: "the snake George is big and purple" Generate an image based on the following sentence: "George ate a mouse"', 'picture book'))
