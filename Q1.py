
with open('Q1_input.txt', 'r') as file:

    left_list = []
    right_list = []
    for line in file:

        left, right = map(int, line.split())

        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()
res = 0
for i in range(len(left_list)):
    res += abs(left_list[i] - right_list[i])
print(res)

# getting the similarity score
right_list_dict = {}

for num in right_list:
    if num in right_list_dict:
        right_list_dict[num] += 1
    else:
        right_list_dict[num] = 1

similarity_score = 0

for num in left_list:
    if num in right_list_dict:
        similarity_score += num * right_list_dict[num]

print(similarity_score)


### CHATGPT VERSION ###

'''with open('Q1_input.txt', 'r') as file:
    # Parse input into two lists
    left_list = []
    right_list = []
    
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()

# Calculate the absolute difference sum
res = sum(abs(left - right) for left, right in zip(left_list, right_list))
print("Absolute Difference Sum:", res)

# Calculate the similarity score
from collections import Counter

# Use Counter to efficiently count occurrences in right_list
right_list_dict = Counter(right_list)

# Compute similarity score
similarity_score = sum(num * right_list_dict.get(num, 0) for num in left_list)
print("Similarity Score:", similarity_score)'''