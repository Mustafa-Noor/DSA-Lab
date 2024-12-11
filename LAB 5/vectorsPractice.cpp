#include <iostream>
#include <vector>
using namespace std;

int main(){

    vector <int> vec;
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);
    vec.push_back(40);


    cout << "Vector elements: ";
    for (int i = 0; i < vec.size(); ++i)
    {
        cout << vec[i] << " ";
    }


    cout << "\nSize: " << vec.size() << ", Capacity: " << vec.
    capacity() << endl;
    // Adding more elements to show dynamic resizing
    vec.push_back(50);
    cout << "After adding one more element:\n";
    cout << "Size: " << vec.size() << ", Capacity: " << vec.
    capacity() << endl;
    return 0;


}

