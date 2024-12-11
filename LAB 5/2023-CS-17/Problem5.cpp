#include<iostream>
#include<vector>
using namespace std;

// Function to display a matrix
void PrintMatrix(const vector<vector<int>>& grid)
{
    for(int i = 0; i < grid.size(); i++)
    {
        for(int j = 0; j < grid[i].size(); j++)
        {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to add a new row to the matrix
void InsertRow(vector<vector<int>>& grid, vector<int> row)
{
    grid.push_back(row);
}

// Function to add a new column to the matrix
void InsertColumn(vector<vector<int>>& grid, vector<int> col)
{
    if(grid.size() == col.size())
    {
        for(int i = 0; i < grid.size(); i++)
        {
            grid[i].push_back(col[i]);
        }
        cout << "Matrix after adding a new column:" << endl;
    }
    else
    {
        cout << "Error: Column size does not match the matrix. Unable to add column." << endl;
    }
}

// Function to transpose the matrix
vector<vector<int>> TransposeMatrix(const vector<vector<int>>& grid)
{
    vector<vector<int>> transposedGrid(grid[0].size(), vector<int>(grid.size()));
    
    for(int i = 0; i < grid.size(); i++)
    {
        for(int j = 0; j < grid[i].size(); j++)
        {
            transposedGrid[j][i] = grid[i][j];
        }
    }
    return transposedGrid;
}

int main()
{
    // Initialize a matrix (2D grid)
    vector<vector<int>> grid = {{10, 20, 30}, {40, 50, 60}};
    
    // Display the initial matrix
    cout << "Original Matrix:" << endl;
    PrintMatrix(grid);
    
    // Add two rows to the matrix
    InsertRow(grid, {70, 80, 90});
    InsertRow(grid, {15, 25, 35});
    
    // Display the matrix after adding rows
    cout << endl << "Matrix after inserting 2 new rows:" << endl;
    PrintMatrix(grid);
    
    // Add a column to the matrix
    InsertColumn(grid, {100, 110, 120, 130});
    PrintMatrix(grid);
    
    // Display the transposed matrix
    cout << endl << "Transposed Matrix:" << endl;
    PrintMatrix(TransposeMatrix(grid));
    
    return 0;
}
