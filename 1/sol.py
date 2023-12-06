import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines:{len(lines)}")

# PART 1

result = 0

for line in lines:
    first_digit = ''
    last_digit = ''
    for char in line:
        if char.isdigit() and not first_digit:
            first_digit = char
        if char.isdigit():
            last_digit = char
    number = int(first_digit+last_digit)
    result += number

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

for line in lines[:10]:
    digit_strings = {val:line.find(st) for st,val in num_to_int.items() if line.find(st) != -1}
    print(digit_strings)
