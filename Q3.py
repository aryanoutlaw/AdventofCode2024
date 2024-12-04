def parse_memory_part1(text):
    
    total = 0
    i = 0
    
    while i < len(text):
        
        if i + 3 < len(text) and text[i:i+4] == "mul(":
            i += 4
            try:
               
                num1 = ""
                while i < len(text) and text[i].isdigit():
                    num1 += text[i]
                    i += 1
                    
                # Skip comma
                if i < len(text) and text[i] == ",":
                    i += 1
                else:
                    continue
                    
                # Get second number
                num2 = ""
                while i < len(text) and text[i].isdigit():
                    num2 += text[i]
                    i += 1
                    
                # Verify closing parenthesis
                if i < len(text) and text[i] == ")":
                    if num1 and num2:  
                        total += int(num1) * int(num2)
            except:
                pass
        i += 1
        
    return total

def parse_memory_part2(text):
    
    total = 0
    i = 0
    enabled = True  
    
    while i < len(text):
        
        if i + 2 < len(text) and text[i:i+3] == "do(":
            if i + 3 < len(text) and text[i+3] == ")":
                enabled = True
                i += 4
                continue
                
        
        if i + 5 < len(text) and text[i:i+6] == "don't(":
            if i + 6 < len(text) and text[i+6] == ")":
                enabled = False
                i += 7
                continue
                
        
        if i + 3 < len(text) and text[i:i+4] == "mul(":
            i += 4
            try:
                num1 = ""
                while i < len(text) and text[i].isdigit():
                    num1 += text[i]
                    i += 1
                    
                if i < len(text) and text[i] == ",":
                    i += 1
                else:
                    continue
                    
                num2 = ""
                while i < len(text) and text[i].isdigit():
                    num2 += text[i]
                    i += 1
                    
                if i < len(text) and text[i] == ")":
                    if num1 and num2 and enabled:  
                        total += int(num1) * int(num2)
            except:
                pass
        i += 1
        
    return total


with open('Q3_input.txt', 'r') as file:
    puzzle_input = file.read()


part1_answer = parse_memory_part1(puzzle_input)
part2_answer = parse_memory_part2(puzzle_input)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")