#change the ending/beg coords

import json

stuff = [
    {
        "id": 1,
        "number_cars": 0,
        "actual_direction": True,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 0,
        "ending_coords_x": 0,
        "ending_coords_y": 500,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 2,
        "number_cars": 50,
        "actual_direction": False,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 0,
        "ending_coords_x": 0,
        "ending_coords_y": 500,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 3,
        "number_cars": 0,
        "actual_direction": True,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 500,
        "ending_coords_x": 500,
        "ending_coords_y": 1000,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 4,
        "number_cars": 38,
        "actual_direction": False,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 500,
        "ending_coords_x": 0,
        "ending_coords_y": 1000,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 5,
        "number_cars": 0,
        "actual_direction": True,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 1000,
        "ending_coords_x": 0,
        "ending_coords_y": 1500,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 6,
        "number_cars": 0,
        "actual_direction": False,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 1000,
        "ending_coords_x": 0,
        "ending_coords_y": 1500,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 7,
        "number_cars": 0,
        "actual_direction": True,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 1500,
        "ending_coords_x": 0,
        "ending_coords_y": 1700,
        "street": {
            "name": "14",
            "id": 1
        }
    },
    {
        "id": 8,
        "number_cars": 0,
        "actual_direction": False,
        "n_accident": 0,
        "beggining_coords_x": 0,
        "beggining_coords_y": 1500,
        "ending_coords_x": 0,
        "ending_coords_y": 1700,
        "street": {
            "name": "14",
            "id": 1
        }
    }
]

# f = open("stuff.txt", "w")
# f.write(json.dumps(stuff, indent=4))
# f.close()

f = open("stuff.txt", "r")
stuff = json.loads(f.read())
f.close()

for i in range(len(stuff)-1):
    if (stuff[i]["beggining_coords_x"] == stuff[i+1]["beggining_coords_x"]
        and stuff[i]["beggining_coords_y"] == stuff[i+1]["beggining_coords_y"]
        and stuff[i]["ending_coords_x"] == stuff[i+1]["ending_coords_x"]
        and stuff[i]["ending_coords_y"] == stuff[i+1]["ending_coords_y"]):

        assert(not stuff[i+1]["actual_direction"])

        tmpx = stuff[i+1]["ending_coords_x"]
        tmpy = stuff[i+1]["ending_coords_y"]

        stuff[i+1]["ending_coords_x"] = stuff[i+1]["beggining_coords_x"]
        stuff[i+1]["ending_coords_y"] = stuff[i+1]["beggining_coords_y"] 
        stuff[i+1]["beggining_coords_x"] = tmpx 
        stuff[i+1]["beggining_coords_y"] = tmpy 
        
        print(i)
        i+=1

f = open("stuff.txt", "w")
f.write(json.dumps(stuff, indent=4))
f.close()

