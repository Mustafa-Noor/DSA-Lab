#include<iostream>
#include<vector>
using namespace std;

// Function to display the elements of a vector
void DisplayArray(vector<int>arr)
{
    for(int i=0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
}

// Function to reverse the elements of a vector
void ReverseArray(vector<int>& arr)
{
    for(int i = arr.size() - 1; i >= arr.size() / 2; i--)
    {
        int j = arr.size() - 1 - i;
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
}

// Function to sort the vector in ascending order
void SortAscending(vector<int>& arr)
{
    for(int i = 0; i < arr.size() - 1; i++)
    {
        int minIndex = i;
        for(int j = i + 1; j < arr.size(); j++)
        {
            if(arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

// Function to remove duplicates from the vector
void RemoveDuplicates(vector<int>& arr)
{
    for(int i = 0; i < arr.size() - 1; i++)
    {
        for(int j = i + 1; j < arr.size(); j++)
        {
            if(arr[i] == arr[j])
            {
                arr.erase(arr.begin() + j); 
                break;
            }
        }
    }
}

int main()
{
    vector<int> numbers1 = {25, 15, 45, 55, 25, 95, 45, 75};
    ReverseArray(numbers1);
    cout << "Reversed Array: ";
    DisplayArray(numbers1);
    cout <<endl;
    
    vector<int> numbers2 = {25, 15, 45, 55, 25, 95, 45, 75};
    SortAscending(numbers2);
    cout << "Sorted Array: ";
    DisplayArray(numbers2);
    cout << endl;
    
    vector<int> numbers3 = {25, 15, 45, 55, 25, 95, 45, 75};
    RemoveDuplicates(numbers3);
    cout << "Array After Removing Duplicates: ";
    DisplayArray(numbers3);
    
    return 0;
}
