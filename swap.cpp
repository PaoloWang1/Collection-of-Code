#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
using namespace std;


int check_swap(vector<int> cows, int first_min, int first_max, int second_min, int second_max) {
    vector<int> cow_sim = cows;
    reverse(cow_sim.begin() + first_min - 1, cow_sim.begin() + first_max);
    reverse(cow_sim.begin() + second_min - 1, cow_sim.begin() + second_max);
    int times = 1;
    while (cow_sim != cows) {
        reverse(cow_sim.begin() + first_min - 1, cow_sim.begin() + first_max);
        reverse(cow_sim.begin() + second_min-1, cow_sim.begin() + second_max);
        times++;
    }   
    return times; 
}

int main() {
    ifstream file("swap.in");
    int num_cows;
    int num_times;
    int first_min;
    int first_max;
    int second_min;
    int second_max;
    string line;
    getline(file, line);
    stringstream s(line);
    s >> num_cows >> num_times;
    getline(file, line);
    stringstream ss(line);
    ss >> first_min >> first_max;
    getline(file, line);
    stringstream sss(line);
    sss >> second_min >> second_max;


    vector<int> cows;
    for (int x = 1; x <= num_cows; x++){
        cows.push_back(x);
    }
    int times = check_swap(cows, first_min, first_max, second_min, second_max);
    num_times = num_times % times;
    for (int x = 0; x < num_times; x++) {
        reverse(cows.begin() + first_min-1, cows.begin() + first_max);
        reverse(cows.begin() + second_min-1, cows.begin() + second_max);
    }
    cout << "times " << times <<  "num_times " << num_times;
    ofstream file_output("swap.out");
    for (int x = 0; x < num_cows; x++) {
        file_output << cows[x] << "\n";
    }
    file_output.close();
    file.close();
}