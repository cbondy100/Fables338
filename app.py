from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    text = request.form.get("submit")
    return text

if __name__ == '__main__':
    app.run()