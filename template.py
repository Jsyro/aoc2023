import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines:{len(lines)}")

# PART 1
result = None

print(f"Part 1 Result: {result}")
# PART 2