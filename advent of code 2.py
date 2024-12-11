#check whether the levels are increasing or decreasing returning a boolean
# checks if the levels are changing within the allowed range returning a boolean 
# returns a safe line if both are true.
# -1 is needed to ensure that there is no index error when i + 1 tries to checks
# for an additional elements which dont exist
def is_safe_line(levels):
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    allowed_diff = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    return (increasing or decreasing) and allowed_diff
    
# opens and reads the txt file line by line, this then splits the line into integers in a list 
# and checks if the line is safe, if it is the safe count increases.
# additional logic is used to check if the length of the line is more than 2 
# if it isn't then thats false 


def count_safe_lines(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                levels = list(map(int, line.split()))
                if len(levels) < 2:
                    continue
                
                if is_safe_line(levels):
                    safe_count += 1
            except ValueError:
                continue
    return safe_count



file_path = 'Python/advent of code/advc2.txt'
safe_lines = count_safe_lines(file_path)
print(f"Number of safe line: {safe_lines}")