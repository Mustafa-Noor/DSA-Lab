#include <iostream>
#include <stdexcept>
#include <algorithm> // For std::copy
using namespace std;

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

    T operator[](int index) const {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return data[index];
    }

    T& operator[](int index) {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return data[index];
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity *= 2;
            T* newData = new T[capacity];
            // Use std::copy to copy existing data to newData
            std::copy(data, data + size, newData);
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    friend ostream& operator<<(ostream& out, const AutoGrowingArray& array) {
        out << "[ ";
        for (int i = 0; i < array.size; ++i) {
            out << array.data[i];
            if (i < array.size - 1) {
                out << ", ";
            }
        }
        out << " ]";
        return out;
    }
};

int main() {
    AutoGrowingArray<int> arr;

    arr.PushBack(10);
    arr.PushBack(20);
    arr.PushBack(30);
    arr.PushBack(40);
    arr.PushBack(50);

    cout << "Array contents: " << arr << endl;

    cout << "Element at index 2: " << arr[2] << endl;

    arr[2] = 100;
    cout << "Array contents after modification: " << arr << endl;

    return 0;
}
