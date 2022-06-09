#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
	ifstream file("factory.in");
	ofstream output_file("factory.out");
	int num;
	string row;
	int input[101];
	int output[101];
	getline(file, row);
	stringstream s(row);
	s >> num;
	for (int x = 0; x < 101; x++) {
		input[x] = 0;
		output[x] = 0;
	}
	for (int x = 0; x < num - 1; x++) {
		getline(file, row);
		stringstream ss(row);
		int a;
		int b;
		ss >> a >> b;
		input[a]++;
		output[b]++;
		cout << a << " " << b << "\n";
	}

	for (int x = 0; x++;)
	cout << num << "\n"; 
	int ans = -1;
	for (int x=1; x<=num; x++) {
		cout << x << " ";
		if (input[x] == 0 && ans != -1) {
			ans = -1;
			break;
			cout << input[x] << "\n";
		}
		if (input[x] == 0) {
			ans = x;
			cout << input[x] << "\n";
		}
	}
	output_file << ans << "\n";
}