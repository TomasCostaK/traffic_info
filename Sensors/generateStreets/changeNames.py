import json
import unicodedata

f = open("mapa2.txt", "r")
streets = json.loads(f.read())
f.close()

stNames = open("streetName.csv","r")
for i in range(len(streets)):
    streets[i]["name"] =  unicodedata.normalize('NFD',stNames.readline().split(",")[0]).encode('ascii','ignore').decode('utf-8')  #remove accents

stNames.close()

f = open("mapa2.txt", "w")
f.write(json.dumps(streets, indent=4))
f.close()