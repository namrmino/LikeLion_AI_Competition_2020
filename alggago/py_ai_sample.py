import sys
import math
import json


with open('temp.json') as json_file:
    json_data = json.load(json_file)


MAX_NUMBER = 16000


my_position = [0]
your_position = [1]

for key in json_data["my_position"].keys():
    my_position.append(json_data["my_position"][key])

for key in json_data["your_position"].keys():
    your_position.append(json_data["your_position"][key])


current_stone_number = 0
index = 0
min_length = MAX_NUMBER
x_length = MAX_NUMBER
y_length = MAX_NUMBER

moongchim = MAX_NUMBER
your_dist = MAX_NUMBER
a = 0
b = 0
moongchin_index1 = 0
moongchin_index2 = 0

while a <= (your_position.count - 2):
    b=a+1
    while b <= (your_position.count - 1):
        your_dist = math.sqrt((your_position[a][0] - your_position[b][0]) * (your_position[a][0] - your_position[b][0])
                    + (your_position[a][1] - your_position[b][1]) * (your_position[a][1] - your_position[b][1]))
        if moongchim > your_dist:
            moongchin_index1 = a
            moongchin_index2 = b
            moongchim = your_dist
        b=b+1
    a=a+1

avg_x = (your_position[moongchin_index1][0] + your_position[moongchin_index2][0]) / 2
avg_y = (your_position[moongchin_index1][1] + your_position[moongchin_index2][1]) / 2

if your_dist <= 100:
    for my in my_position:
        x_distance = abs(my[0] - avg_x)
        y_distance = abs(my[1] - avg_y)

        current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)

        if min_length > current_distance:
            current_stone_number = index
            min_length = current_distance
            x_length = avg_x - my[0]
            y_length = avg_y - my[1]
        
        index = index + 1

else:
    for my in my_position:
        for your in your_position:
            
            x_distance = abs(my[0] - your[0])
            y_distance = abs(my[1] - your[1])
            
            current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
            
            if min_length > current_distance:
                current_stone_number = index
                min_length = current_distance
                x_length = your[0] - my[0]
                y_length = your[1] - my[1]

        index = index + 1

#Return values
message = "MY AI!!!"
stone_number = current_stone_number
stone_x_strength = x_length * 5
stone_y_strength = y_length * 5
result = [stone_number, stone_x_strength, stone_y_strength, message]


print(str(result)[1:-1].replace("'", ""))