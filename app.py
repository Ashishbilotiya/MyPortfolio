from flask import Flask
from routes.home import home_page
from routes.BookRecommender import book_page
from routes.MovieRecommender import movie_page
from routes.Top_50_Books import top_books_page

app = Flask(__name__)

# Required for flash messages
app.secret_key = "secret_key_123"
# Register Blueprints
app.register_blueprint(blueprint= home_page ,url_prefix=  "/")
app.register_blueprint(blueprint= top_books_page ,url_prefix=  "/Top_Books")
app.register_blueprint(blueprint= book_page ,url_prefix=  "/BookRecommender")
app.register_blueprint(blueprint= movie_page ,url_prefix=  "/MovieRecommender")


if __name__ == "__main__" :
    app.run(host='0.0.0.0',debug=True)
