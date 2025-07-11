POWER_RANKING_URL = (
    "https://thepowerrank.com/college-football/bowl-subdivision-rankings/"
)


def fetch_power_ranking_rankings():
    import re
    import pandas as pd
    from requests_html import HTMLSession
    from bs4 import BeautifulSoup

    session = HTMLSession()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = session.get(POWER_RANKING_URL, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch the top-level webpage. Status code: {response.status_code}"
        )

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if not table:
        print("No table found on the page.")
        return None

    headers = [th.text.strip() for th in table.find("thead").find_all("th")]

    rows = []
    for tr in table.find("tbody").find_all("tr"):
        row = [td.text.strip() for td in tr.find_all("td")]
        rows.append(row)

    df = pd.DataFrame(rows, columns=headers)
    df = df[["Rank", "Team"]]
    df["Team"] = df["Team"].apply(lambda x: re.sub(r"\s\(\d+-\d+\)", "", x))
    df.reset_index(drop=True, inplace=True)

    return df
