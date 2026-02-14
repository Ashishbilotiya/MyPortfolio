import os
import json

# Base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# file paths for movie and book titles
MOVIE_TITLES_FILE_PATH= os.path.join(BASE_DIR, "movie_titles.json")
BOOK_TITLES_FILE_PATH = os.path.join(BASE_DIR, "book_titles.json")

# functions to load movie and book titles from the respective JSON files
def load_movies_titles()-> list:
    movies : list = None
    if movies is None:
        with open(MOVIE_TITLES_FILE_PATH, "r") as f:
            movies = json.load(f)
    return movies["titles"]

def load_books_titles()-> list:
    books : list = None
    if books is None:
        with open(BOOK_TITLES_FILE_PATH, "r") as f:
            books = json.load(f)
    return books["titles"]


