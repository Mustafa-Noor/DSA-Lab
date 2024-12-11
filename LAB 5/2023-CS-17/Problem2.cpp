#include <iostream>
#include <vector>
using namespace std;
int main() 
{
    vector<int> vec;
    for (int i=0; i<100;i++) 
    {
        vec.push_back(i);
        cout << "After inserting element "<<i<<endl;
        cout << "Vector Size: " <<vec.size()<<endl;
        cout << "Vector Capacity: " <<vec.capacity()<<endl;
    }
}
