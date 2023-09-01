#include <iostream>
#include <string>
using namespace std;

int main() {
    string input;

    cout << "Enter a string: ";
    cin >> input;

    string reversed = string(input.rbegin(), input.rend());

    cout << "Reversed string: " << reversed << endl;

    return 0;
}
