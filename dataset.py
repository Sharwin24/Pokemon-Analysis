import pandas as pd
import numpy as np


class PokemonDataSet:
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(path)
        # print(self.data.head())

    def get_pokemon(self, pokemon_name):
        return self.data[self.data['Name'] == pokemon_name]


PokeDex = PokemonDataSet('Pokemon.csv')
# print(PokeDex.get_pokemon('Pikachu'))
