#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
using namespace std;

int main() {
    ifstream file("lifeguards.in");
    vector<vector<int>> lifeguards;
    string line;
    getline(file, line);
    stringstream s(line);
    int num_lifeguards;
    s >> num_lifeguards;
    for (int x = 0; x < num_lifeguards; x++) {
        lifeguards.push_back({});
        getline(file, line);
        stringstream ss(line);
        int num;
        ss >> num;
        lifeguards[x].push_back(num);
        ss >> num;
        lifeguards[x].push_back(num);
    }
    int largest = 0;

    int sim [1001] = {0};
    for (int x = 0; x < num_lifeguards; x++){
        for (int y = lifeguards[x][0]; y < lifeguards[x][1]; y++){
            sim[y]++;
        }
    }
    for (int x = 0; x < 10; x++){
        cout << sim[x] << " ";
    }
    cout << "\n";

    for (int fired = 0; fired < num_lifeguards; fired++){
        for (int x = lifeguards[fired][0]; x < lifeguards[fired][1]; x++){
            sim[x]--;
        }

        int count = 0;

        for (int x = 0; x < 1001; x++){
            if (sim[x] > 0){
                count++;
            }
        }

        if (count > largest){
            largest = count;
        }

        cout << count;
        cout << "\n";
        cout << lifeguards[fired][0] << " " << lifeguards[fired][1];
        cout << "\n";

        for (int x = lifeguards[fired][0]; x < lifeguards[fired][1]; x++){
            sim[x]++;
        }
    }
    ofstream file_output("lifeguards.out");
    file_output << largest;
    file_output.close();
    file.close();

}