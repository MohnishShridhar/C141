from flask import Flask, jsonify, request
from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demographic_filtering import output
from content_filtering import get_recomendations

app=Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data={
        "original_title":all_movies[0][8],
        "poster_link":all_movies[0][27],
        "release_date":all_movies[0][13] or "N/A",
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9]
    }
    return jsonify({
        "data":movie_data,
        "status":"success"
    })
    
@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status":"success"
    }),201

if __name__ =="__main__":
    app.run()