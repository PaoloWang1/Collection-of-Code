#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	long long num_machines;
	cin >> num_machines;
	long long num_prod;
	cin >> num_prod;
	vector<int> machines;
	for (int f = 0; f < num_machines; f++) {
		int d;
		cin >> d;
		machines.push_back(d);
	}
	
	long long low = 0;
	long long high = machines[0]*num_prod;
	long long ans = machines[0]*num_prod;

	while (low <= high) {
		long long mid = (low+high)/2;
		long long prod = 0;
		for (int x = 0; x < num_machines; x++) {
			prod += min(mid/machines[x],(long long)1e9);
		}
		if (prod >= num_prod) {
			if (mid < ans) {
				ans = mid;
			} 
			high = mid-1;
		} else {
			low = mid+1;
		}
	}
	cout << ans;
}