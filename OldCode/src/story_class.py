import stanza
import requests

class Story:
    # pass in text, title
    # get out a story object, which is composed of a sequence of scenes
    def __init__(self, raw_story_text, raw_story_title, style):
        self.title = raw_story_title
        self.raw_story_text = raw_story_text
        self.style = style + ' style'
        self.nlp_model = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        self.processed_text = self.nlp_model(raw_story_text)
        #self.POS_to_exclude = set(['ADV', 'DET', 'INTJ', 'PART', 'PUNCT', 'SYM', 'X'])
        self.last_noun_subject = None
        self.noun_map = {}
        self.build_scenes()

    def build_scenes(self):
        self.scenes = []
        raw_sentences = self.raw_story_text.split('.')
        len_raw = len(raw_sentences)
        for i in range(0, len_raw):
            raw_sentence = raw_sentences[i]
            if raw_sentence:
                processed_sentence = self.processed_text.sentences[i]
                scene = Scene(raw_sentence, processed_sentence, self)
                self.scenes.append(scene)

    def get_image(self, scene):
        return scene.image       
        
class Scene:

    def __init__(self, raw_sentence, processed_sentence, story_obj):
        self.story_obj = story_obj
        self.raw_sentence = raw_sentence + '.'
        self.processed_sentence = processed_sentence
        self.build_words()

    def build_words(self):
        self.output_sentence = ''

        for word in self.processed_sentence.words:
            output_word = word.text
            word_upos = word.upos
            word_deprel = word.deprel
            pointed_word_id = word.head
            pointed_word = self.processed_sentence.words[pointed_word_id-1]
            if pointed_word.upos == 'NOUN' and pointed_word_id != 0:
                self.story_obj.noun_map[pointed_word.text] = self.story_obj.noun_map.get(pointed_word.text, '') + ' ' + output_word

            if word_deprel == 'nsubj':
                if word_upos == 'PRON' and self.story_obj.last_noun_subject is not None:
                    #keyError when pronoun is present
                    output_word = self.story_obj.noun_map[self.story_obj.last_noun_subject] + ' ' + self.story_obj.last_noun_subject
                else:
                    self.story_obj.last_noun_subject = output_word

            #if word_upos not in self.story_obj.POS_to_exclude:
            if word.text != '.':
                self.output_sentence = self.output_sentence + ' ' + output_word
        
        self.output_sentence = self.output_sentence + self.story_obj.style

        self.image = self.generateImage(self.output_sentence)

    def generateImage(self, text):
        url = "https://api.openai.com/v1/images/generations"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer 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"}
        data = {"prompt": text, "n": 4, "size": "1024x1024"}
        images = requests.post(url, json = data, headers = headers)
        returned = images.json()
        return returned['data'][0]['url']

if __name__ == '__main__':
    input_story = 'The green fat dog is wet. He is the worst.'
    test = Story(input_story, 'title', 'comic')
    print('The test story is (' + test.raw_story_text + ')\n')
    print('The outputed sentences to be passed to DALLE are:\n')
    for scene in test.scenes:
        print(scene.output_sentence)

