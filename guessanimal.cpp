#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
 
int N;
vector<string> type[100];
 
int shared(int x, int y)
{
  int count = 0;
  vector<string> &string1 = type[x];
  vector<string> &string2 = type[y];
  for (int i=0; i<string1.size(); i++)
    for (int j=0; j<string2.size(); j++)
      if (string1[i] == string2[j]) count++;
  return count;
}

int main(void)
{
  ifstream file ("guess.in");
  file >> N;
  string s;
  for (int i=0; i<N; i++) {
    int K;
    file >> s >> K;
    for (int j=0; j<K; j++) {
      file >> s;
      type[i].push_back(s);
    }
  }
    
  int largest = 0;
  for (int i=0; i<N; i++)
    for (int j=i+1; j<N; j++)
      largest = max(largest, shared(i,j));
 
  ofstream fout ("guess.out");
  fout << largest+1 << "\n";
  return 0;
}