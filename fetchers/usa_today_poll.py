USA_TODAY_URL = "https://sportsdata.usatoday.com/football/ncaaf/coaches-poll"
PERFECT_SCORE = 1375

def fetch_usa_today_rankings():
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        response = requests.get(USA_TODAY_URL, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', class_='J1Eb23__J1Eb23')

        ranks = []
        teams = []
        records = []
        points = []

        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')

            ranks.append(cols[0].text.strip())
            team_name = cols[1].find('span', class_='QA1t2T__QA1t2T').text.strip()
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

        df['Normalized Score'] = (df['Points'] / PERFECT_SCORE)

        df = df.drop('Points', axis=1)
        df = df[["Rank", "Team", "Normalized Score"]]

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None
