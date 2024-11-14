import pandas as pd
import requests
from bs4 import BeautifulSoup

# Constants for USA Today Poll
USA_TODAY_URL = "https://sportsdata.usatoday.com/football/ncaaf/coaches-poll"  # Replace with the actual URL
PERFECT_SCORE = 1375  # Perfect score for USA Today Poll

def fetch_and_parse():
    """
    Scrapes and parses the USA Today Coaches Poll data for college football teams.
    Returns a pandas DataFrame with rank, team, points percentage, and record.
    Points are normalized as a percentage of maximum possible points (1375).
    """

    try:
        # Make request to the website
        response = requests.get(USA_TODAY_URL)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the poll table (this selector might need updating based on site changes)
        table = soup.find('table', class_='class-J1Eb23b')

        # Initialize lists to store data
        ranks = []
        teams = []
        records = []
        points = []

        # Parse each row in the table
        rows = table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cols = row.find_all('td')

            # Extract data from columns
            ranks.append(cols[0].text.strip())
            team_name = cols[1].find('span', class_='class-QA1t2Tt').text.strip()
            teams.append(team_name)
            records.append(cols[2].text.strip())
            points.append(cols[3].text.strip())

        # Create DataFrame
        df = pd.DataFrame({
            'Rank': ranks,
            'Team': teams,
            'Record': records,
            'Points': points
        })

        # Convert rank to numeric
        df['Rank'] = pd.to_numeric(df['Rank'])

        # Convert points to numeric, removing any commas
        df['Points'] = pd.to_numeric(df['Points'].str.replace(',', ''))

        # Calculate points as percentage of maximum (1375)
        df['Points_Pct'] = (df['Points'] / PERFECT_SCORE)

        # Drop raw points column and rename percentage column
        df = df.drop('Points', axis=1)

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    usa_today_poll_df = fetch_and_parse()
    print(usa_today_poll_df)
