import requests

MOVIES_URL = "https://raw.githubusercontent.com/mdnazmul582378/Link-Bot/main/dd.json"
cached_movies = []

def fetch_movies():
    global cached_movies
    response = requests.get(MOVIES_URL)
    if response.status_code == 200:
        cached_movies = response.json()

def get_movie_by_id(movie_id):
    return next((m for m in cached_movies if m["id"] == movie_id), None)

def is_poster_valid(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False
