from flask import Flask, render_template, redirect, request, url_for, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/movie', methods=['POST'])
def movie():
    title = request.form['title']
    year = request.form['year']
    lead_actor = request.form['lead-actor']

    create_movie(title, year, lead_actor)

    return redirect(url_for('movies'), )

@app.route('/movies')
def movies():
    movies = fetch_movies()
    return jsonify(movies)

@app.route('/search')
def search():
    search_term = request.args.get('search', '')

    movies = find_by_title(search_term)
    return jsonify(movies)

def create_movie(title, year, lead_actor):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('INSERT INTO movies VALUES (?, ?, ?)', (title, year, lead_actor))
    conn.commit()
    conn.close()

def fetch_movies(title=None):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('SELECT * FROM movies')
    result = c.fetchall()
    movies = [{'title': movie[0], 'year': movie[1], 'lead-actor': movie[2]} for movie in result]
    conn.close()
    return movies

def find_by_title(title):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('SELECT * FROM movies WHERE title = ?', (title,))
    result = c.fetchall()
    movies = [{'title': movie[0], 'year': movie[1], 'lead-actor': movie[2]} for movie in result]
    conn.close()
    return movies
