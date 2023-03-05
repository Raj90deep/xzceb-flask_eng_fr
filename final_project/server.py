from machinetranslation import translator
from flask import Flask, render_template, request
import json

from machinetranslation import translator

app = Flask(__name__)

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text=translator.englishToFrench(textToTranslate)
    return ("Translated text to French: <b>" + translated_text + "</b>")

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text=translator.frenchToEnglish(textToTranslate)
    return ("Translated text to English: <b>" + translated_text +"</b>")

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

app.run(host="0.0.0.0", port=8080)
