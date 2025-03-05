FEI_URL = "https://www.bcftoys.com/2024-fei"

def fetch_bcs_toys_fei_rankings():
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    try:
        response = requests.get(FEI_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')

        if not table:
            print("No table found on the page.")
            return None

        headers = [header.get_text(strip=True) for header in table.find_all('tr')[1].find_all('td')]
        rows = [
            [col.get_text(strip=True) for col in row.find_all('td')]
            for row in table.find_all('tr')[2:]
        ]

        df = pd.DataFrame(rows, columns=headers)

        header_row = list(df.columns)

        df = df[~df.apply(lambda row: list(row) == header_row, axis=1)]
        df = df.rename(columns={"Rk": "Rank"})
        df = df.dropna()
        df = df.reset_index(drop=True)
        df = df.iloc[:, :2] # multiple cols called Rank, so keep by position not name


        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None
