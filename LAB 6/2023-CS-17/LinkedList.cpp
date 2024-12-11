#include <iostream>
using namespace std;



class Node {

public:
    int data;
    Node* next;

    Node(int value){
        data = value;
        next = nullptr;
    }
    
};



class LinkList { 
public: 

    LinkList() { head = NULL; } 
    

    ~LinkList(){
        Node* temp;
        while(head != NULL){
            temp = head;
            head = head->next;
            delete temp;
        }
    }   
    
    bool isEmpty() { 
        return head == NULL; 
    } 

    Node* insertNode(int index, int x){
        if (index < 0){
            cout << "Index must be a non-negative integer." << endl;
            return nullptr;
        }

        Node* newNode = new Node(x);

        if(index == 0){
            newNode->next = head;
            head = newNode;
            return head;

        }

        Node* temp = head;
        for(int i=0; i< index - 1 && temp != nullptr; i++){
            temp = temp->next;
        }

        if(temp == nullptr){
            cout << "Index out of bounds." << endl;
            delete newNode;
            return nullptr;
        }

        newNode->next = temp->next;
        temp->next = newNode;
        return newNode;
    }


    Node* insertAtHead(int x){
        Node* newNode = new Node(x);
        newNode -> next = head;
        head = newNode;
        return head;

    }

    Node* insertAtEnd(int x){
        Node* newNode = new Node(x);
        if (head == nullptr){
            head = newNode;
        }
        else
        {
            Node* temp = head;
            while(temp->next != nullptr){
            temp->next = temp;
            }
            temp->next = newNode;
        }

        return newNode;   
    }

    bool findNode(int x){
        Node* temp = head;
        while (temp != nullptr)
        {
            if(temp->data == x){
                return true;
            } 

            temp = temp->next;
        }

        return false;
        
    }
    bool deleteNode(int x){
        if(head == nullptr){
            return false;
        }
        
        if(head->data == x){
            Node* temp = head;
            head = head->next;
            delete temp;
            return true;
        }

        Node* temp = head;
        while(temp->next != nullptr){
            if(temp->next->data == x){
                Node* nodeToDelete = temp->next;
                temp->next = temp->next->next;
                delete nodeToDelete;
                return true;
            }


            temp = temp->next;
        }


        return false;

    }

    bool deleteFromStart(){
        if(head == nullptr){
            return false;
        }
        
        
            Node* temp = head;
            head = head->next;
            delete temp;
            return true;
        
    }
    bool deleteFromEnd(){
        if(head == nullptr){
            return false;
        }

        if(head->next == nullptr){
            delete head;
            head = nullptr;
            return true;
        }


        Node* temp = head;

        while(temp->next->next != nullptr){
            temp = temp->next;
        }

        delete temp->next;
        temp->next = nullptr;
        return true;
    }

    void displayList(void){
        Node* temp = head;
        while(temp != nullptr){
            cout << temp->data << " -> ";
            temp = temp->next;
        }

        cout << "null" << endl;
    }


    Node* reverseList(){
        Node* prev = nullptr;
        Node* current = head;
        Node* next = nullptr;

        while (current != nullptr) {
            next = current->next;  
            current->next = prev;  
            prev = current;        
            current = next;        
        }

        head = prev;  
        return head;
    }

    Node* sortList(Node *list){
        if (list == nullptr || list->next == nullptr) {
        return list;  
        }

        Node* current;
        Node* index;
        int temp;

        for (current = list; current != nullptr; current = current->next) {
            for (index = current->next; index != nullptr; index = index->next) {
                if (current->data > index->data) {
                    // Swap the data
                    temp = current->data;
                    current->data = index->data;
                    index->data = temp;
                }
            }
        }

        return list;
    }

    Node* removeDuplicates(Node *list){
        if (list == nullptr) {
        return nullptr;
        }

        Node* current = list;

        while (current->next != nullptr) {
            if (current->data == current->next->data) {
                Node* duplicate = current->next;
                current->next = current->next->next;
                delete duplicate;  
            } else {
                current = current->next;
            }
        }

        return list;
    }

    Node* mergeLists(Node *list1, Node *list2){
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        Node* mergedHead = nullptr;

        if (list1->data <= list2->data) {
            mergedHead = list1;
            mergedHead->next = mergeLists(list1->next, list2);
        } else {
            mergedHead = list2;
            mergedHead->next = mergeLists(list1, list2->next);
        }

        return mergedHead;
    }

    Node* interestLists(Node *list1, Node *list2){
        Node* result = nullptr;
        Node* tail = nullptr;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->data < list2->data) {
                list1 = list1->next;
            } else if (list1->data > list2->data) {
                list2 = list2->next;
            } else {
                Node* newNode = new Node(list1->data);

                if (result == nullptr) {
                    result = newNode;  
                    tail = newNode;
                } else {
                    tail->next = newNode;
                    tail = newNode;
                }

                list1 = list1->next;
                list2 = list2->next;
            }
        }

        return result;
    }


private: 
    Node* head; 
}; 


int main(){
    
    LinkList list;

    // Insert nodes at head, end, and at a specific index
    list.insertAtHead(10);
    list.insertAtEnd(30);
    list.insertNode(1, 20);  // Insert at index 1

    // Display list
    cout << "List after inserting nodes:" << endl;
    list.displayList();

    // Find a node
    cout << "Is 20 in the list? " << (list.findNode(20) ? "Yes" : "No") << endl;

    // Delete from end
    list.deleteFromEnd();
    cout << "List after deleting from end:" << endl;
    list.displayList();

    // Delete a specific node
    list.deleteNode(10);
    cout << "List after deleting node with value 10:" << endl;
    list.displayList();

    // Reverse the list
    list.reverseList();
    cout << "List after reversing:" << endl;
    list.displayList();

    // Insert more nodes and sort the list
    list.insertAtEnd(50);
    list.insertAtEnd(40);
    list.insertAtEnd(30);
    cout << "List after adding more nodes before sorting:" << endl;
    list.displayList();

    list.sortList(list.sortList(nullptr));  // Sort the list
    cout << "List after sorting:" << endl;
    list.displayList();

    // Remove duplicates
    list.insertAtEnd(40);
    list.insertAtEnd(40); // Duplicates
    list.removeDuplicates(nullptr);
    cout << "List after removing duplicates:" << endl;
    list.displayList();

    // Merge two lists
    LinkList list2;
    list2.insertAtEnd(5);
    list2.insertAtEnd(15);
    list2.insertAtEnd(25);
    cout << "Second list:" << endl;
    list2.displayList();

    LinkList mergedList;
    mergedList.mergeLists(nullptr, nullptr);  // Merge list and list2
    cout << "Merged list:" << endl;
    mergedList.displayList();

    // Intersection of two lists
    LinkList intersectedList;
    intersectedList.interestLists(nullptr, nullptr);
    cout << "Intersection of lists:" << endl;
    intersectedList.displayList();
}