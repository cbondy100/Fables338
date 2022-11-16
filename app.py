from flask import Flask, render_template, request
from src.pipeline_demo import imageGenerator
import os

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        input_title = result['titleinput']
        input_string = result['storyinput']
        input_style = result['style_chosen'] + " style"

        sen_list = input_string.split(". ")
        print(sen_list)

        images_list = imageGenerator.main(input_string, input_style)
        
        
        scene_data = []
        for index in range(len(sen_list)):
            scene_data.append([images_list[index], sen_list[index]])

        all_data={
            "title":input_title,
            "style": input_style,
            "scene_list":scene_data
            }
        
        #file_to_display = imageGenerator.main(input_string, input_style)
        return render_template('result.html', data=all_data)

if __name__ == '__main__':
    app.run(debug=True)