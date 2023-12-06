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
    print(number)
    result += number

print(result)

# PART 2