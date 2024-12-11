#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <chrono>
using namespace std;

// AutoGrowingArray class implementation
template <typename T>
class AutoGrowingArray {
public:
    T* data;
    int size;
    int capacity;

    AutoGrowingArray() : size(0), capacity(1) {
        data = new T[capacity];
    }

    ~AutoGrowingArray() {
        delete[] data;
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity *= 2;
            T* newData = new T[capacity];
            for (int i = 0; i < size; i++) {
                newData[i] = data[i];
            }
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    friend ostream& operator<<(ostream& out, const AutoGrowingArray& array) {
        for (int i = 0; i < array.size; i++) {
            out << array.data[i] << " ";
        }
        return out;
    }
};

// Function to load data from a file into a vector
void LoadIntoVector(const string& filename, vector<int>& vec) {
    ifstream file(filename);
    int number;
    while (file >> number) {
        vec.push_back(number);
    }
    file.close();
}

// Function to load data from a file into an AutoGrowingArray
void LoadIntoAutoGrowingArray(const string& filename, AutoGrowingArray<int>& arr) {
    ifstream file(filename);
    int number;
    while (file >> number) {
        arr.PushBack(number);
    }
    file.close();
}

// Function to load data from a file into a list
void LoadIntoList(const string& filename, list<int>& lst) {
    ifstream file(filename);
    int number;
    while (file >> number) {
        lst.push_back(number);
    }
    file.close();
}

// Function to write the content of a vector to a file
void WriteToFile(const string& filename, const vector<int>& vec) {
    ofstream file(filename);
    for (const auto& value : vec) {
        file << value << " ";
    }
    file.close();
}

// Function to write the content of a list to a file
void WriteToFile(const string& filename, const list<int>& lst) {
    ofstream file(filename);
    for (const auto& value : lst) {
        file << value << " ";
    }
    file.close();
}

// Function to write the content of AutoGrowingArray to a file
template <typename T>
void WriteToFile(const string& filename, const AutoGrowingArray<T>& arr) {
    ofstream file(filename);
    for (int i = 0; i < arr.size; i++) {
        file << arr.data[i] << " ";
    }
    file.close();
}

// Function to create a random file of size `Size` MB
void CreateRandomFile(const string& fn, int Size, int RN = 100) {
    srand(static_cast<unsigned int>(time(0)));
    ofstream Writer(fn);
    for (int i = 0; i < Size * 1024 * 1024; i++) {
        Writer << rand() % RN << " ";
    }
    Writer.close();
}

int main() {
    const string inputFile = "random_data.txt";
    const int fileSizeMB = 2; // Create a 2 MB file

    // Create the random file
    CreateRandomFile(inputFile, fileSizeMB);

    // Measure time for Vector
    vector<int> vec;
    auto start = chrono::high_resolution_clock::now();
    LoadIntoVector(inputFile, vec);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "Time taken to load into Vector: " << elapsed.count() << " seconds" << endl;
    WriteToFile("OutputVector.txt", vec);

    // Measure time for AutoGrowingArray
    AutoGrowingArray<int> autoArr;
    start = chrono::high_resolution_clock::now();
    LoadIntoAutoGrowingArray(inputFile, autoArr);
    end = chrono::high_resolution_clock::now();
    elapsed = end - start;
    cout << "Time taken to load into AutoGrowingArray: " << elapsed.count() << " seconds" << endl;
    WriteToFile("OutputGA.txt", autoArr);

    // Measure time for List
    list<int> lst;
    start = chrono::high_resolution_clock::now();
    LoadIntoList(inputFile, lst);
    end = chrono::high_resolution_clock::now();
    elapsed = end - start;
    cout << "Time taken to load into List: " << elapsed.count() << " seconds" << endl;
    WriteToFile("OutputArraylist.txt", lst);

    return 0;
}
