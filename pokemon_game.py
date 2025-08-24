import random
from player_class import Player
from pokemon_class import Pokemon
from pokemon_api import get_pokemon_data

class PokemonGame:
    """Main game class that manages the entire game"""

    def __init__(self):
        self.player = None
        self.wild_pokemon = None

    def start_game(self):
        """Initialize the game and get player info"""
        print("====== Welcome to Pokemon CLI Adventure ======")
        player_name = input("\nWhat is your name trainer? ")
        self.player = Player(player_name)

        print(f"\nHello {player_name}! Time to choose your starter Pokemon!")
        self.choose_starter()

    def choose_starter(self):
        """Let player choose their starting Pokemon"""

        starters = {
            "1": 'Bulbasaur',
            "2": 'Charmander',
            "3": 'Mudkip'
        }

        print("\nChoose your starter Pokemon:")
        print("1. Bulbasaur (Grass Type)")
        print("1. Charmander (Fire Type)")
        print("1. Mudkip (Water Type)")

        while True:
            choice = input("Enter 1, 2, or 3: ")
            if choice in starters:
                starter_name = starters[choice]
                starter_data = get_pokemon_data(starter_name)

                if starter_data:
                    starter = Pokemon(**starter_data)
                    self.player.add_pokemon(starter)
                    print(f"You chose {starter_name}! Great Choice!")
                    break
                else:
                    print("Error loading Pokemon data. Please try again")
            else:
                print("Please enter a valid selection. 1, 2, or 3")

    def show_main_menu(self):
        print(f"\n=== Pokemon Adventure - {self.player.name} ===")
        print("1. Go Hunting (find wild Pokemon)")

    def main_game_loop(self):
        while True:
            self.show_main_menu()
            choice = input("\nWhat would you like to do? ")

            if choice == '1':
                self.go_hunting()
            elif choice == '2':
                self.player.show_collection()
            elif choice == '3':
                self.remove_pokemon_menu()
            elif choice == '4':
                print(f"Thanks for playing, {self.player.name}! Goodbye")

    def go_hunting(self):
        random_id = random.random(1-151)
        wild_pokemon = get_pokemon_data(random_id)
        self.wild_pokemon = wild_pokemon

        print(f"A wild {wild_pokemon.name} appeared!")
        print(wild_pokemon)
        choice = int(input("""
                    1. Try to catch
                    2. Flee
                    """))
        if choice == '1':
            self.try_catch_pokemon(self.wild_pokemon)
        elif choice == '2':
            self.wild_pokemon = None
            print("Ran away")         
        else:
            print("Invalid option, please enter 1 or 2")

        # YOUR CODE HERE - Part 1: Generate Wild Pokemon
        # 1. Generate a random Pokemon ID between 1 and 151
        # 2. Use get_pokemon_data() to fetch the Pokemon info
        # 3. Create a Pokemon object from the data
        # 4. Store it in self.wild_pokemon
        
        # YOUR CODE HERE - Part 2: Encounter Menu
        # Display: "A wild {pokemon_name} appeared!"
        # Show the Pokemon's info using pokemon.info()
        # Show options: "1. Try to catch  2. Flee"
        # Get user input and call appropriate method

        # Use random.randint(1, 151) to generate random Pokemon IDs
        # Check if get_pokemon_data() returns valid data before creating Pokemon object
        # Handle the case where API request fails gracefully
        # Use input() to get user choice and convert to integer
        # Call try_catch_pokemon() or handle fleeing based on user input

    def try_catch_pokemon(self, wild_pokemon):
        catch_rate = 0.25
        random_num = random.random(0-1)
        print("You throw a Pokeball...")
        print(f"Catch rate: {random_num:.0%}")
        if random_num >= catch_rate:
            print(f"Gotcha! {self.wild_pokemon.name} was caught!")
            self.player.add_pokemon(wild_pokemon)
            print(f"{self.wild_pokemon.name} added to {self.player.name}'s collection!")
            self.wild_pokemon = None
        else:
            print(f"{self.wild_pokemon.name} broke out of the Pokeball!")

        # 1. Calculate catch probability (base rate: 50%)
        # 2. Generate random number (0-1)
        # 3. If successful:
        #    - Add Pokemon to player's collection
        #    - Clear wild_pokemon
        #    - Show success message
        # 4. If failed:
        #    - Show failure message
        # 5. Show the catch probability for debugging

        # Base catch rate is 25% (0.25)
        # Use random.random() to generate a number between 0 and 1
        # If random number ≤ catch rate, the catch is successful
        # Remember to check if player's collection is full before adding Pokemon
        # Clear self.wild_pokemon after successful catch or flee

    def remove_pokemon_menu(self):
        self.player.show_collection()
        choice = int(input("Which Pokemon would you like to remove? Choose 1-6"))
        remove = choice - 1
        if remove <= len(Player.collection):
            self.player.remove_pokemon(remove)
        else:
            print("Enter a valid number 1-6")

        # YOUR CODE HERE
        # 1. Show current collection using player.show_collection()
        # 2. Get user input for which Pokemon to remove
        #hint: make sure to convert input number to a proper index (1 -> 0)
        # 3. Call player.remove_pokemon() with the index
        # 4. Handle invalid input gracefully

        # Show the collection first so user knows what's available
        # Get user input for which Pokemon to remove (1-based indexing)
        # Convert to 0-based index for the remove_pokemon() method
        # Handle invalid input (non-numbers, out-of-range numbers)

def create_game():
    game = PokemonGame
    game.start_game()
    game.main_game_loop()

create_game()