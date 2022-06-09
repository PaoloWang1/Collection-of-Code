import json

file = open("nba-teams-pretty.json", "r")
teams = json.load(file)

fg_percent = [(team["FG_PCT"], team["TEAM_NAME"]) for team in teams]
fg_pct_sorted = sorted(fg_percent)
print(fg_pct_sorted)
