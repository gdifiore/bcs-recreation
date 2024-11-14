import pandas as pd
import requests
from bs4 import BeautifulSoup

# Constants for AP Poll
AP_URL = "https://apnews.com/hub/ap-top-25-college-football-poll"  # Replace this with the actual URL of the AP Poll
PERFECT_SCORE = 1550  # Perfect score for AP Poll

def fetch_and_parse():
    """
    Fetches the AP Poll data from the given URL, parses it, and returns a DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame with team names and normalized AP poll scores.
    """
    try:
        # Fetch the page content
        response = requests.get(AP_URL)
        response.raise_for_status()  # Raise an error if the request fails

        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the 'Results-container' div
        results_container = soup.find("div", class_="Results-container")
        if not results_container:
            print("Error: 'Results-container' div not found.")
            return pd.DataFrame()

        # Initialize lists to collect poll data
        ranks = []
        teams = []
        scores = []

        # Find all poll rows within the Results-container
        poll_rows = results_container.find_all("dd", class_="PollModuleRow")

        for row in poll_rows:
            # Extract rank
            rank = row.find("div", class_="PollModuleRow-rank").get_text(strip=True)

            # Extract team name
            team = row.find("div", class_="PollModuleRow-team").a.get_text(strip=True)

            # Extract score
            score_text = row.find("div", class_="PollModuleRow-points").get_text(strip=True)
            score = int(score_text.split()[0])  # Extract just the score as an integer

            # Append data to lists
            ranks.append(int(rank))
            teams.append(team)
            scores.append(score)

        # Create DataFrame from the extracted data
        ap_df = pd.DataFrame({
            "Rank": ranks,
            "Team": teams,
            "Score": scores
        })

        # Normalize the score
        ap_df["Normalized Score"] = ap_df["Score"] / PERFECT_SCORE

        # Keep only relevant columns
        ap_df = ap_df[["Rank", "Team", "Normalized Score"]]

        return ap_df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching AP Poll data: {e}")
    except ValueError as e:
        print(f"Error parsing the AP Poll table: {e}")

    return pd.DataFrame()  # Return empty DataFrame on failure

# Example usage
if __name__ == "__main__":
    ap_poll_df = fetch_and_parse()
    print(ap_poll_df)