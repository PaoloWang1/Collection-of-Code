#include <iostream>
#include <sstream>
#include <istream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream file("shuffle.in");
    int num_cows;
    vector<int> shuffle;
    vector<int> cowid;
    string row;
    getline(file, row);
    stringstream d(row);
    d >> num_cows;
    getline(file, row);
    stringstream s(row);
    for (int x = 0; x < num_cows; x++){
        int num;
        s >> num;
        shuffle.push_back(num);
    }
    getline(file, row);
    stringstream ss(row);
    for (int x = 0; x < num_cows; x++){
        int num;
        ss >> num;
        cowid.push_back(num);
    }
    vector<int> orig = cowid;

    for (int x = 0; x < 3; x++){
        for (int i = 0; i < num_cows; i++) {
            orig[i] = cowid[shuffle[i]];
        }

        for (int i = 0; i < num_cows; i++){
            cowid[i] = orig[i];
        }
    }
    ofstream output_file("shuffle.out");
    for (int x = 0; x < num_cows; x++) {
        output_file << cowid[x] << "\n";
    }

}