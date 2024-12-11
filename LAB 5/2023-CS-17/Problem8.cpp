#include <iostream>
#include <stdexcept>
using namespace std;

template <typename T>
class ArrayList {
public:
    T* arr;
    int size;
    int capacity;

    ArrayList() : size(0), capacity(2) {
        arr = new T[capacity];
    }

    ~ArrayList() {
        delete[] arr;
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity = static_cast<int>(capacity * 1.5);
            T* temp = new T[capacity];
            for (int i = 0; i < size; i++) {
                temp[i] = arr[i];
            }
            delete[] arr;
            arr = temp;
        }
        arr[size] = value;
        size++;
    }

    T& operator[](int index) {
        if (index >= size || index < 0) {
            throw out_of_range("Index out of bounds");
        }
        return arr[index];
    }

    T operator[](int index) const {
        if (index >= size || index < 0) {
            throw out_of_range("Index out of bounds");
        }
        return arr[index];
    }

    friend ostream& operator<<(ostream& out, const ArrayList& arrList) {
        for (int i = 0; i < arrList.size; i++) {
            out << arrList[i] << " ";
        }
        return out;
    }
};

int main() {
    ArrayList<int> arrList;
    arrList.PushBack(10);
    arrList.PushBack(20);
    arrList.PushBack(30);
    cout << "ArrayList: " << arrList << endl;

    cout << "Element at index 1: " << arrList[1] << endl;

    arrList.PushBack(40);
    arrList.PushBack(50);
    cout << "ArrayList after adding more elements: " << arrList << endl;

    return 0;
}