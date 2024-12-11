#include <iostream>
using namespace std;

class Queue{

private:
    int front, rear;
    int arr[100];
    int maxSize;

public:
    Queue(int size){
        maxSize = size;
        front = rear = -1;
    }

    bool isEmpty(){
        return front == -1;
    }

    bool isFull(){
        return rear == maxSize - 1;
    }

    void enqueue(int value){

        if(isFull()){
            cout << "Queue is Full!"<< endl;
            return;
        }
        if(isEmpty()){
            front = 0;
        }

        arr[++rear] = value;
    }

    int dequeue(){
        if(isEmpty()){
            cout << "Queue is empty!" << endl;
            return;
        }

        int value = arr[front];

        if(front == rear){
            front = rear = -1;

        }
        else{
            front++;
        }

        return value;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return arr[front];
    }

};


int main() {
    Queue queue(10);

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);

    cout << "Dequeued element: " << queue.dequeue() << endl;
}