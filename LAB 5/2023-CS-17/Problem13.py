
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_grid():
    for row in grid:
        print(row)

def add_row(new_row):
    if len(new_row) == len(grid[0]):  
        grid.append(new_row)
    else:
        print("Row length does not match the grid columns.")

def add_column(new_col):
    if len(new_col) == len(grid):  
        for i in range(len(grid)):
            grid[i].append(new_col[i])
    else:
        print("Column length does not match the grid rows.")

def sum_grid():
    total = sum(sum(row) for row in grid)
    return total

# Example Usage
print("Original Grid:")
display_grid()

add_row([10, 11, 12])
print("\nGrid after adding a row:")
display_grid()

add_column([13, 14, 15, 16])
print("\nGrid after adding a column:")
display_grid()

print(f"\nSum of all elements in the grid: {sum_grid()}")