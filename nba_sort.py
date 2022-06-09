import json

with open("nba-teams-better-pretty.json", "r") as json_files:
    s_json = "".join(json_files.readlines())
    team_stats = json.loads(s_json)

with open("nba-players-better-pretty.json", "r") as json_files:
    s_json1 = "".join(json_files.readlines())
    players_stats = json.loads(s_json1)
    
#pts, field goal percentage fg_PCT, assists per game ast, total rebounds reb

info = {"PTS" : "Points Per Game:", "FG_PCT" : "Field Goal Percentage:", "AST" : "Assists Per Game", "REB" : "Total Rebounds"}



for category, message in info.items():
    team_pts=[]
    for team in team_stats:
        team_pts.append((team["TEAM_ID"], team[category], team["TEAM_NAME"]))
    team_sorted_pts = sorted(team_pts)
    team_sorted_pts = team_sorted_pts[::-1]
    print(message)
    for y in range(3):
        print("#"+ str(y)+ ":", str(team_sorted_pts[y]))
        # PLAYER_NAME, PTS_RANK
        teamID = team_sorted_pts[y][2]
        players_in_team = []
        for player in range(len(players_stats)):
            if players_stats[player]["TEAM_ID"] == teamID:
                players_in_team.append((players_stats[player][str(category+"_RANK")], players_stats[player]["PLAYER_NAME"]))
        players_in_team = sorted(players_in_team)
        players_in_team = players_in_team[::-1]
        print()
        for p in range(3):
            print(players_in_team[p][1], "#" + str(players_in_team[p][0]), str(category), "ranking")
        print()
    print()
    print()
