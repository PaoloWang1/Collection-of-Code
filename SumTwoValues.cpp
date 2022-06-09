#include <bits/stdc++.h>
using namespace std;

void getIndex(vector<int> v, int K)
{
    auto it = find(v.begin(), v.end(), K);
    if (it != v.end())
    {
        int index = it - v.begin();
        cout << index;
    }
}



int main() {
	int n, x;
	cin >> n >> x;
	vector<int> pos;
	vector<int> nums;
	for (int i = 0; i < n; i++) {
		int d;
		cin >> d;
		nums.push_back(d);
		pos.push_back(d);
	}

	sort(nums.begin(), nums.end());
	int n1, n2;
	bool found = false;
	for (int a = 0; a < n; a++) {
		bool check = true;
		n1 = nums[a];
		bool high = false;
		int index = n/2;
		if (nums[index] + n1 > x) {
			high = true;
		}
		while (check && !found) {
			n2 = nums[index];
			if (n1 + n2 == x) {
				found = true;
				break;
			}
			if (high) {
				index--;
				if (n1 + nums[index] < x) {
					check = false;
				}
			} else {
				index++;
				if (n1 + nums[index] > x) {
					check = false;
				}
			}
		}

		if (found) {
			break;
		}
	}

	if (!found) {
		cout << "IMPOSSIBLE";
	} else {
		getIndex(pos, n1);
		cout << " ";
		getIndex(pos, n2);
	}

} 