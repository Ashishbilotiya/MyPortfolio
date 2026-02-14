import requests
from flask import render_template ,request ,Blueprint
from models.load_models import load_books_titles

# API endpoint for book recommendations
BASE_URL = "https://bookrecommenderapi-k78q.onrender.com/recommend_books/"

# Blueprint for book recommender routes
book_page = Blueprint("BookRecommender",__name__)

# function to fetch book recommendations from the API
def get_data(book_name):
    try :
        URL = f"{BASE_URL}{book_name}"
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e :
        print("Error in fetching data from API:", e)
        return None

# route for book recommender page
@book_page.route("/",methods=["POST","GET"])
def book_recommender_page():
    book_titles : list = None
    try :
        book_titles = load_books_titles()
    except Exception as e :
        print("Error in fetching book titles:", e)
    success_code  =-1
    if request.method == "POST" :
        user_input = str(request.form.get("user_input"))
        if user_input :
            try:
                response = get_data(user_input)
                if response is None:
                    success_code = 0
                    return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles,user_input=user_input)
                data = response["recommendations"]
                success_code=1
                return render_template("book/BookRecommender.html",success=success_code,data=data,book_titles=book_titles,user_input=user_input)
            except:
                success_code=0
                return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles)
    return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles)
