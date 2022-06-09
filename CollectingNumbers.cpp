#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int d;
	cin >> d;
	int pos[d];
	int counter = 0;
	for (int x = 0; x < d; x++) {
		int g;
		cin >> g;
		pos[g-1] = x;
	}
	int f = 1;
	for (int x = 1; x < d; x++) {
		if (pos[x] < pos[x-1]) {
			f++;
		}
	}
	cout << f;
}