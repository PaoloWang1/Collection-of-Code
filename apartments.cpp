#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
	int n, m, k;
	cin >> n >> m >> k;
	vector<int> desired;
	vector<int> apartments;

	for (int x = 0; x < n; x++) {
		int g;
		cin >> g;
		desired.push_back(g);
	}

	for (int x = 0; x < m; x++) {
		int g;
		cin >> g;
		apartments.push_back(g);
	}

	int count = 0;

	sort(desired.begin(), desired.end());
	sort(apartments.begin(), apartments.end());

	int a = 0;
	int d = 0;

	

	while (d < desired.size() && a < apartments.size()) {
        //cout << desired[d] << " " << apartments[a] << "\n";
		if ((desired[d] <= apartments[a] + k) && (desired[d] >= apartments[a] - k)) {
			count ++;
			d++;
			a++;
		} else if (desired[d] < apartments[a] - k) {
			d++;
		} else if (desired[d] > apartments[a] + k) {
			a++;
		}
	}

	cout << count;
} 