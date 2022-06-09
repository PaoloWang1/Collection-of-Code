import json

with open('nba-teams-better-pretty.json','r') as json_file:
  team_stats=json.load(json_file)

with open('nba-players-better-pretty.json','r') as json_file:
    player_stats = json.loads(json_file)
    

info={ 'PTS':'Top 3 Scoring Teams:',      # category:message
       'FG_PCT':'Top 3 Goal Percentage Teams:',
       'AST':'Top 3 Assist Teams:',
       'REB':'Top 3 Rebounding Teams:'}

# Using list comprehension!
for category, message in info.items():
  team_pts=[(team[category], team['TEAM_NAME'], team['TEAM_ID']) for team in team_stats]
  sorted_team_stats=sorted(team_pts,reverse=True)
  print(message)
  for index,team in enumerate(sorted_team_stats[:3]):
    print('#'+str(index+1)+':', team[1])
  print()



'''
Using For loop with append to list

for category, message in info.items():
  team_pts=[]
  for team in team_stats:
          team_pts.append( (team[category], team['TEAM_NAME'], team['TEAM_ID']) )
  sorted_team_stats=sorted(team_pts,reverse=True)
  print(message)
  for index,team in enumerate(sorted_team_stats[:3]):
    print('#'+str(index+1)+':', team[1])
  print()
'''
