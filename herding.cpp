#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
using namespace std;

int main() {
    ifstream file("herding.in");
    vector<int> cows;
    string line;
    getline(file, line);
    stringstream s(line);
    while (s.eof() == false) {
        int num;
        s >> num;
        cows.push_back(num);
    }
    sort(cows.begin(), cows.end());
    ofstream file_output("herding.out");

    if (cows[2] == cows[0]+2) {
        file_output << 0 << "\n";
    } else if (cows[1] == cows[0] + 2 or cows[2] == cows[1] + 2) {
        file_output << 1 << "\n";
    } else {
        file_output << 2 << "\n";
    }
    int max1 = max(cows[1] - cows[0], cows[2] - cows[1]) - 1;
    file_output << max1 << "\n";

    file_output.close();
    file.close();

}