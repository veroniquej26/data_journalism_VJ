import json


f1 = open("data/data_original_2.csv", "r")
lines = f1.readlines()
#yr_keys = lines[1].strip().split(",")

year_list = []
year_list = lines[1].split(",")[1:]
#print(yr_keys)

dictionary = {}

bronx = lines[2].split(",")[1:]
brooklyn = lines[3].split(",")[1:]
manhattan = lines[4].split(",")[1:]
queens = lines[5].split(",")[1:]
staten_island = lines[6].split(",")[1:]
#other = lines[7].split(",")[1:]

bronx_dict = {}
brooklyn_dict = {}
manhattan_dict = {}
queens_dict = {}
staten_island_dict = {}
#other_dict = {}

for num in range(0,9):
    year = year_list[num]
    bronx_dict[2015+num] = bronx[num]
    brooklyn_dict[2015+num] = brooklyn[num]
    manhattan_dict[2015+num] = manhattan[num]
    queens_dict[2015+num] = queens[num]
    staten_island_dict[2015+num] = staten_island[num]
    #other_dict[year] = other[num]


dictionary = {
    "Bronx":bronx_dict,
    "Brooklyn":brooklyn_dict,
    "Manhattan":manhattan_dict,
    "Queens":queens_dict,
    "Staten Island":staten_island_dict
}

f1.close()

# save the json object to a file 

f2 = open("data_bite.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
