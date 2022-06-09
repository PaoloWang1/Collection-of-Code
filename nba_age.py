import json

with open("nba-teams-better-pretty.json", "r") as json_files:
    s_json = "".join(json_files.readlines())
    team_stats = json.loads(s_json)

with open("nba-players-better-pretty.json", "r") as json_files:
    s_json1 = "".join(json_files.readlines())
    players_stats = json.loads(s_json1)


for team in team_stats:
    players_in_team = []
    for player in players_stats:
        if player["TEAM_ID"] == team["TEAM_ID"]:
            players_in_team.append((player["PTS_RANK"], player["PLAYER_NAME"], str(player["AGE"])))
    players_in_team = sorted(players_in_team)
    print(team["TEAM_NAME"])
    print(players_in_team)
    for p in range(5):
        print(str(p+1) + "." + players_in_team[p][1] + ":" , players_in_team[p][2])
