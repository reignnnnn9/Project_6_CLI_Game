from pokemon_class import Pokemon
from pokemon_api import get_pokemon_data

class Player:
    """Represents a player with a collection of Pokemon"""
    def __init__(self, name):
        self.name = name
        self.collection = []  # List of Pokemon objects
    
    def add_pokemon(self, pokemon):
        """Add a Pokemon to the collection (max 6 Pokemon)"""
        if len(self.collection) < 6:
            self.collection.append(pokemon)
            print(f"\n{pokemon.name} added to {self.name}'s collection!")
            return True
        else:
            print(f"Collection is full! Can't add {pokemon.name}")
            return False
    
    def remove_pokemon(self, index):
        """Remove a Pokemon from the collection by index"""
        if not self.collection:
            print("You have no Pokemon to remove.")
            return None
        
        if 0 <= index < len(self.collection): # 1. Check if the index is valid (between 0 and 5, and less than collection size)
            removed = self.collection.pop(index) # 2. If valid, remove the Pokemon at that index using pop()
            print(f"\n{removed.name} released successfully") # 3. Print a message about releasing the Pokemon
            return removed                                   # 4. Return the removed Pokemon
        else:
            print("Invalid selection")
            return None # 5. If invalid index, return None
    
    def show_collection(self):
        """Display all Pokemon from the collection """
        if not self.collection:
            print(f"{self.name} has no pokemon to remove.")
            return None
        
        print(f"\n{self.name}'s Pokemon Collection ({len(self.collection)} total)")
        for i, pokemon in enumerate(self.collection):
            print(f"{i + 1}. {pokemon.name} (ID: {pokemon.id} - {pokemon.type} type)")

# Test the Player class
# def test_player_class():
#     player = Player("Ash")
    
#     # Create some Pokemon
#     # pikachu = Pokemon("Pikachu", 25, 90, 55, "url", "electric")
#     # charizard = Pokemon("Charizard", 6, 158, 84, "url", "fire")
#     pikachu_data = get_pokemon_data('pikachu')
#     charizard_data = get_pokemon_data('charizard')
    
#     pikachu = Pokemon(**pikachu_data)
#     charizard = Pokemon(**charizard_data)
    
#     # Add to collection
#     player.add_pokemon(pikachu)
#     player.add_pokemon(charizard)
    
#     # Show collection
#     player.show_collection()

#     player.remove_pokemon(0)
#     player.show_collection()


#test_player_class()