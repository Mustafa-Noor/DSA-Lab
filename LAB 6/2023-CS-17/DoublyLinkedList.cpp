#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;

    Node(int value) {
        data = value;
        next = nullptr;
        prev = nullptr;
    }
};

class DoublyLinkedList {
public:
    DoublyLinkedList() {
        head = nullptr;
    }

    ~DoublyLinkedList() {
        Node* temp;
        while (head != nullptr) {
            temp = head;
            head = head->next;
            delete temp;
        }
    }

    bool isEmpty() {
        return head == nullptr;
    }

    Node* insertNode(int index, int x) {
        if (index < 0) {
            cout << "Index must be a non-negative integer." << endl;
            return nullptr;
        }

        Node* newNode = new Node(x);

        if (index == 0) {
            newNode->next = head;
            if (head != nullptr) {
                head->prev = newNode;
            }
            head = newNode;
            return head;
        }

        Node* temp = head;
        for (int i = 0; i < index - 1 && temp != nullptr; i++) {
            temp = temp->next;
        }

        if (temp == nullptr) {
            cout << "Index out of bounds." << endl;
            delete newNode;
            return nullptr;
        }

        newNode->next = temp->next;
        newNode->prev = temp;
        if (temp->next != nullptr) {
            temp->next->prev = newNode;
        }
        temp->next = newNode;
        return newNode;
    }

    Node* insertAtHead(int x) {
        Node* newNode = new Node(x);
        newNode->next = head;
        if (head != nullptr) {
            head->prev = newNode;
        }
        head = newNode;
        return head;
    }

    Node* insertAtEnd(int x) {
        Node* newNode = new Node(x);
        if (head == nullptr) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
            newNode->prev = temp;
        }
        return newNode;
    }

    bool findNode(int x) {
        Node* temp = head;
        while (temp != nullptr) {
            if (temp->data == x) {
                return true;
            }
            temp = temp->next;
        }
        return false;
    }

    bool deleteNode(int x) {
        if (head == nullptr) {
            return false;
        }

        if (head->data == x) {
            Node* temp = head;
            head = head->next;
            if (head != nullptr) {
                head->prev = nullptr;
            }
            delete temp;
            return true;
        }

        Node* temp = head;
        while (temp != nullptr) {
            if (temp->data == x) {
                if (temp->next != nullptr) {
                    temp->next->prev = temp->prev;
                }
                if (temp->prev != nullptr) {
                    temp->prev->next = temp->next;
                }
                delete temp;
                return true;
            }
            temp = temp->next;
        }
        return false;
    }

    bool deleteFromStart() {
        if (head == nullptr) {
            return false;
        }

        Node* temp = head;
        head = head->next;
        if (head != nullptr) {
            head->prev = nullptr;
        }
        delete temp;
        return true;
    }

    bool deleteFromEnd() {
        if (head == nullptr) {
            return false;
        }

        if (head->next == nullptr) {
            delete head;
            head = nullptr;
            return true;
        }

        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }

        temp->prev->next = nullptr;
        delete temp;
        return true;
    }

    void displayList() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " <-> ";
            temp = temp->next;
        }
        cout << "null" << endl;
    }

    Node* reverseList() {
        Node* temp = nullptr;
        Node* current = head;

        while (current != nullptr) {
            temp = current->prev;
            current->prev = current->next;
            current->next = temp;
            current = current->prev;
        }

        if (temp != nullptr) {
            head = temp->prev;
        }

        return head;
    }

    Node* sortList(Node* list) {
        if (list == nullptr || list->next == nullptr) {
            return list;
        }

        Node* current;
        Node* index;
        int temp;

        for (current = list; current != nullptr; current = current->next) {
            for (index = current->next; index != nullptr; index = index->next) {
                if (current->data > index->data) {
                    temp = current->data;
                    current->data = index->data;
                    index->data = temp;
                }
            }
        }

        return list;
    }

    Node* removeDuplicates(Node* list) {
        if (list == nullptr) {
            return nullptr;
        }

        Node* current = list;

        while (current->next != nullptr) {
            if (current->data == current->next->data) {
                Node* duplicate = current->next;
                current->next = current->next->next;
                if (current->next != nullptr) {
                    current->next->prev = current;
                }
                delete duplicate;
            } else {
                current = current->next;
            }
        }

        return list;
    }

    Node* mergeLists(Node* list1, Node* list2) {
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        Node* mergedHead = nullptr;

        if (list1->data <= list2->data) {
            mergedHead = list1;
            mergedHead->next = mergeLists(list1->next, list2);
            if (mergedHead->next != nullptr) {
                mergedHead->next->prev = mergedHead;
            }
        } else {
            mergedHead = list2;
            mergedHead->next = mergeLists(list1, list2->next);
            if (mergedHead->next != nullptr) {
                mergedHead->next->prev = mergedHead;
            }
        }

        return mergedHead;
    }

    Node* interestLists(Node* list1, Node* list2) {
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
                    newNode->prev = tail;
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

int main() {
    DoublyLinkedList list;

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

}
