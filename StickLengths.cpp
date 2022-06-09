#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int d;
	cin >> d;
	int sum = 0;
	vector<int> numbers;
	for (int x = 0; x < d; x++) {
		int f;
		cin >> f;
		numbers.push_back(f);
	}
	sort(numbers.begin(), numbers.end());
	int median = numbers[d/2];
	uint64_t diff = 0;
	for (int x = 0; x < d; x++) {
		diff += abs(median-numbers[x]);
	}

	cout << diff;




	/*int avg = sum/d;
	int diff = 0;
	int diff1 = 0;
	for (int x = 0; x < d; x++) {
		diff += abs(avg - numbers[x]);
		diff1 += abs(avg+1-numbers[x]);
	}

	if (diff > diff1) {
		cout << diff1;
	}else {
		cout << diff;
	}

	*/


	

}