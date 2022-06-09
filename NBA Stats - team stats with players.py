import requests
import json

URL_league_leaders = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2018-19&SeasonType=Regular+Season&StatCategory=PTS"
#URL="https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision="
#URL="https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="
URL_team="https://stats.nba.com/js/data/widgets/teams_landing_inner.json"
URL_player="https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
URL_curry_shot_data="https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=2018-19&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=201939&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID="
params=""

def get_request(weburl):
  return requests.get(
    url=weburl,
    params=params,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    })

team_response=get_request(URL_team).content.decode()
stats_team=json.loads(team_response)

player_response=get_request(URL_player).content.decode()
stats_player=json.loads(player_response)

top_teams=[]
print("Top 3 Points Per Game Teams:")
team_stats=stats_team["items"][0]["items"][0]["teamstats"]
for i in range(3):
  print (team_stats[i]['TEAM_CITY'],
         team_stats[i]['TEAM_NAME'])
  top_teams.append(team_stats[i]['TEAM_ABBREVIATION'])

player_stats=stats_player['resultSets'][0]['rowSet']

# build a dictionary of teams with a list of players with each player's data:
#                             (player name, pts, FG%, assists, rebounds)
team_player_data={}
for player in player_stats:
  if player[3] not in team_player_data.keys():
    team_player_data[player[3]]=[]
  team_player_data[player[3]].append(
    (player[1], player[29], player[12], player[22], player[21]))

# As an example, let's get GSW (Golden State Warrior) top pts players
GSW_players=team_player_data['GSW']
GSW_top_scorers=sorted(GSW_players, key=lambda player:player[1], reverse=True)
print("\nGolden State's top 3 scorers: ")
for i in range(3):
  print(GSW_top_scorers[i][0])

GSW_top_FG=sorted(GSW_players, key=lambda player:player[2], reverse=True)
print("\nGolden State's top 3 FG% players: ")
for i in range(3):
  print(GSW_top_FG[i][0])

GSW_top_assists=sorted(GSW_players, key=lambda player:player[3], reverse=True)
print("\nGolden State's top 3 assists players: ")
for i in range(3):
  print(GSW_top_assists[i][0])









  





  





