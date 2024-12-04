with open("Q2_input.txt", 'r') as file:
    input_list = [list(map(int, line.split())) for line in file]


safe = 0


for list in input_list:
    if list[0] > list[-1]:
        decreasing_check = True
        for i in range(len(list)-1):
            if list[i] < list[i+1] or (list[i] - list[i+1]) > 3 or (list[i] - list[i+1])==0 :
                decreasing_check = False
        
        if decreasing_check:
            safe += 1

    if list[0] < list[-1]:
        increasing_check = True
        for i in range(len(list)-1):
            if list[i] > list[i+1] or (list[i+1] - list[i] > 3) or (list[i] - list[i+1])==0 :
                increasing_check = False
        
        if increasing_check:
            safe += 1

print(safe)

### Part 2 : New Safe check ###

def is_safe_sequence(seq):
    increasing = all(1 <= seq[i+1] - seq[i] <= 3 for i in range(len(seq) - 1))
    decreasing = all(1 <= seq[i] - seq[i+1] <= 3 for i in range(len(seq) - 1))
    return increasing or decreasing

def is_safe_with_removal(seq):
    if is_safe_sequence(seq):
        return True

 
    for i in range(len(seq)):
        new_seq = seq[:i] + seq[i+1:]  
        if is_safe_sequence(new_seq):
            return True
    return False


# Count the number of safe lists
safe_count = 0

for seq in input_list:
    if is_safe_with_removal(seq):
        safe_count += 1

print(f"Total number of safe lists: {safe_count}")

### CHATGPT VERSION ###

#Part 1
# with open("Q2_input.txt", 'r') as file:
#     input_list = [list(map(int, line.split())) for line in file]

# def is_safe_sequence(sequence, increasing=True):
#     for i in range(len(sequence) - 1):
#         diff = sequence[i+1] - sequence[i]  # Calculate difference between consecutive elements
#         if (increasing and (diff <= 0 or diff > 3)) or (not increasing and (diff >= 0 or abs(diff) > 3)):
#             return False
#     return True

# safe = 0
# for seq in input_list:
#     if seq[0] < seq[-1] and is_safe_sequence(seq, increasing=True):
#         safe += 1
#     elif seq[0] > seq[-1] and is_safe_sequence(seq, increasing=False):
#         safe += 1

# print(safe)