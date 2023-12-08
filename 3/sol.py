import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines:{len(lines)}")

raw_input = open(f"{folder_path}/input.txt").read()
symbols = set(raw_input) - {str(i) for i in range(10)} - {"."}
print(symbols)
# PART 1
result = 0

for i,line in enumerate(lines[:10]): 
    print(lines[i-1])
    print(lines[i])
    print(lines[i+1])
    possible_parts = [p for p in line.split(".") if p != "" and p.isdigit()]
    print(possible_parts)
    for pp in possible_parts:
        start_index = line.find(pp)
        end_index = start_index + len(pp)

        prev_line, curr_line, next_line = "", "", ""
        try:
            if i > 0:
                prev_line = lines[i-1][start_index-1:end_index+1]   
        except IndexError:
            pass
        try: 
            curr_line = lines[i][start_index-1:end_index+1]
        except IndexError:
            pass
        try:
            next_line = lines[i+1][start_index-1:end_index+1]
        except IndexError:
            pass
        
        char_set = set(str(prev_line) + str(curr_line) + str(next_line))
        if not pp.isdigit():
            print(f"WEIRD CHARACTER: {pp}")
            continue

        if symbols.intersection(char_set):
            print(f"REAL PART: {pp}")
            result += int(pp)
        else:
            print(f"BAD PART: {pp}")

print(f"Part 1 Result: {result}")

# PART 2