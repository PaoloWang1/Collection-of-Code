#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int d;
	cin >> d;
	map<int, int> songs;
	vector<int> vector_songs;
	int counter = 0;
	int big = 0;
	for (int x = 0; x < d; x++) {
		int f;
		cin >> f;
		vector_songs.push_back(f);
	}
	int num = 0;
	for (int x = 0; x < d; x++) {
		if (songs.find(vector_songs[x]) != songs.end()) {
			if (songs[vector_songs[x]] >= num) {
				num = songs[vector_songs[x]] + 1;
			}
		}

		big = max(big, x - num + 1);
		songs[vector_songs[x]] = x;
	}

	cout << big;


	/*
	for (int x = 0; x < d; x++) {
		uint64_t f;
		cin >> f;
		bool found = false;
		current = numbers.size();
		for (int y = 0; y < numbers.size(); y++) {
			if (f == numbers[y]) {
				largest = max(largest, current);
				found = true;
				numbers.clear();
			}
		}
		if (!found) {
			numbers.push_back(f);
			largest = max(largest, current + 1);
		}
	}
	cout << largest;
	*/

}