from ..request import get_news,get_articles
from flask import render_template,request,redirect,url_for
import main
#Views
@main.route('/')
def index():
    current_news = get_news()
    print(current_news)
    title = "Welcome to my news hub"
    return render_template('index.html', title= title, current_news = current_news )
@main.route("/news/<news_id>")
def articles(news_id): #codecamp 
    articles = get_articles(news_id)
    print(articles)
    title = f'{news_id}'
    return render_template("articles.html", articles = articles, title = title)

