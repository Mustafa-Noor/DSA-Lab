#include <iostream>
using namespace std;

class Stack{

private:
    int top;
    int arr[100];
    int maxSize;


public:
    Stack(int size){
        maxSize = size;
        top = -1;
    }

    bool isEmpty(){
        return top == -1;
    }

    bool isFull(){
        return top == maxSize-1;
    }

    void push(int value){
        if(isFull()){
            cout << "Stack is full!" << endl;
            return;
        }
        else{
            top++;
            arr[top] = value;
        }
    }

    int pop(){
        if(isEmpty()){
            cout << "Stack is empty!!" << endl;
            return;
        }
        else{
            int value = arr[top];
            top--;
            return value;
        }
    }

    int peek(){
        if(isEmpty()){
            cout << "Stack is empty!!" << endl;
            return;
        }
        int value = arr[top];
        return value;
    }


};

int main() {
    
    Stack stack(10);

    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout << "Popped element: " << stack.pop() << endl;
}