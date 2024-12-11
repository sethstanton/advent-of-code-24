import re

final_result = []
matches_found = []
total_mul = []
pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

file_path = 'Python/advent of code/advc3.txt'

def whole_thing(file_path):
    with open(file_path, 'r') as file:
        document = file.read()
        matches_found = re.findall(pattern, document)
    for a,b in matches_found:
        prod_result = int(a) * int(b)
        final_result.append(prod_result)
    total_mul = sum(final_result)
    return print("Total Number", total_mul)

whole_thing(file_path);


    
    


    





        



