from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

def parse_college_football_rankings():
    html = requests.get("http://sagarin.com/sports/cfsend.htm").text
    soup = bs(html, "html.parser")

    table = str(soup.find_all("pre")[2])

    lines = table.split("\n")

    rank_team_data = []

    for line in lines[3:]:
        if line.strip():
            strip = line.split()
            if strip[0].isdigit():
                rank = strip[0]
                for x in range(1, len(strip)):
                    if strip[x] == "A":  # A means D1
                        team = " ".join(strip[1:x])  # combine team name
                        rank_team_data.append((rank, team))

    df = pd.DataFrame(rank_team_data, columns=["Rank", "Team"])
    df['Rank'] = range(1, len(df) + 1)
    df.reset_index(drop=True, inplace=True)

    return df


if __name__ == "__main__":
    df = parse_college_football_rankings()
    if df is not None:
        print(df.to_string())
