#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int num_books;
	cin >> num_books;
	long long sum = 0;
	long long big = 0;
	for (int x = 0; x < num_books; x++) {
		int c;
		cin >> c;
		if (c > big) big = c;
		sum+=c;
	}
	cout << max(sum, big*2);
}