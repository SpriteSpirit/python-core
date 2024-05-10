from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)  # Используйте __name__, чтобы обозначить текущий модуль
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    dest_lang = request.form['dest_lang']
    translation = translator.translate(text, dest=dest_lang).text
    return render_template('result.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
