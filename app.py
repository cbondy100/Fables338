from flask import Flask, render_template
from pipeline_demo import imageGenerator

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    input_string = ''
    input_style = ''
    imageGenerator.main(input_string, input_style)

if __name__ == '__main__':
    app.run()