class Pokemon:
    """Represents a Pokemon with basic stats"""
    
    def __init__(self, name, pokemon_id, hp, attack, sprite_url, pokemon_type):
        self.name = name
        self.id = pokemon_id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.type = pokemon_type
    
    def info(self):
        """Print the Pokemon's information"""
        print(f"{self.name} (ID: {self.id})")
        print(f"   HP: {self.hp}")
        print(f"   Attack: {self.attack}")
        print(f"   Type: {self.type}")
        print(f"   Sprite: {self.sprite_url}")