#include <iostream>
#include <ostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;


void pour_milk(int& total1, int& bucket1, int& total2, int& bucket2) {
    int milk = min(bucket1, total2 - bucket2);
    bucket1 -= milk;
    bucket2 += milk;
}

int main() {
    ifstream file("mixmilk.in");
    vector<vector<int>> cows;

    for (int x = 0; x < 3; x++) {
        string line;
        getline(file, line);
        stringstream s(line);
        int d;
        s >> d;
        cows.push_back({});
        cows[x].push_back(d);
        s >> d;
        cows[x].push_back(d);
    }

    for (int i = 0; i < 33; i++) {
        pour_milk(cows[0][0], cows[0][1], cows[1][0], cows[1][1]);
        pour_milk(cows[1][0], cows[1][1], cows[2][0], cows[2][1]);
        pour_milk(cows[2][0], cows[2][1], cows[0][0], cows[0][1]);
    }

    pour_milk(cows[0][0], cows[0][1], cows[1][0], cows[1][1]);

    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 2; y++) {
            cout << cows[x][y];
            cout << " ";
        }
        cout << "\n";
    }

    ofstream output_file("mixmilk.out");
    output_file << cows[0][1] << "\n";
    output_file << cows[1][1] << "\n";
    output_file << cows[2][1] << "\n";
}