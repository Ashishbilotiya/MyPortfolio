from flask import render_template,Blueprint
import requests

# API endpoint for top books
URL = "https://bookrecommenderapi-k78q.onrender.com/famous_books"

# Blueprint for top books routes
top_books_page = Blueprint("top_books",__name__)

# function to fetch top books data from the API
def get_data():
    try :
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e :
        print("Error in fetching data from API:", e)
        return None


# route for top books page
@top_books_page.route("/")
def show():
    book_title: list = None
    author: list = None
    image: list = None
    votes: list = None
    rating: list = None
    try :
        response = get_data()
        if response is not None:
            book_title = response["top_books"]["book_title"]
            author = response["top_books"]["author"]
            image = response["top_books"]["image"]
            votes = response["top_books"][ "votes"]
            rating = response["top_books"]["rating"]
            return render_template("book/TopBooks.html",
                           book_title=book_title,
                           author=author,
                           image=image,
                           votes=votes,
                           rating=rating,
                           )
    except Exception as e :
        print("Error in fetching top books data:", e)
    
    
