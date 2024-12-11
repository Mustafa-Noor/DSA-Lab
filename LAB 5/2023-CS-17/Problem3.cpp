#include<iostream>
#include<vector>
using namespace std;
void SearchValue(vector<int>vec, int value)
{
    bool found=false;
    for(int i=0;i<vec.size();i++)
    {
        if(vec[i]==value)
        {
            cout<<"Your Number found at index: "<<i;
            found=true;
            break;
        }
    }
    if(!found)
    cout<<"Your number is not found.";
}

int main()
{
    vector<int>vec={5,2,8,11,13,16,19};
    int value=8;
    SearchValue(vec,value);
}