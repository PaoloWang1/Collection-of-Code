#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int d;
	cin >> d;
	vector<int> nums;
	for (int x = 0; x < d; x++) {
		int f;
		cin >> f;
		nums.push_back(f);
	}
	sort(nums.begin(), nums.end());
	int sum = 0;
	for (int x = 0; x < d && sum <= nums[x]; x++) {
		sum += nums[x];
	}
	cout << sum;
}