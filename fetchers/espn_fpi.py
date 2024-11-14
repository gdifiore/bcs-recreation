import pandas as pd
import requests
from bs4 import BeautifulSoup

def parse_fpi_rankings():
    """
    Scrapes and parses ESPN's FPI rankings, handling their split table structure.
    Returns a pandas DataFrame with team names and ranks.
    """
    url = "https://www.espn.com/college-football/fpi/_/season/2023"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Get team names from the left table
        team_table = soup.find('div', class_='Table__Colgroup')
        team_rows = team_table.find_all('tr')[1:]  # Skip header row
        teams = [row.find('td').text.strip() for row in team_rows]

        # Get ranks from the scrollable table
        rank_table = soup.find('div', class_='Table__Scroller')
        rank_rows = rank_table.find_all('tr')[1:]  # Skip header row
        ranks = [row.find_all('td')[1].text.strip() for row in rank_rows]  # Second column

        df = pd.DataFrame({
            'Rank': pd.to_numeric(ranks),
            'Team': teams
        })

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

if __name__ == "__main__":
    espn_fpi_df = parse_fpi_rankings()
    print(espn_fpi_df)
