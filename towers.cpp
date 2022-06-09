#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int d;
	cin >> d;
	multiset<int> towers;
	for (int x = 0; x < d; x++) {
		uint64_t f;
		cin >> f;
		auto find = towers.upper_bound(f);
		if (find != towers.end()) {
			towers.erase(find);
		}
		towers.insert(f);
	}
	cout << towers.size();
}
//10
//10 4 5 9 4 10 2 7 4 6