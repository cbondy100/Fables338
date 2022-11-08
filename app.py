from flask import Flask, request, render_template
#from pipeline_demo import imageGenerator

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    result = request.form['storyinput']
    input_string = ''
    input_style = ''
    #imageGenerator.main(input_string, input_style)
    return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)