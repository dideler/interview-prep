matrix = [[1,2,3],
          [4,0,6],
          [7,8,9]]

def clear_row_col_on_match(matrix, value=0):
    # Have to keep track of coords so modifications don't affect future modifications.
    coords = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == value:
                coords.append((i, j))
    clear_rows_cols(coords, matrix, value)

def clear_rows_cols(coords, matrix, value):
    for row, col in coords:
        # Clear a whole row all at once.
        matrix[row] = [value for x in xrange(len(matrix[row]))]
        
        # Clear a column, row by row.
        for row in xrange(len(matrix)):
            matrix[row][col] = value

def print_matrix(matrix):
    for row in matrix:
        print row
    print

print_matrix(matrix)
clear_row_col_on_match(matrix)
print_matrix(matrix)
