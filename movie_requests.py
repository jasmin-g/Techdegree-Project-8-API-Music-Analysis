import requests
import csv
import pandas as pd

from key import api_key

oscar_winners = pd.read_csv('oscar_winners.csv')
header = ['title', 'runtime(min)', 'genre', 'award_wins', 'award_nominations', 'box_office(USD)']
movies = []

for id in oscar_winners['IMDB']:
    all_movies = []
    r = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&i={id}').json()
    all_movies.append(r['Title'])
    all_movies.append(int(r['Runtime'].split()[0]))
    all_movies.append(r['Genre'])
    all_movies.append(int(r['Awards'].split()[3]))
    all_movies.append(int(r['Awards'].split()[6]))
    all_movies.append(int(r['BoxOffice'][1:].replace(',', '')))
    movies.append(all_movies)

with open('movies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for movie in movies:
        writer.writerow(movie)