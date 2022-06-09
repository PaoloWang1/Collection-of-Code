#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
using namespace std;


int main() {
    ifstream file("outofplace.in");
    vector<int> cows;
    string line;
    getline(file, line);
    stringstream s(line);
    int num_cows;
    s >> num_cows;
    for (int x = 0; x < num_cows; x++) {
        getline(file, line);
        stringstream ss(line);
        int num;
        ss >> num;
        cows.push_back(num);
    }

    vector<int> sorted = cows;
    sort(sorted.begin(), sorted.end());
    
    int count = 0;

    for (int x = 0; x < num_cows; x++){
        if (cows[x] != sorted[x]){
            count++;
        }
    }
    
    if (count != 0) {
        count--;
    }

    ofstream file_output("outofplace.out");
    file_output << count;
    file.close();
    file_output.close();
}