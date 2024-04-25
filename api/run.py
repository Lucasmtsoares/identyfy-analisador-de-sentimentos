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

@app.route("/identificador-de-sentimentos", methods=['GET', 'POST'])
def identificar_sentimento():
    if request.method =='POST':
        request_ = request.form['date']

        sentiment = Sentiment(request_)
        message = sentiment.get()
        instance = sentiment.instance()
        response = sentiment.execute()
        return render_template('identyfy.html', response=response, message=message, instance=instance)
    return render_template("identyfy.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/o-que-e-nltk")
def explane_nltk():
    return render_template("explane_nltk.html")

@app.route("/quem-sou-eu")
def my_description():
    
    return render_template("mydescription.html")




if __name__=="__main__":
    #port = int(os.getenv('PORT'), '5000')
    app.run()