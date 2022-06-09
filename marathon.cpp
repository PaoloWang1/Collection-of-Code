#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
using namespace std;

int main() {
    ifstream file("marathon.in");
    vector<vector<int>> stops;
    string line;
    getline(file, line);
    stringstream s(line);
    int num_check;
    s >> num_check;
    for (int checks = 0; checks < num_check; checks++) {
        stops.push_back({});
        getline(file, line);
        stringstream ss(line);
        int num;
        ss >> num;
        stops[checks].push_back(num);
        ss >> num;
        stops[checks].push_back(num);
    }
    ofstream file_output("marathon.out");
    int biggest = 0;
    int length = 0;
    int length2 = 0;
    for (int skip = 1; skip < stops.size() - 1; skip++) {
        length = abs(stops[skip + 1][0] - stops[skip - 1][0]) + abs(stops[skip + 1][1] - stops[skip - 1][1]);

        length2 = abs(stops[skip][0] - stops[skip - 1][0]) + abs(stops[skip][1] - stops[skip - 1][1]) + abs(stops[skip + 1][0] - stops[skip][0]) + abs(stops[skip + 1][1] - stops[skip][1]);

        int skipped = length2 - length;

        if (skipped > biggest) {
            biggest = skipped;
        }
    }

    int total = 0;
    for (int x = 1; x < num_check; x++){
        total += abs(stops[x][0] - stops[x-1][0]) + abs(stops[x][1] - stops[x-1][1]);
    }
    total = total - biggest;

    file_output << total;
    file.close();
    file_output.close();
}