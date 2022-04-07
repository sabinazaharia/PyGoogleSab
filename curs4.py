# # Curs 4
#
# import copy
#
# # lambda
#
# players = [
#     {
#         "first_name": "John",
#         "last_name": "Die",
#         "rank": 3
#     },
#     {
#         "first_name": "Kevin",
#         "last_name": "McDonald",
#         "rank": 1
#     },
#     {
#         "first_name": "Bradd",
#         "last_name": "Kelvin",
#         "rank": 2
#     }
# ]
#
# print(players)
# sorted_players = sorted(players, key=lambda player: player["rank"], reverse=True)
# print(sorted_players)
#
# # map
#
#
# def check_top_3_player(player):
#     updated_player = copy.deepcopy(player)
#     updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     return updated_player
#
#
# player_with_top_3_value = map(check_top_3_player, players)
# print(list(player_with_top_3_value))
#
#
# # zip
#
# first_list = [x for x in range(10)]
# second_list = [x for x in range(10, 100, 10)]
# third_list = [x for x in range(100, 1000, 100)]
#
# for zip_item in zip(first_list, second_list, third_list):
#     first_element, second_element, third_element = zip_item
#     print(first_element, second_element, third_element)
#
# even_squared_number = [item ** 2 for item in first_list if item % 2 == 0]
# print(even_squared_number)
import csv

with open("hello.txt", "w") as file:
    file.write("Hello World!")


new_cars = [['Dacia', 'Logan', 2005, 75],['Renault', 'Clio', 2005, 75],]

with open('data.csv', 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for new_car in new_cars:
        csv_writer.writerow(new_car)

with open('data.csv', 'r', newline='', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:
        print(row)