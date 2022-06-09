//#include <bits/stdc++.h>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	string a;
	cin >> a;
	char odd_char;
	bool odds = false;
	vector<char> char_nums;
	/*
	for (int x = 0; x < a.size(); x++) {
		char_nums.push_back(a[x]);	
	}
	sort(char_nums.begin(), char_nums.end());
	char_nums.erase(unique(char_nums.begin(), char_nums.end()), char_nums.end() );
	int occurances[char_nums.size()];
	bool no = true;

	for (int x = 0; x < char_nums.size(); x++) {
		int d = count(a.begin(), a.end(), a[x]);
		occurances[x] = d;
		if ((d % 2 == 1) && !odds) {
			odds = true;
			odd_char = a[x];
			char_nums.erase(char_nums.begin() + x, char_nums.begin() + x + 1);
		}  else{
			cout << "NO SOLUTION";
			break;
			no = false;
		}
	}

	string returned1 = "";
	string odd = "";
	if (no) {
		for (int x = 0; x < char_nums.size(); x++) {
			if (occurances[x] % 2 == 0) {
				for (int y = 0; y < occurances[x]/2; y++) {
					returned1 += char_nums[x];
				}
			} else {
				for (int e = 0; e < occurances[x]/2; e++) {
					odd += char_nums[x];
				}
			}
		}
		string other = returned1 + odd;
		reverse(other.begin(), other.end());
		cout << returned1 << "\n" << char(odd_char) << other;
	}
	*/
	int occurances[26] = {0};
	for (int x = 0; x < a.size(); x++) {
		int letter = (int) a[x];
		occurances[letter - 65]++;
	}
	int counter = 0;
	int times;
	string odd = "";
	for (int x = 0; x < 26; x++) {
		if (occurances[x] % 2 == 1) {
			counter++;
			odd = (char) x + 65; 
			occurances[x]--;
		}
	}
	string returned = "";
	if (counter > 1) { 
		cout << "NO SOLUTION";
	} else {
		for (int x = 0; x < 26; x++) {
			returned.insert(0, occurances[x]/2, (char)x + 'A');
			returned.insert(returned.size(), occurances[x]/2, (char)x + 'A');
		}
		returned.insert(returned.size()/2, odd);	
		cout << returned;
	}
	

}