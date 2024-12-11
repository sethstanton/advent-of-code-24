# read in file scanning for mul(,) and removing any characters which are not numbers
# build the mul function - simple mul(a,b) = a * b
# collect them all into an array and then sum them up
import re
results = []

file_path = 'Python/advent of code/advc3.txt'
with open(file_path,'r') as file:
    input = file.read()

pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

matches = re.findall(pattern, input)
# print(len(matches))

for x, y in matches:
    product = int(x) * int(y)
    results.append(product)

total = sum(results)

print("Total Number:", total)