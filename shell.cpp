#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
using namespace std;

/*
simulate by swapping then counting which shells were guessed
*/

int main() {
    ifstream file("shell.in");
    vector<vector<int>> shells;
    int num_points;
    string line;
    //cin >> num_points;
    getline(file, line);
    stringstream s(line);
    s >> num_points;
    string line_shells;
    for (int x = 0; x < num_points; x++){
        getline(file, line_shells);
        stringstream ss(line_shells);
        shells.push_back({}); 
        while (ss.eof() == false) {
            int data;
            ss >> data;
            shells[x].push_back(data);
        }
    }
    cout << "data read: \n";
    cout << num_points << "\n";
    for (int x = 0; x < num_points; x++) {
        for (int y = 0; y < shells[x].size(); y++){
            cout<< shells[x][y] << " ";
        }
        cout << "\n";
    }
    vector<int> simulated = {1, 2, 3};
    vector<int> guesses = {0, 0, 0};
    for (int row = 0; row < shells.size(); row++){
        swap(simulated[shells[row][0]-1], simulated[shells[row][1]-1]);guesses[simulated[shells[row][2]-1]-1]++;
    }
    cout << "guesses: " << "\n";
    for (int x = 0; x < guesses.size(); x++){
        cout << guesses[x] << " ";
    }
    cout << "\n";
    cout << *max_element(guesses.begin(), guesses.end());

    ofstream file_output("shell.out");
    file_output << *max_element(guesses.begin(), guesses.end());
    file_output.close();
    file.close();
}