import os

folder_path = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{folder_path}/input.txt").readlines()

print(f"# of lines: {len(lines)}")

# PART 1
result = 0
for line in lines: 
    win_str = line.split(":")[1].split("|")[0].strip()
    my_str = line.split(":")[1].split("|")[1].strip()
    winning_nums = {int(x) for x in win_str.split(" ") if x.isdigit()}
    my_nums = {int(x) for x in my_str.split(" ") if x.isdigit()}
    assert len(winning_nums) == 10
    assert len(my_nums) == 25

    # print(winning_nums)
    # print(my_nums)
    num_of_winners = winning_nums.intersection(my_nums)
    # print(num_of_winners)
    card_val = 2**(len(num_of_winners)-1)
    # print(card_val)
    if card_val >= 1:
        result += card_val
        
print(f"Part 1 Result: {result}")
# PART 2