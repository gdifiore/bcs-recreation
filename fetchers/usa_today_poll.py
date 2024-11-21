import pandas as pd
import requests
from bs4 import BeautifulSoup

USA_TODAY_URL = "https://sportsdata.usatoday.com/football/ncaaf/coaches-poll"
PERFECT_SCORE = 1375

def fetch_usa_today_rankings():
    try:
        response = requests.get(USA_TODAY_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', class_='class-J1Eb23b')

        ranks = []
        teams = []
        records = []
        points = []

        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')

            ranks.append(cols[0].text.strip())
            team_name = cols[1].find('span', class_='class-QA1t2Tt').text.strip()
            teams.append(team_name)
            records.append(cols[2].text.strip())
            points.append(cols[3].text.strip())

        df = pd.DataFrame({
            'Rank': ranks,
            'Team': teams,
            'Record': records,
            'Points': points
        })

        df['Rank'] = pd.to_numeric(df['Rank'])

        df['Points'] = pd.to_numeric(df['Points'].str.replace(',', ''))

        df['Points_Pct'] = (df['Points'] / PERFECT_SCORE)

        df = df.drop('Points', axis=1)
        df = df[["Rank", "Team", "Points_Pct"]]

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

# Test the function
if __name__ == "__main__":
    df = fetch_usa_today_rankings()
    if df is not None:
        print(df.to_string())