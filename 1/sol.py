import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines: {len(lines)}")

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

print(f"Part 1 result: {result}")

# PART 2

num_to_int = {
    "nine": 9,
    "eight": 8,
    "seven": 7,
    "six": 6,
    "five": 5,
    "four": 4,
    "three": 3,
    "two": 2,
    "one": 1,
    "zero": 0,
}
result = 0

# this can't handle the substrings `twone` and `nineight`

for line in lines:    
    # print(line)
    for string,val in num_to_int.items():
        line = line.replace(string, str(val))
    # print(line)
    number = get_2_digit_num(line)
    # print(number)
    result += number
print(f"Part 2 result: {result}")
