#include <iostream>
#include <stdexcept>  // For exception handling
using namespace std;

template <typename T>
class Vector {
public:
    T* data;         // Pointer to dynamically allocated array
    int size;        // Current number of elements
    int capacity;    // Current capacity of the array

    // Constructor to initialize an empty vector
    Vector() : size(0), capacity(1) {
        data = new T[capacity];  // Start with capacity 1
    }

    // Destructor to clean up the dynamic memory
    ~Vector() {
        delete[] data;
    }

    // Function to add elements at the end of the vector
    void PushBack(T value) {
        if (size >= capacity) {
            capacity *= 2; // Double the capacity if needed
            T* newData = new T[capacity]; // Allocate new larger array

            // Copy the old elements to the new array
            for (int i = 0; i < size; i++) {
                newData[i] = data[i];
            }
            delete[] data;  // Deallocate the old array
            data = newData; // Point to the new array
        }

        // Add the new element and increase the size
        data[size++] = value;
    }

    // Operator[] overloading for element access with bounds checking (modifiable)
    T& operator[](int index) {
        if (index >= size || index < 0) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }

    // Operator[] overloading for element access with bounds checking (read-only)
    T operator[](int index) const {
        if (index >= size || index < 0) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }

    // Overload the << operator for printing the vector elements
    friend ostream& operator<<(ostream& out, const Vector& vec) {
        for (int i = 0; i < vec.size; i++) {
            out << vec[i];
            if (i < vec.size - 1) {
                out << " "; // Add space between elements
            }
        }
        return out;
    }
};

int main() {
    // Create a vector of integers
    Vector<int> vec;

    // Add elements to the vector
    vec.PushBack(10);
    vec.PushBack(20);
    vec.PushBack(30);

    // Output the contents of the vector
    cout << "Vector: " << vec << endl;

    // Access and print a specific element
    cout << "Element at index 1: " << vec[1] << endl;

    // Add more elements
    vec.PushBack(40);
    vec.PushBack(50);

    // Output the contents of the vector again
    cout << "Vector after adding more elements: " << vec << endl;

    return 0;
}

