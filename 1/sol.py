import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines:{len(lines)}")

def get_2_digit_num(line):
    first_digit = ''
    last_digit = ''
    for char in line:
        if char.isdigit() and not first_digit:
            first_digit = char
        if char.isdigit():
            last_digit = char
    number = int(first_digit+last_digit)
    return number

# PART 1

result = 0

for line in lines:
    result += get_2_digit_num(line)

print(f"Part 1 result:{result}")

# PART 2

num_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}
result = 0

for line in lines[:10]:    
    for string,val in num_to_int.items():
        line = line.replace(string, str(val))
    result += get_2_digit_num(line)
print(f"Part 2 result:{result}")
