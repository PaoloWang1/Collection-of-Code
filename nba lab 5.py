import json

with open("player-shots.json", "r") as json_files:
    s_json1 = "".join(json_files.readlines())
    player_stats = json.loads(s_json1)

with open("nba-players-better-pretty.json", "r") as json_files:
    s_json1 = "".join(json_files.readlines())
    player_stats = json.loads(s_json1)

pts_rank = sorted(player_stats, key = lambda x:x["PTS"], reverse = True)
for i in pts_rank[:10]:
    print(i["PLAYER_NAME"], i["PTS"])
