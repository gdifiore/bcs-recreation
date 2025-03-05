COLLEY_URL = "https://www.colleyrankings.com/currank.html"

def fetch_colley_matrix_table():
    import pandas as pd
    from bs4 import BeautifulSoup
    from requests_html import HTMLSession

    session = HTMLSession()

    response = session.get(COLLEY_URL)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch the top-level webpage. Status code: {response.status_code}"
        )

    soup = BeautifulSoup(response.text, "html.parser")
    frame = soup.find("frame", {"name": "mainframe"})
    if not frame:
        raise Exception("No mainframe found on the webpage.")

    frame_url = response.url.rsplit("/", 1)[0] + "/" + frame["src"]

    frame_response = session.get(frame_url)
    if frame_response.status_code != 200:
        raise Exception(
            f"Failed to fetch the mainframe content. Status code: {frame_response.status_code}"
        )

    soup = BeautifulSoup(frame_response.text, "html.parser")

    table = soup.find("table")
    if not table:
        raise Exception("No table found in the mainframe content.")

    rows = table.find_all("tr")
    data = []
    EXPECTED_COLUMNS = 8

    for row in rows:
        cells = row.find_all(["td", "th"])

        if len(cells) != EXPECTED_COLUMNS or cells[0].get_text(strip=True) == "":
            continue

        row_data = [cell.get_text(strip=True) for cell in cells]

        rank_cell = row_data[0]
        if rank_cell.endswith("."):
            rank = rank_cell.replace(".", "").strip()
            row_data[0] = rank

        data.append(row_data)

    df = pd.DataFrame(data)

    df.columns = [
        "Rank",
        "Team",
        "Rating",
        "Record",
        "SOS: rank",
        "Top 25 Wins",
        "Top 50 Wins",
        "Best Game",
    ]

    df = df.dropna(how="all")
    df = df[["Rank", "Team"]]
    df = df[~df['Team'].str.contains(r'FCS GROUP \d', regex=True)]
    df.reset_index(drop=True, inplace=True)
    df['Rank'] = range(1, len(df) + 1)

    return df
