MASSEY_URL = "https://masseyratings.com/cf/fbs/ratings"

def fetch_massey_ratings():
    import pandas as pd
    from bs4 import BeautifulSoup
    from requests_html import HTMLSession
    from io import StringIO

    session = HTMLSession()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = session.get(MASSEY_URL, headers=headers)

    response.html.render(timeout=50)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch the webpage. Status code: {response.status_code}")

    soup = BeautifulSoup(response.html.html, 'html.parser')

    table_div = soup.find('div', id='mytable0')
    if not table_div:
        raise Exception('No div with id "mytable0" found.')

    table = table_div.find('table')
    if not table:
        raise Exception('No table found inside the div with id "mytable0".')

    for td in table.find_all('td'):
        detail_div = td.find('div', class_='detail')
        if detail_div:
            detail_div.decompose()

    df = pd.read_html(StringIO(str(table)))[0]

    df = df.iloc[:-1]
    df = df.rename(columns={"Rat" : "Rank"})

    if "Rank" in df.columns:
        rank_column = df.pop("Rank")
        df.insert(0, "Rank", rank_column)
    else:
        raise Exception("'Rank' column not found in the combined DataFrame.")

    df = df[["Rank", "Team"]]

    df = df[df['Rank'] != 'Rat']
    df.reset_index(drop=True, inplace=True)
    df['Rank'] = range(1, len(df) + 1)

    return df
