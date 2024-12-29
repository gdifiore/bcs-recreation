ESPN_FPI_URL = "https://www.espn.com/college-football/fpi"

def fetch_espn_fpi_rankings():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from io import StringIO

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

    response = requests.get(ESPN_FPI_URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the webpage. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    responsive_table_div = soup.find('div', class_='ResponsiveTable')
    if not responsive_table_div:
        raise Exception("No div with class 'ResponsiveTable' found.")

    table1 = responsive_table_div.find('table')
    if not table1:
        raise Exception("No table found inside the 'ResponsiveTable' div.")

    df1 = pd.read_html(StringIO(str(table1)))[0]

    all_tbody_tags = soup.find_all('tbody')
    if len(all_tbody_tags) < 2:
        raise Exception("Less than two <tbody> tags found in the HTML.")

    table2_html = f"<table>{str(all_tbody_tags[1])}</table>"
    df2 = pd.read_html(StringIO(table2_html))[0]

    new_column_names = [
        "W-L", "FPI", "Rank", "TREND", "PROJ W-L", "WIN OUT%",
        "6WINS%", "WIN DIV%", "WIN CONF%", "PLAYOFF%",
        "MAKE NC%", "WIN NC%"
    ]
    if len(df2.columns) != len(new_column_names):
        raise Exception("Column count mismatch between DataFrame and new column names.")

    df2.columns = new_column_names

    combined_df = pd.concat([df1, df2], axis=1)

    if "Rank" in combined_df.columns:
        rank_column = combined_df.pop("Rank")
        combined_df.insert(0, "Rank", rank_column)
    else:
        raise Exception("'Rank' column not found in the combined DataFrame.")

    combined_df = combined_df[["Rank", "Team"]]

    return combined_df

if __name__ == "__main__":
    df = fetch_espn_fpi_rankings()
    if df is not None:
        print(df.to_string())