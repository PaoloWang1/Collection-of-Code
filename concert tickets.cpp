#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	int c;
	cin >> c;
	multiset<int, greater<int>> tickets;

	for (int x = 0; x < t; x++) {
		int g;
		cin >> g;
		tickets.insert(g);
	}

	multiset<int, greater<int>>::iterator find;

	for (int x = 0; x < c; x++) {
		int g;
		cin >> g;
		find = tickets.lower_bound(g);
		if (find == tickets.end()) {
			cout << -1 << "\n";
		} 
		else {
			cout << *find << "\n";
			tickets.erase(find);
		}
	}
} 		