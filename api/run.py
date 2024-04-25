from flask import Flask
from api import app
import os
from api import app
from flask import render_template, request
from api.models.analitic_sentiment import Sentiment

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
#essas duas rotas levam a mesma pagina (abaixo). Isso é muito útil
def index():
    return render_template("basic.html")




if __name__=="__main__":
    #port = int(os.getenv('PORT'), '5000')
    app.run()