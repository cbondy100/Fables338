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
        input_string = result['storyinput']
        input_style = 'comic'
        file_to_display = imageGenerator.main(input_string, input_style)
        return render_template('result.html', result = file_to_display)

if __name__ == '__main__':
    app.run()