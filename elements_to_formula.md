## human
- [x] ~~Harris Interactive College Football Poll~~ -> AP Poll
    Perfect Score is 1550pts, so divide score by that (62 votes)
- [x] USA Today Coaches Poll
    Perfect Score is 1375pts, so divide by that (55 votes)

## computer
- [x] FPI (espn)
- [x] Sagarin (http://sagarin.com/sports/cfsend.htm) hell to parse LMAO
- [x] FEI Ratings (https://www.bcftoys.com/2024-fei)
- [x] The Power Rank (https://thepowerrank.com/college-football/bowl-subdivision-rankings/)
- [x] Massey Ratings (https://masseyratings.com/cf/fbs/ratings)
- [x] Colley Matrix (https://www.colleyrankings.com/currank.html)

Drop the highest and lowest ratings for each team, then for each ranking (1=25, 2=24, ...) sum the remaining 4 and divide by 100 (all 1st place)

## Formula

AP% + USA% + computer% = BCS rating scaled [0, 1] sort by that

## What if team is ranked in one poll but not another?

The BCS (Bowl Championship Series) calculator had a specific method for handling situations where a team was ranked in one poll but not another. Here's how it typically worked:
Handling Discrepancies in Rankings
When a team was ranked in one poll but unranked in another, the BCS calculator would use a standardized approach to ensure fair representation:

    Assigned Value: For the poll where the team was unranked, the BCS would assign that team a ranking value just below the last ranked team in that poll.
    Averaging: The BCS would then average the team's ranking from the poll where it was ranked with the assigned value from the poll where it was unranked.
    Computer Rankings: In addition to the human polls, the BCS also incorporated computer rankings, which helped to balance out discrepancies between different polls.

Example Application
Using the example you provided:

    Tulane: Ranked 25th in AP, unranked in USA Today
    Iowa State: Unranked in AP, ranked 25th in USA Today

The BCS would likely handle this situation as follows:

    For Tulane, it would use the 25th ranking from AP and assign a value just below the last ranked team in USA Today (e.g., 26th or 27th).
    For Iowa State, it would use the 25th ranking from USA Today and assign a value just below the last ranked team in AP (e.g., 26th or 27th).
    These values would then be averaged with the other components of the BCS formula, including the computer rankings, to determine the team's overall BCS ranking.