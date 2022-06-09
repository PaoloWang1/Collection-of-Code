#include <iostream>
#include <fstream>
#include <vector>
#include <istream>
#include <sstream>
using namespace std;

int main() {
	ifstream file("crossroad.in");
	ofstream output("crossroad.out");
	string d;
	int f;
	getline(file, d);
	stringstream s(d);
	s >> f;
	vector<int> cow_log;
	vector<bool> cow_first;
	int num_move = 0;


	for (int i = 0; i < 10; i++) {
		cow_log.push_back(0);
		cow_first.push_back(true);
	}

	for (int x = 0; x < f; x++) {
		int num;
		int pos;
		getline(file, d);
		stringstream ss(d);
		ss >> num >> pos;

		if (cow_first[num - 1]) {
			cow_log[num - 1] = pos;
			cow_first[num - 1] = false;
		} else {
			if (pos != cow_log[num - 1]) {
				num_move++;
				cow_log[num - 1] = pos;
				cout << num << " " << pos << "\n";
			}
		}
	}

	output << num_move;
} 