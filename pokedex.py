import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

for pokemon in range(len(data)):
    print(data[pokemon]['name']['english'])

language = input("What language would you like to print: english, japanese, chinese, or french? : ")
pokemon_choice = int(input("What pokemon do you want to see the name of? type the id: ")) 

if language == "english":
        print (data[pokemon_choice]['name']['english'])
if language == "japanese":
        print (data[pokemon_choice]['name']['japanese'])
if language == "chinese":
        print (data[pokemon_choice]['name']['chinese'])
if language == "french":
        print (data[pokemon_choice]['name']['french'])
