from flask import render_template ,request ,Blueprint
import requests
from models.load_models import load_movies_titles

# API endpoint for movie recommendations
BASE_URL= "https://movierecommenderapi-5sxp.onrender.com/recommend_movies/"

# Blueprint for movie recommender routes
movie_page = Blueprint("MovieRecommender",__name__)

# function to fetch movie recommendations from the API
def get_data(movie_name):
    try :
        URL = f"{BASE_URL}{movie_name}"
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e :
        print("Error in fetching data from API:", e)
        return None

# route for movie recommender page
@movie_page.route("/",methods=["POST","GET"])
def movie_recommender_page():
    titles : list  = None
    try :
        titles = load_movies_titles()
    except Exception as e :
        print("Error in fetching movie titles:", e)
    success_code : int = -1
    if request.method == "POST" :
        user_input : str = str(request.form.get("user_input"))
        if user_input :
            try :
                response = get_data(user_input)
                if response is None:
                    success_code = 0
                    return render_template("movie/MovieRecommender.html",success=success_code,titles=titles,user_input=user_input)
                success_code= 1
                return render_template("movie/MovieRecommender.html",success=success_code,data = response["recommendations"],titles=titles,user_input=user_input)
            except:
                success_code = 0
                return render_template("movie/MovieRecommender.html",success = success_code,titles=titles)
    return render_template("movie/MovieRecommender.html",success=success_code,titles=titles)


