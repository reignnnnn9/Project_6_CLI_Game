import requests

def get_pokemon_data(pokemon_identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon = {
            'name': data['name'].title(),
            'pokemon_id': data['id'],
            'hp': data['stats'][0]['base_stat'],
            'attack': data['stats'][1]['base_stat'],
            'sprite_url': data['sprites']['front_default'],
            'pokemon_type': data['types'][0]['type']['name']
        }
        return pokemon
    else:
        print(f"Error fetching data for pokemon {pokemon_identifier}")




#==============================================================================
    """
    Get Pokemon data from PokeAPI and extract game-relevant information  
    Args:
        pokemon_identifier: Pokemon name (str) or ID (int)
    Returns:
        dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
        None: if Pokemon not found or error occurred
    """
    # YOUR CODE HERE
    # 1. Make a GET request to https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}
    # 2. Check if the request was successful (status code 200)
    # 3. Parse the JSON response
    # 4. Extract: name, id, hp stat, attack stat, front_default sprite, primary type
    # 5. Return as a dictionary
    # 6. Handle errors gracefully (return None if something goes wrong)

# Test your function with these Pokemon
# test_pokemon = ["bulbasaur", "charmander", "squirtle", 25, "pikachu"]

# for pokemon in test_pokemon:
#     print(f"\n--- Testing {pokemon} ---")
#     data = get_pokemon_data(pokemon)
#     if data:
#         print(f"Found: {data['name']} (ID: {data['id']})")
#         print(f"   HP: {data['hp']}, Attack: {data['attack']}")
#         print(f"   Type: {data['type']}")
#         print(f"   Sprite: {data['sprite_url']}")
#     else:
#         print(f"Failed to get data for {pokemon}")