from flask import Flask, request, render_template
import requests

app = Flask(__name__)

my_api = 'YOUR_API_KEY'
def get_news(x):
    url = f'https://newsapi.org/v2/everything?q={x}&from=2023-05-27&sortBy=publishedAt&apiKey={my_api}'
    # https://newsapi.org/v2/everything?q={x}&from=2023-05-27&sortBy=publishedAt&apiKey=ec1dc33f73174c69bfcb164a64e8c2ee
    response = requests.get(url)
    news_data = response.json()
    results = news_data.get('totalResults')

    articles = news_data.get('articles')
    return articles, results

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        news = request.form['news']
        articles, results = get_news(news)
        return render_template('news.html', news=news, articles=articles, results=results)
    return render_template('index.html')


app.run(debug=True)
