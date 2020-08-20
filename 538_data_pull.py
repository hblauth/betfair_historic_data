import pandas as pd
import datetime as dt

spi_url = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv'

spi_data = pd.read_csv(spi_url)

spi_data.shape



lookup_date = dt.date.today().strftime('%Y-%m-%d')

matches_today = spi_data[spi_data['date'] == lookup_date]

print(matches_today[['league', 'team1', 'team2']])

for idx, match in matches_today.iterrows():
    league = match['league']
    match_day = match['date']
    home_team = match['team1']
    away_team = match['team2']
    home_odds = match['prob1']
    away_odds = match['prob2']
    draw_odds = match['probtie']

    print(F'On: {match_day} in {league}\n'
          F'{home_team} win probability: {home_odds}\n'
          F'{away_team} win probability: {away_odds}\n'
          F'Draw: {draw_odds}\n')
