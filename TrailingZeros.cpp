#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int num;
	cin >> num;
	int i = 0;
	for (int x = 5; x <= num; x *= 5) {
		i+= num/x;
	}

	cout << i;

} 