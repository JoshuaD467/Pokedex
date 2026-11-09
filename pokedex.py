import json

pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

for i in range(pokedex):
    print["name"]