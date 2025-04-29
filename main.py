from bcs_calculator import bcs_ranking_calculator
from utils import generate_table
import os

if __name__ == "__main__":
    try:
        # Create rankings directory if it doesn't exist
        os.makedirs("rankings", exist_ok=True)
        os.makedirs("docs", exist_ok=True)

        print("Running BCS Ranking Calculator...")
        rankings = bcs_ranking_calculator()

        print("\nTop 25 BCS Rankings:")
        print(rankings.head(25).to_string(index=False))

        # Save to CSV
        rankings.to_csv("rankings/bcs_rankings.csv", index=False)
        print("\nRankings saved to rankings/bcs_rankings.csv")

        # Generate HTML table from the rankings
        with open('rankings/bcs_rankings.csv', 'r') as f:
            csv_data = f.read()

        html_table = generate_table.bcs_rankings_to_html_table(csv_data)
        generate_table.save_html_to_file(html_table, "bcs_rankings.html")
        os.rename("bcs_rankings.html", "docs/index.html")
        print("\nCreated docs/index.html")

    except Exception as e:
        print(f"Error running BCS calculator: {str(e)}")
        exit(1)
