from flask import Flask, render_template

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()