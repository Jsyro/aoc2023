import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines:{len(lines)}")

# PART 1
result = 0

max_cubes = {"red": 12, "green":13,"blue":14}

for line in lines: 
    game_num = int(line.split(':')[0].split(" ")[1])
    draws = line.split(":")[1].split(";")
    draws = [d.strip() for d in draws]
    valid_game = True
    for draw in draws:
        pulls = draw.split(", ")
        for pull in pulls:
            amt, colour = pull.split(" ")
            if int(amt) > max_cubes[colour]:
                valid_game = False
        
    if valid_game:
        result += game_num

print(f"Part 1 Result: {result}")
# PART 2

result = 0

for line in lines: 
    game_num = int(line.split(':')[0].split(" ")[1])
    draws = line.split(":")[1].split(";")
    draws = [d.strip() for d in draws]
    colours_needed = {}
    valid_game = True
    for draw in draws:
        pulls = draw.split(", ")
        for pull in pulls:
            amt, colour = pull.split(" ")
            if int(amt) > colours_needed.get(colour,0):
                colours_needed[colour] = int(amt)
        
    power = 1
    for max in colours_needed.values():
        power = power * max
    result += power

print(f"Part 2 Result: {result}")