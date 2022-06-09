#include <iostream>
#include <bits/stdc++.h>
using namespace std;



void loop(string a, int x, int y, set<string>& d)
{
	
    if (x == y)
        //cout << a << endl;
		d.insert(a);
    else
    {

        for (int i = x; i <= y; i++)
        {
            swap(a[x], a[i]);
            loop(a, x+1, y, d);
            swap(a[x], a[i]);
        }
    }
}
 

int main()
{	
	set<string> sorted;
	string str;
    cin >> str;
    int n = str.size();
    loop(str, 0, n-1, sorted);

	cout << sorted.size() << endl;
	
	for (auto it = sorted.begin(); it !=sorted.end(); ++it) cout << *it << endl;
}