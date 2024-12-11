#include <iostream>
#include <stack>
#include <sstream>
#include <string>
#include <cctype>

using namespace std;

class Stack {
private:
    stack<int> s;

public:
    void push(int value) {
        s.push(value);
    }

    int pop() {
        if (s.empty()) {
            cout << "Error: Stack is empty!" << endl;
            return 0;
        }
        int top = s.top();
        s.pop();
        return top;
    }

    int top() {
        if (s.empty()) {
            cout << "Error: Stack is empty!" << endl;
            return 0;
        }
        return s.top();
    }

    bool empty() {
        return s.empty();
    }

    void printStack() {
        stack<int> temp = s; // Make a copy to print
        if (temp.empty()) {
            cout << "Stack is empty." << endl;
            return;
        }
        cout << "Stack contents: ";
        while (!temp.empty()) {
            cout << temp.top() << " ";
            temp.pop();
        }
        cout << endl;
    }
};

int main() {
    Stack calculatorStack;
    string input;

    cout << "Enter integers, operators (+, -, *, /, %), '?' for stack state, '^' for top element, '!' to exit:" << endl;

    while (true) {
        cout << "> ";
        getline(cin, input);
        istringstream tokens(input);
        string token;

        while (tokens >> token) {
            if (isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) { // Check for valid integer
                calculatorStack.push(stoi(token));
            } else if (token == "+") {
                int right = calculatorStack.pop();
                int left = calculatorStack.pop();
                calculatorStack.push(left + right);
            } else if (token == "-") {
                int right = calculatorStack.pop();
                int left = calculatorStack.pop();
                calculatorStack.push(left - right);
            } else if (token == "*") {
                int right = calculatorStack.pop();
                int left = calculatorStack.pop();
                calculatorStack.push(left * right);
            } else if (token == "/") {
                int right = calculatorStack.pop();
                int left = calculatorStack.pop();
                if (right != 0) {
                    calculatorStack.push(left / right);
                } else {
                    cout << "Error: Division by zero" << endl;
                }
            } else if (token == "%") {
                int right = calculatorStack.pop();
                int left = calculatorStack.pop();
                calculatorStack.push(left % right);
            } else if (token == "?") {
                calculatorStack.printStack();
            } else if (token == "^") {
                cout << "Top element: " << calculatorStack.top() << endl;
                calculatorStack.pop(); // Remove the top element after printing
            } else if (token == "!") {
                cout << "Exiting..." << endl;
                return 0; // Exit the program
            } else {
                cout << "Error: Unknown command or operator '" << token << "'" << endl;
            }
        }
    }

    return 0;
}
