import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

def pokemon_printer():
        for pokemon in range(len(data)):
                print(data[pokemon]['name']['english'])

        language = input("What language would you like to print: english, japanese, chinese, or french? : ").lower()
        pokemon_choice = int(input("What pokemon do you want to see the name of? type the id: ")) 

        print(data[pokemon_choice - 1]['name'][language])
pokemon_printer()

def pokemon_searcher():
        types = input("What types of pokemon do you want to find? : ")
        for pokemon in data:
                if types in pokemon['type']:
                        print (pokemon['name']['english'])
                if types != pokemon['type']:
                        types = input("That is not a valid type please try again: ")
                        print(pokemon['name']['english'])
pokemon_searcher()


# Create a function that will take the data from the JSON file and you will iterate through the list of 
# pokemon and print each pokemons name.
# Add a language choice feature and print the pokemons name based on the user input.
# Develop a function that creates a new list of pokemon based on the type the user searched for. 
# If no pokemon was found of that type inform the user.
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, 
#Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, 
#show all fire and flying moves. HINT import the moves.json file too!
