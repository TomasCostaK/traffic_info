from random import randint
import json
import unicodedata

class Street():
    def __init__(self, name, beginning, ending, length):
        self.name = unicodedata.normalize('NFD',name).encode('ascii','ignore').decode('utf-8')  #remove accents
        self.beginning = beginning
        self.ending = ending
        self.length = length
    
    def getDict(self):
        return {
                    "name": self.name,
                    "beginning_coords": self.beginning,
                    "ending_coords": self.ending,
                    "length": self.length
                }

class Trecho():
    def __init__(self, street, beginning, direction):
        self.street = unicodedata.normalize('NFD',street).encode('ascii','ignore').decode('utf-8')  #remove accents
        self.beginning = beginning
        self.num_cars = 0
        self.num_acc = 0
        self.direction = direction

    def getDict(self):
        return {
                    "street": self.street,
                    "beginning_coords": self.beginning,
                    "number_cars": self.num_cars,
                    "accident": self.num_acc,
                    "actual_direction": self.direction
                }

squareX = 5
squareY = 5

stNames = open("streetName.csv", "r")
streets = []

for i in range(squareX+1):
    vertical_street_beginning = (i, 0)
    vertical_street_ending = (i, squareY)
    horizontal_street_beginning = (0,i)
    horizontal_street_ending = (squareX,i)
    vertical_stName = stNames.readline().split(",")[0]
    horizontal_stName = stNames.readline().split(",")[0]
    streets.append(Street(vertical_stName, vertical_street_beginning, vertical_street_ending, 5).getDict())
    streets.append(Street(horizontal_stName, horizontal_street_beginning, horizontal_street_ending, 5).getDict())

data = {"Streets" : streets}
# print(streets)

trechos = []

for street in streets:
    street_name = street["name"]
    beg_street = street["beginning_coords"]
    end_street = street["ending_coords"]
    for i in range(5):
        ## Check if it"s vertical or horizontal
        if beg_street[0]==end_street[0]:
            beg_trecho_lr = (beg_street[0], i)
            beg_trecho_rl = (beg_street[0], squareY-i)
            trechos.append(Trecho(street_name, beg_trecho_lr, True).getDict())
            trechos.append(Trecho(street_name, beg_trecho_rl, False).getDict())
        else:
            beg_trecho_ud = (i, beg_street[1])
            beg_trecho_du = (squareX-i, beg_street[1])
            trechos.append(Trecho(street_name, beg_trecho_ud, True).getDict())
            trechos.append(Trecho(street_name, beg_trecho_du, False).getDict())

data['Trechos'] = trechos

print(json.dumps(data, indent=4))
f = open("very_primordial_data.txt", "w")
f.write(json.dumps(data, indent=4))
f.close()

"""
for i in range(1):
    stName = stNames.readline().split(",")[0]
    ## Random for vertical vs horizontal streets
    is_horizontal = randint(0,1) == 1
    common_var = 0
    diff_var1 = 0
    diff_var2 = 0
    if is_horizontal:
        common_var = randint(0, squareY)
        diff_var1 = randint(0, squareY)
        diff_var2 = randint(0, squareY)
        begin, end = sorted([x1, x2])
        print(f"Street {stName}, starts at {(begin, common_y)} ends at {(end, common_y)}")
    else:
        common_x = randint(0, squareY)
        y1 = randint(0, squareX)
        y2 = randint(0, squareX)
        begin, end = sorted([y1, y2])
        print(f"Street {stName}, starts at {(begin, y1)} ends at {(end, y2)}")
    #st = Street(stName, (0,1), squareX, 20)"""

