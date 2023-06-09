import csv

def get_win_rates(floor):
    with open(f'winrates/floor{floor}.csv', newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def get_pick_rates(floor):
    with open(f'pickrates/floor{floor}.csv', newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def get_matchups(floor):
    with open(f'matchup/floor{floor}.csv', newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def get_all_matchups(char):
    with open(f'matchup/allfloors.csv', newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader if row['Character 1'] == char]
    return data