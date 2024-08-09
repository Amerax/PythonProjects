import requests
import random
import time
from collections import Counter
from animegenres import anime_genres as codes

# Read anime codes from file
file = open('export.txt', 'rt', encoding='UTF-8')
list_of_animes = [int(row.strip()[-5:].lstrip('/')) for row in file]
file.close()

def random_animes(anime_list):
    randomized_list = []
    for _ in range(15):
        randomized_list.append(anime_list[random.randrange(0, len(anime_list))])
    return randomized_list

def fetch_genre(anime_id):
    try:
        url = f'https://api.jikan.moe/v4/anime/{anime_id}'
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        genres = [genre['name'] for genre in data['data']['genres']]
        return genres
    except requests.RequestException as e:
        print(f"Error fetching data for anime code {anime_id}: {e}")
        return []

def fetch_genres(anime_ids):
    all_genres = {}
    for index, anime_id in enumerate(anime_ids):
        genres = fetch_genre(anime_id)
        all_genres[anime_id] = genres
        print(f"Anime code {anime_id} genres: {genres}")
        
        # Delay after every 5 requests
        if (index + 1) % 5 == 0:
            print("Waiting for 5 seconds...")
            time.sleep(5)
    
    return all_genres

def most_genres_found(list_of_genres, n):
    counted_items = Counter(list_of_genres)
    n_common_items = counted_items.most_common(n)
    genres = [item[0] for item in n_common_items]
    return genres


# Generate random anime codes
random_codes = random_animes(list_of_animes)

# Fetch genres for random anime codes
genres = fetch_genres(random_codes)
print("All genres fetched:", genres)

list_of_all_genres_found = [genre for val in genres.values() for genre in val]

popular_genres = most_genres_found(list_of_all_genres_found, 3)


#prev code

def convert_genre_code(genre_list):
    list_of_codes = []
    for genre in list(genre_list):
        upper = str(genre).capitalize()
        list_of_codes.append(codes[upper])
    return list_of_codes


def concat_codes(codes_list):
    return ','.join(map(str, codes_list))
        
    
def request_recs(genre_codes):
    
    genre_codes_str = concat_codes(genre_codes)

    # Define the URL for the Jikan API endpoint for searching anime
    url = "https://api.jikan.moe/v4/anime"

    # Define the parameters for searching anime with the romance genre
    params = {
        "genres": genre_codes_str,  # Romance genre ID should be a string
        "order_by": "score",  # Order results by score (you can change this to popularity, title, etc.)
        "sort": "desc",  # Sort results in descending order
        "limit": 5  # Increase limit to 50 (maximum allowed by Jikan)
    }

    try:
        # Send the GET request to the API with the specified parameters
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()
        
        # Extract and print relevant information
        anime_list = data.get('data', [])
        
        if anime_list:
            print("Top Animes With Your Genres:")
            for anime in anime_list:
                print(f"Title: {anime.get('title')}")
                print(f"Score: {anime.get('score')}")
                print(f"URL: {anime.get('url')}")
                print()
        else:
            print("No anime found with the specified criteria.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

request_recs(convert_genre_code(popular_genres))