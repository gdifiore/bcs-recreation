from fetchers.ap_poll import fetch_ap_poll_rankings
from fetchers.bcf_toys_fei import fetch_bcs_toys_fei_rankings
from fetchers.colley import fetch_colley_matrix_table
from fetchers.espn_fpi import fetch_espn_fpi_rankings
from fetchers.massey import fetch_massey_ratings
from fetchers.power_rankings import fetch_power_ranking_rankings
from fetchers.sagarin import parse_college_football_rankings
from fetchers.usa_today_poll import fetch_usa_today_rankings
from utils.standardize_team_names import standardize_team_names
import pandas as pd
import numpy as np

def normalize_rankings(df, team_col='Team', rank_col='Rank', points_col=None, normalize_by=None):
    """
    Normalizes team names and converts rankings to a standardized format.

    Parameters:
    - df: DataFrame with rankings
    - team_col: Column name containing team names
    - rank_col: Column name containing rankings
    - points_col: Column name containing points (if available)
    - normalize_by: Value to normalize points by (if applicable)

    Returns:
    - Normalized DataFrame with standardized team names and scores
    """
    normalized_df = df.copy()

    normalized_df['team'] = normalized_df[team_col].apply(standardize_team_names)

    normalized_df['rank'] = normalized_df[rank_col]

    if points_col is not None and normalize_by is not None and points_col in normalized_df.columns:
        normalized_df['normalized_points'] = normalized_df[points_col] / normalize_by
    elif 'Normalized Score' in normalized_df.columns:
        # For fetchers that already provide normalized scores
        normalized_df['normalized_points'] = normalized_df['Normalized Score']
    else:
        # For rankings that only have ranks, convert to points (25 for 1st, 24 for 2nd, etc.)
        normalized_df['points'] = normalized_df['rank'].apply(lambda x: max(26 - int(x), 0) if int(x) <= 25 else 0)
        normalized_df['normalized_points'] = normalized_df['points'] / 25

    # Select only the columns we need
    result_df = normalized_df[['team', 'rank', 'normalized_points']]

    return result_df

def calculate_computer_composite(rankings_list):
    """
    Calculate computer composite rankings by dropping highest and lowest for each team.

    Parameters:
    - rankings_list: List of DataFrames with normalized rankings

    Returns:
    - DataFrame with composite computer rankings
    """
    # Combine all rankings into a single DataFrame
    all_teams = set()
    for df in rankings_list:
        all_teams.update(df['team'].tolist())

    # For each team, collect all rankings
    team_rankings = {team: [] for team in all_teams}
    ranking_names = ["FPI", "Sagarin", "FEI", "Power Rank", "Massey", "Colley"]

    for i, df in enumerate(rankings_list):
        ranking_name = ranking_names[i] if i < len(ranking_names) else f"Ranking {i+1}"
        print(f"Processing {ranking_name}...")
        for team in all_teams:
            # If team is in current ranking, add its points
            if team in df['team'].values:
                points = df.loc[df['team'] == team, 'normalized_points'].iloc[0]
                team_rankings[team].append(points)
            else:
                # If team is not ranked, assign 0 points
                team_rankings[team].append(0)

    # Drop highest and lowest for each team
    composite_scores = []
    for team, scores in team_rankings.items():
        if len(scores) >= 3:  # Only process if we have at least 3 rankings
            # Sort scores
            sorted_scores = sorted(scores)

            # Drop lowest and highest
            if len(sorted_scores) > 2:
                middle_scores = sorted_scores[1:-1]
            else:
                middle_scores = sorted_scores

            # Calculate average of remaining scores
            # Instead of dividing by 100, we're directly averaging the normalized scores
            avg_score = sum(middle_scores) / len(middle_scores)
            composite_scores.append({
                'team': team,
                'computer_score': avg_score
            })

    return pd.DataFrame(composite_scores)

def handle_unranked_teams(df1, df2, name1='poll1', name2='poll2'):
    """
    Handle teams ranked in one poll but not another.

    Parameters:
    - df1, df2: Two ranking DataFrames to compare
    - name1, name2: Names to use for the polls

    Returns:
    - DataFrame with combined rankings
    """
    # Get all unique teams
    all_teams = set(df1['team']).union(set(df2['team']))

    # For each poll, if a team is not ranked, assign a value just below the last ranked team
    max_rank1 = df1['rank'].max() + 1
    max_rank2 = df2['rank'].max() + 1

    combined_data = []

    for team in all_teams:
        team_data = {'team': team}

        # Get rank from first poll
        if team in df1['team'].values:
            rank1 = df1.loc[df1['team'] == team, 'rank'].iloc[0]
            norm_score1 = df1.loc[df1['team'] == team, 'normalized_points'].iloc[0]
        else:
            rank1 = max_rank1
            norm_score1 = 0

        # Get rank from second poll
        if team in df2['team'].values:
            rank2 = df2.loc[df2['team'] == team, 'rank'].iloc[0]
            norm_score2 = df2.loc[df2['team'] == team, 'normalized_points'].iloc[0]
        else:
            rank2 = max_rank2
            norm_score2 = 0

        team_data[f'{name1}_rank'] = rank1
        team_data[f'{name2}_rank'] = rank2
        team_data[f'{name1}_score'] = norm_score1
        team_data[f'{name2}_score'] = norm_score2

        combined_data.append(team_data)

    return pd.DataFrame(combined_data)

def bcs_ranking_calculator():
    """
    Calculate BCS rankings using the specified formula.
    """
    print("Fetching rankings from all sources...")

    print("Processing AP Poll...")
    ap_poll = fetch_ap_poll_rankings()

    if 'Normalized Score' in ap_poll.columns:
        ap_norm = normalize_rankings(ap_poll)
    else:
        ap_norm = normalize_rankings(ap_poll)

    print("Processing USA Today Poll...")
    usa_today = fetch_usa_today_rankings()

    if 'Normalized Score' in usa_today.columns:
        usa_norm = normalize_rankings(usa_today)
    else:
        usa_norm = normalize_rankings(usa_today)

    # Handle teams in one poll but not the other
    print("Combining human polls...")
    human_polls = handle_unranked_teams(ap_norm, usa_norm, name1='ap', name2='usa')

    human_polls['human_score'] = (human_polls['ap_score'] + human_polls['usa_score'])

    print("Processing computer rankings...")

    computer_dfs = []

    print("Processing ESPN FPI...")
    fpi = fetch_espn_fpi_rankings()
    computer_dfs.append(normalize_rankings(fpi))

    print("Processing Sagarin...")
    sagarin = parse_college_football_rankings()
    computer_dfs.append(normalize_rankings(sagarin))

    print("Processing FEI Ratings...")
    fei = fetch_bcs_toys_fei_rankings()
    computer_dfs.append(normalize_rankings(fei))

    print("Processing Power Rankings...")
    power_rank = fetch_power_ranking_rankings()
    computer_dfs.append(normalize_rankings(power_rank))

    print("Processing Massey Ratings...")
    massey = fetch_massey_ratings()
    computer_dfs.append(normalize_rankings(massey))

    print("Processing Colley Matrix...")
    colley = fetch_colley_matrix_table()
    computer_dfs.append(normalize_rankings(colley))

    print("Calculating computer composite rankings...")
    computer_rankings = calculate_computer_composite(computer_dfs)

    print("Merging human and computer rankings...")
    final_df = pd.merge(human_polls, computer_rankings, on='team', how='outer')

    final_df = final_df.fillna(0)

    # Calculate BCS score (human_score + computer_score)
    final_df['bcs_score'] = ( final_df['human_score'] + final_df['computer_score'] ) / 3

    # Sort by BCS score and assign rankings
    final_df = final_df.sort_values(by='bcs_score', ascending=False).reset_index(drop=True)
    final_df['bcs_rank'] = final_df.index + 1

    # Select and reorder columns for display
    final_cols = [
        'bcs_rank', 'team', 'bcs_score',
        'ap_rank', 'usa_rank', 'human_score', 'computer_score'
    ]

    final_df = final_df[final_cols]

    return final_df
