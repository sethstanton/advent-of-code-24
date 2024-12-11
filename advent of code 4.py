

def count_num_xmas(file_input):
    with open(file_input, 'r') as file:
        character_grid = [list(row.strip()) for row in file.readlines()]
    movement_directions = [
        (0,1),
        (0, -1),
        (1, 0),
        (-1,0),
        (1,1),
        (-1,-1),
        (1,-1),
        (-1,1),
    ]

    target_word = "XMAS"
    number_of_rows = len(character_grid)
    number_of_columns = len(character_grid[0])
    total_count = 0

    def does_word_exist_from_position(starting_row, starting_col, row_increment, col_increment):
        for letter_index in range(len(target_word)):
            current_row = starting_row + letter_index * row_increment
            current_col = starting_col + letter_index * col_increment
            # Ensure the current position is valid and matches the target letter

            if not (0 <= current_row < number_of_rows and 0 <= current_col < number_of_columns) or \
               character_grid[current_row][current_col] != target_word[letter_index]:
                return False
        return True
    
    for row_index in range(number_of_rows):
        for col_index in range(number_of_columns):
            for row_direction, column_direction in movement_directions:
                if does_word_exist_from_position(row_index, col_index, row_direction, column_direction):
                    total_count += 1
    return total_count

file_path = 'Python/advent of code/advc4.txt'
print("Number of XMAS occurrences", count_num_xmas(file_path))