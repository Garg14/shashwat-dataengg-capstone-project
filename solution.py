import pandas as pd
import numpy as np

def load_players(file_path):
    return pd.read_csv('C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\cricket_players_analysis\\data\\players.csv')

def load_matches(file_path):
    return pd.read_csv('C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\cricket_players_analysis\\data\\matches.csv')

def merge_players_matches(players, matches):
    merged = matches.merge(players, on='PlayerID', how='left')
    ordered = [
        'PlayerID', 'Name', 'Team', 'Role', 'Age',
        'MatchID', 'Runs', 'Balls', 'Fours', 'Sixes',
        'Wickets', 'Catches', 'Date'
    ]
    return merged[ordered]

def total_runs_per_team(data):
    return data.groupby('Team', as_index=False)['Runs'].sum()

def calculate_strike_rate(data):
    temp = data.copy()
    temp['StrikeRate'] = temp['Runs'] / temp['Balls'] * 100
    return temp[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]

def runs_agg_per_player(data):
    grouped = data.groupby(['PlayerID', 'Name'], as_index=False)['Runs']
    stats = grouped.agg(['mean', 'max', 'min']).rename(
        columns={'mean':'mean', 'max':'max', 'min':'min'}
    )
    return stats[['PlayerID', 'Name', 'mean', 'max', 'min']]

def avg_age_by_role(players):
    return players.groupby('Role', as_index=False)['Age'].mean()

def total_matches_per_player(matches):
    counts = matches.groupby('PlayerID', as_index=False)['MatchID'].nunique()
    return counts.rename(columns={'MatchID': 'MatchCount'})

def top_wicket_takers(data):
    grouped = data.groupby(['PlayerID', 'Name'], as_index=False)['Wickets'].sum()
    top3 = grouped.sort_values('Wickets', ascending=False).head(3)
    return top3[['PlayerID', 'Name', 'Wickets']]

def avg_strike_rate_per_team(data):
    agg = data.groupby('Team', as_index=False).agg({'Runs':'sum', 'Balls':'sum'})
    agg['StrikeRate'] = agg['Runs'] / agg['Balls'] * 100
    return agg[['Team', 'StrikeRate']]

def catch_to_match_ratio(data):
    catches = data.groupby('PlayerID')['Catches'].sum()
    matches = data.groupby('PlayerID')['MatchID'].nunique()
    ratio = (catches / matches).reset_index(name='CatchToMatchRatio')
    return ratio

