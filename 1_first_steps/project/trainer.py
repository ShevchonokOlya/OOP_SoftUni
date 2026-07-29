from project_0.pokemon import Pokemon


class Trainer(object):
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [pok.name for pok in self.pokemons]
        if pokemon_name not in pokemon_names:
            return "Pokemon is not caught"
        else:
            for pok in self.pokemons:
                if pok.name == pokemon_name:
                    self.pokemons.remove(pok)
                    break
            return f"You have released {pokemon_name}"

    def trainer_data(self):
        result_string = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pok in self.pokemons:
            result_string += f'- {pok.pokemon_details()}\n'
        return result_string.strip()

