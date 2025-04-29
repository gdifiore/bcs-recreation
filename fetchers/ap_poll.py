import pandas as pd
import requests
from bs4 import BeautifulSoup

AP_URL = "https://apnews.com/hub/ap-top-25-college-football-poll"
PERFECT_SCORE = 1550

def fetch_ap_poll_rankings():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        response = requests.get(AP_URL, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        results_container = soup.find("div", class_="Results-container")
        if not results_container:
            print("Error: 'Results-container' div not found.")
            return pd.DataFrame()

        ranks = []
        teams = []
        scores = []

        poll_rows = results_container.find_all("dd", class_="PollModuleRow")

        for row in poll_rows:
            rank = row.find("div", class_="PollModuleRow-rank").get_text(strip=True)

            team = row.find("div", class_="PollModuleRow-team").a.get_text(strip=True)

            score_text = row.find("div", class_="PollModuleRow-points").get_text(strip=True)
            score = int(score_text.split()[0])

            ranks.append(int(rank))
            teams.append(team)
            scores.append(score)

        ap_df = pd.DataFrame({
            "Rank": ranks,
            "Team": teams,
            "Score": scores
        })

        ap_df["Normalized Score"] = ap_df["Score"] / PERFECT_SCORE

        ap_df = ap_df[["Rank", "Team", "Normalized Score"]]
        return ap_df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching AP Poll data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing the AP Poll table: {e}")
        return None
