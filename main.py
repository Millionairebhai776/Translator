pip install googletrans

from googletrans import Translator

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def index():

    if request.method == 'POST':

        text = request.form['text']

        translator = Translator(dest='ml')

        result = translator.translate(text).text

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == "__main__":

    app.run()

