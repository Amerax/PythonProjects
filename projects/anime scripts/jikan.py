import requests
from animegenres import anime_genres as codes

chosen_genres = []

while True:
    chosen_genres.append(input('Enter a genre: '))
    choice = input('Want to add more? ')
    if  choice.strip().lower() == 'yes':
        pass
    else: 
        break

def convert_genre_code(genre_list):
    list_of_codes = []
    for genre in genre_list:
        upper = genre.capitalize()
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

request_recs(convert_genre_code(chosen_genres))
        

