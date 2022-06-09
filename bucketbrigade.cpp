#include <iostream>
#include <istream>
#include <fstream>
#include <cstdio>
#include <sstream>
using namespace std;

int main()
{
	ifstream file("buckets.in");
	ofstream output_file("buckets.out");
	int barny = 0, barnx = 0, rocky = 0, rockx = 0, lakey = 0, lakex = 0;
	for (int i = 0; i < 10; i++)
	{
		string row;
		getline(file, row);

		for (int j = 0; j < 10; j++)
		{
			if (row[j] == 'B')
			{
				barny = i;
				barnx = j;
			}
			else if (row[j] == 'R')
			{
				rocky = i;
				rockx = j;
			}
			else if (row[j] == 'L')
			{
				lakey = i;
				lakex = j;
			}
		}
	}

	int cows = abs(barnx - lakex) + abs(barny - lakey) - 1;


	if (barny == lakey && rocky == barny && ((lakex < rockx && rockx < barnx) || (barnx < rockx && rockx < lakex))){
		cows += 2;
	} else if (barnx == lakex && rockx == barnx && ((lakey < rocky && rocky < barny) || (barny < rocky && rocky < lakey))){
		cows += 2;
	}
	output_file << cows << "\n";
}