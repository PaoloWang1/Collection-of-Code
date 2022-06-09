#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <istream>
#include <set>
using namespace std;

int main() {
    ifstream file("tttt.in");
    vector<string> board;
    string row;
    for (int rows = 0; rows < 3; rows++){
        getline(file, row);
        board.push_back(row);
    }
    
    vector<string> full;

    for (int rows = 0; rows < 3; rows++){
        full.push_back(board[rows]);
    }
    
    string r;
    for (int i=0; i<3; i++) {
        r += board[i][i];
    }
    full.push_back(r);
    r.clear();
    r += board[0][2];
    r += board[1][1];
    r += board[2][0];
    full.push_back(r);
    r.clear();
    for (int column = 0; column < 3; column++){
        for (int x = 0; x < 3; x++){
            r += char(board[x][column]);
        }
        full.push_back(r);
        r.clear();
    }


    /* build 

    vector<set<char>> checks;
    checks[0] is the set for row 0
    checks[1] is the set for row 1
    checks[2] is the set for row 2
    checks[3] is the set for col 0
    checks[4] is the set for col 1
    checks[5] is the set for col 2
    checks[6] is the set for forward cross
    checks[7] is the set for the reverse cross

    <set<char>> distinct_players;

    if distinct_playser.size() <= 2, then there're no teams!

    convert distinct_players into a vector of char

    vector<char> players(distinct_players.begin(), distinct_players.end());

    create pairs using players vector.  

    player[0], player[1] 
    player[0], player[2]
    ...

    check_pair_wins(char p1, p2) {}
    iterate through checks vector,
    if checks[i].size() == 2, if checks[i].find(player[0]) == true and checks[i].find(player[1]) == true
    }
    returns true if the team can check_pair_wins
    false otherwise

    vector<set<char>> winning_team;

    if checks[i].size() == 2
        winning_team.find(checks[i]) if false
        winning_team.push_back(checks[i])

*/


    



    for (int x = 0; x < full.size(); x++){
        for (int y = 0; y < 3; y++){
            cout << full[x][y];
        }
        cout << "\n";
    }

    int team = 0;
    int solo = 0;

    set <char> solowin;
    set<set <char>> teamwin;

    for (int pos = 0; pos < full.size(); pos++){
        set<char> repeated;
        repeated.insert(full[pos].begin(), full[pos].end());
        if (repeated.size() == 1) solowin.insert(full[pos][0]);
    }

    for (int left = 0; left < full.size(); left++){
        set<char> repeated;
        repeated.insert(full[left].begin(), full[left].end());
        if (repeated.size() == 2) teamwin.insert(repeated);
    }

    ofstream file_output("tttt.out");
    file_output << solowin.size() << "\n" << teamwin.size();
}