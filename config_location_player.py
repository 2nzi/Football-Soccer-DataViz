
pitch_width = 120
pitch_height = 80
nb_line = 7
space_line = (pitch_width/2)/7
x_line1 = 5

x_lines = [x_line1 + i * space_line for i in range(7)]
initial_player_position_middlepitch_home = {
    1: (x_lines[0], 40),
    2: (x_lines[1], 70),
    3: (x_lines[1], 55),
    4: (x_lines[1], 40),
    5: (x_lines[1], 25),
    6: (x_lines[1], 10),
    7: (x_lines[2], 70),
    8: (x_lines[2], 10),
    9: (x_lines[2], 55),
    10: (x_lines[2], 40),
    11: (x_lines[2], 25),
    12: (x_lines[3], 70),
    13: (x_lines[3], 55),
    14: (x_lines[3], 40),
    15: (x_lines[3], 25),
    16: (x_lines[3], 10),
    17: (x_lines[4], 70),
    18: (x_lines[4], 55),
    19: (x_lines[4], 40),
    20: (x_lines[4], 25),
    21: (x_lines[4], 10),
    22: (x_lines[6], 55),
    23: (x_lines[6], 40),
    24: (x_lines[6], 25),
    25: (x_lines[5], 40)
}

initial_player_position_middlepitch_away = {
    position_id: (pitch_width - x, y)
    for position_id, (x, y) in initial_player_position_middlepitch_home.items()
}

 

space_line = (pitch_width*0.8)/7
x_lines = [x_line1 + i * space_line for i in range(7)]
initial_player_position_allpitch_home = {
    1: (x_lines[0], 40),
    2: (x_lines[1], 70),
    3: (x_lines[1], 55),
    4: (x_lines[1], 40),
    5: (x_lines[1], 25),
    6: (x_lines[1], 10),
    7: (x_lines[2], 70),
    8: (x_lines[2], 10),
    9: (x_lines[2], 55),
    10: (x_lines[2], 40),
    11: (x_lines[2], 25),
    12: (x_lines[3], 70),
    13: (x_lines[3], 55),
    14: (x_lines[3], 40),
    15: (x_lines[3], 25),
    16: (x_lines[3], 10),
    17: (x_lines[4], 70),
    18: (x_lines[4], 55),
    19: (x_lines[4], 40),
    20: (x_lines[4], 25),
    21: (x_lines[4], 10),
    22: (x_lines[6], 55),
    23: (x_lines[6], 40),
    24: (x_lines[6], 25),
    25: (x_lines[5], 40)
}

initial_player_position_allpitch_away = {
    position_id: (pitch_width - x, y)
    for position_id, (x, y) in initial_player_position_allpitch_home.items()
}