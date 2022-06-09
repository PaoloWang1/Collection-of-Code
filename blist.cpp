#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    ifstream file("8.in");
    string row;
    getline(file, row);
    stringstream s(row);
    int num_cows;
    s >> num_cows;
    int start[num_cows];
    int end[num_cows];
    int buckets[num_cows];
    for (int x = 0; x < num_cows; x++) {
        int num;
        getline(file, row);
        stringstream ss(row);
        ss >> num;
        start[x] = num;
        ss >> num;
        end[x] = num;
        ss >> num;
        buckets[x] = num;
    }

    int biggest = 0;
    for (int time = 0; time < num_cows; time++) {
        int current = buckets[time];
        for (int cow = 0; cow < num_cows; cow++) {
            if (cow != time) {
                if (start[time] <= end[cow] && start[time] >= start[cow]) {
                    current += buckets[cow];
                }
            }
        }

        if (current > biggest) biggest = current;

        /*
        for (int cow = 0; cow < num_cows; cow++) {
            if (cow != time) {
                if (end[time] <= end[cow] && end[time] >= start[cow]) {
                    current += buckets[cow];
                }
            }
        }

        if (current > biggest) biggest = current;

    */
    }

    ofstream output("8.out");
    output << biggest;


}