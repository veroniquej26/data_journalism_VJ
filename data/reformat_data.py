import json


f1 = open("data/original_data.csv", "r")
lines = f1.readlines()

dict = {}

year_list = []
year_list = lines[1].split(",")

borough_list = lines[2].split