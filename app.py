from flask import Flask, render_template, request
from src.story_class import Story
import os

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
        story_obj = Story(input_string, input_title, input_style)

        scene_data = []
        for scene in story_obj.scenes:
            scene_data.append([scene.image, scene.raw_sentence])

        all_data={
            "title":input_title,
            "style": input_style,
            "scene_list": scene_data
            }
        
        return render_template('result.html', data=all_data)

if __name__ == '__main__':
    app.run(debug=True)