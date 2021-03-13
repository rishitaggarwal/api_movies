from flask import Flask,jsonify,request
import csv
all_movies = []
with open("movies_2_api.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
liked_movies = []
notLikedMovies = []
didNotWatch = []
app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })
@app.route("/liked-movie",methods = ["POST"])
def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201
@app.route("/unliked-movie",methods = ["POST"])
def unliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    notLikedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201
@app.route("/unwatched-movie",methods = ["POST"])
def unwatched_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    didNotWatch.append(movie)
    return jsonify({
        "status":"success"
    }),201
if __name__ == "__main__":
    app.run()