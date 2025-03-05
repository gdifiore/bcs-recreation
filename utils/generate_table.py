def bcs_rankings_to_html_table(csv_data):
    """
    Converts CSV-formatted BCS ranking data into an HTML table

    Args:
        csv_data (str): CSV data as a string

    Returns:
        str: HTML table representation of the data
    """
    rows = csv_data.strip().split('\n')

    headers = rows[0].split(',')

    rank_index = headers.index('bcs_rank')
    team_index = headers.index('team')
    bcs_score_index = headers.index('bcs_score')

    data_rows = []
    for row in rows[1:]:
        data_rows.append(row.split(','))

    top_25 = [row for row in data_rows if int(float(row[rank_index])) <= 25]

    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>(Recreated) BCS Top 25 Rankings</title>
    <style>
        body {
            font-family: monospace;
            line-height: 1.5;
            margin: 0 auto;
            max-width: 800px;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 20px;
        }

        h1, h2, h3 {
            margin: 0.5em 0;
        }

        section {
            margin-bottom: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        th, td {
            border: 1px solid #333;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f4f4f4;
            font-weight: bold;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        ul {
            padding-left: 1em;
        }

        footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
        }

        a {
            color: #333;
        }

        a:visited {
            color: #333;
        }

        /* Responsive Design for smaller screens */
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }

            header, footer {
                text-align: center;
            }

            h1 {
                font-size: 1.8em;
            }

            h2 {
                font-size: 1.4em;
            }

            h3 {
                font-size: 1.2em;
            }

            ul {
                padding-left: 1em;
            }
        }

        /* Extra small devices */
        @media (max-width: 480px) {
            body {
                font-size: 0.9em;
                line-height: 1.4;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>(Recreated) BCS Top 25 Rankings</h1>
    </header>
    <section>
        <table>
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Team</th>
                    <th>BCS Score</th>
                </tr>
            </thead>
            <tbody>
    """

    for row in top_25:
        rank = int(float(row[rank_index]))
        team = row[team_index]
        bcs_score = float(row[bcs_score_index])

        html += f"""                <tr>
                    <td>{rank}</td>
                    <td>{team}</td>
                    <td>{bcs_score:.3f}</td>
                </tr>
"""

    html += """
            </tbody>
        </table>
    </section>
</body>
</html>
    """

    return html

def save_html_to_file(html_content, filename="bcs_rankings.html"):
    """
    Saves the HTML content to a file

    Args:
        html_content (str): HTML content to save
        filename (str): Name of the file to save to
    """
    with open(filename, 'w') as f:
        f.write(html_content)
    print(f"HTML table saved to {filename}")
