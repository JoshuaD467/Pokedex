import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

for pokemon in data:
    print(pokemon['name']['english'])

def pokemon_printer():
    language = input("What language do you want to print? english/french/chinese/japanese: ").lower()
    id = int(input("What pokemon would you like to find the name of? Print the id: "))
    print(data[id - 1]['name'][language])
pokemon_printer()

def pokemon_searcher():
    type = input('What type of pokemon would you lie to find? : ').capitalize()
    for pokemon in data:
        if type in pokemon['type']:
            print(pokemon['name']['english'])
pokemon_searcher()

#def pokemon_finder():
    #search = input("What pokemon would you like to find?: ")

#pokemon_finder()







# Create a function that will take the data from the JSON file and you will iterate through the list of 
# pokemon and print each pokemons name.
# Add a language choice feature and print the pokemons name based on the user input.
# Develop a function that creates a new list of pokemon based on the type the user searched for. 
# If no pokemon was found of that type inform the user.
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, 
#Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, 
#show all fire and flying moves. HINT import the moves.json file too!
