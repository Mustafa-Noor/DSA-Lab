#include <iostream>
#include <stack>
#include <string>
using namespace std;

void reverseWords(string sentence);


int main(){

    
    string sentence = "I am from University of Engineering and Technology Lahore";
    cout << "Original Sentence: " << sentence << endl;

    cout << "Reversed Words: ";
    reverseWords(sentence);

}


void reverseWords(string sentence){
    stack<string> words;

    string word = "";
    int index = 0;

    while(sentence[index] != '\0'){

        if(sentence[index] != ' '){
            word += sentence[index];
        }
        else{
            words.push(word);
            word = "";
        }

        index++;

    }

    words.push(word);

    while (!words.empty()) {
        cout << words.top() << " ";
        words.pop();
    }

    cout << endl;
}