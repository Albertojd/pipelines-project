#Sacando la primera generación de Pokémon 

from SRC.MainFunctions import world



def main():
    countries = input('''
        Inserta el país del que quieres obtener información
        ''')
    print(world(countries))
