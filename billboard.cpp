#include <iostream>
#include <sstream>
#include <istream>
#include <fstream>
#include <vector>
using namespace std;

int intersect(vector<int> rect1, vector<int> rect2) {
    int x_val = min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]);
    int y_val = min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]);
    
    x_val = max(0, x_val);
    y_val = max(0, y_val);

    return x_val * y_val;
}

int main() {
    ifstream file("billboard.in");
    vector<int> billboard1;
    vector<int> billboard2;
    vector<int> steak;
    string row;
    getline(file, row);
    stringstream s(row);
    for (int x = 0; x < 4; x++){
        int num;
        s >> num;
        billboard1.push_back(num);
    }
    getline(file, row);
    stringstream ss(row);
    for (int x = 0; x < 4; x++){
        int num;
        ss >> num;
        billboard2.push_back(num);
    }
    getline(file, row);
    stringstream sss(row);
    for (int x = 0; x < 4; x++){
        int num;
        sss >> num;
        steak.push_back(num);
    }


    int area1 = (billboard1[2] - billboard1[0]) * (billboard1[3] - billboard1[1]);
    int area2 = (billboard2[2] - billboard2[0]) * (billboard2[3] - billboard2[1]);

    int total_area = area1 + area2;

    total_area -= intersect(billboard1, steak) + intersect(billboard2, steak);
    
    ofstream file_output("billboard.out");
    file_output << total_area;
    file_output.close();
    file.close();
}