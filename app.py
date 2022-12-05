from flask import Flask, render_template, request
from src.story_class import Story
import os
from run_completion import openai_engine

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        input_string = result['storyinput']
        input_title = result['titleinput']
        input_style = result['style_chosen']
        input_string = input_string.replace('\n', '')
        api_key = os.getenv("OPENAI_API_KEY")
        gpt_output = openai_engine.run_completion(api_key, input_string)

        images = []

        for sentence in gpt_output.splitlines():
            images.append(openai_engine.generate_image(api_key, sentence))
            
        #story_obj = Story(input_string, input_title, input_style)

        #use for html / css edits
        #raw_sentences = input_string.split(". ")
        #scene_data = []
        #for s in raw_sentences:
        #    scene_data.append(["https://readtheforum.org/wp-content/uploads/2018/10/Screen-Shot-2018-10-01-at-7.17.51-PM.png", s])

        scene_data = []
        for scene in story_obj.scenes:
            print(scene.image)
            scene_data.append([scene.image, scene.raw_sentence])

        all_data={
            "title":input_title,
            "style": input_style,
            "scene_list": scene_data
            }
        
        return render_template('result.html', data=all_data)

if __name__ == '__main__':
    app.run(debug=True)