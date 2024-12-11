#include<iostream>
#include<vector>
#include <string>
#include<algorithm>

using namespace std;


int main() {
    vector<string> vec; 
    int choice;
    string input;

    while (true) {
        cout << "1. Add a string" << endl;
        cout << "2. Remove a string" << endl;
        cout << "3. Exit" << endl;
        cout << "Choose an option (1/2/3): ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter the string to add: ";
            cin.ignore(); 
            getline(cin, input); 
            vec.push_back(input);  
            cout << "'" << input << "' added to the vector." << endl;
        } 
        else if (choice == 2) {
            cout << "Enter the string to remove: ";
            cin.ignore();
            getline(cin, input);

            auto it = find(vec.begin(), vec.end(), input);
            if (it != vec.end()) {
                vec.erase(it);
                cout << "'" << input << "' removed from the vector." << endl;
            } else {
                cout << "'" << input << "' not found in the vector." << endl;
            }
        } 
        else if (choice == 3) {
            cout << "Exiting the program." << endl;
            break; 
        } 
        else {
            cout << "Invalid option. Please try again." << endl;
        }

        cout << "Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
    }

    return 0;
}
