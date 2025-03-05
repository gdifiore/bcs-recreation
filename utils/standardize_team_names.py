def standardize_team_names(team_name):
    """
    Standardizes college football team names to a consistent format.

    Args:
        team_name (str): The team name to standardize

    Returns:
        str: The standardized team name
    """
    if team_name is None:
        return None

    team_name = team_name.strip().lower()

    # Comprehensive mapping dictionary
    name_mapping = {
        # A
        "akron": "Akron",
        "akron zips": "Akron",

        "alabama": "Alabama",
        "alabama crimson tide": "Alabama",

        "air force": "Air Force",
        "air force falcons": "Air Force",

        "appalachian state": "Appalachian State",
        "app state": "Appalachian State",
        "app state mountaineers": "Appalachian State",

        "arizona": "Arizona",
        "arizona wildcats": "Arizona",

        "arizona state": "Arizona State",
        "arizona st": "Arizona State",
        "arizona st.": "Arizona State",
        "arizona state sun devils": "Arizona State",

        "arkansas": "Arkansas",
        "arkansas razorbacks": "Arkansas",

        "arkansas state": "Arkansas State",
        "arkansas st": "Arkansas State",
        "arkansas st.": "Arkansas State",
        "arkansas state red wolves": "Arkansas State",

        "army": "Army",
        "army west point": "Army",
        "army black knights": "Army",

        "auburn": "Auburn",
        "auburn tigers": "Auburn",

        # B
        "ball state": "Ball State",
        "ball st": "Ball State",
        "ball st.": "Ball State",
        "ball state cardinals": "Ball State",

        "baylor": "Baylor",
        "baylor bears": "Baylor",

        "boise state": "Boise State",
        "boise st": "Boise State",
        "boise st.": "Boise State",
        "boise state broncos": "Boise State",

        "boston college": "Boston College",
        "boston coll": "Boston College",
        "boston coll.": "Boston College",
        "boston college eagles": "Boston College",

        "bowling green": "Bowling Green",
        "bowling green falcons": "Bowling Green",

        "brigham young": "BYU",
        "byu": "BYU",
        "byu cougars": "BYU",

        "buffalo": "Buffalo",
        "buffalo bulls": "Buffalo",

        # C
        "california": "California",
        "cal": "California",
        "california golden bears": "California",

        "central florida": "UCF",
        "ucf": "UCF",
        "central florida(ucf)": "UCF",
        "ucf knights": "UCF",

        "central michigan": "Central Michigan",
        "cent michigan": "Central Michigan",
        "central michigan chippewas": "Central Michigan",

        "charlotte": "Charlotte",
        "charlotte 49ers": "Charlotte",

        "cincinnati": "Cincinnati",
        "cincinnati bearcats": "Cincinnati",

        "clemson": "Clemson",
        "clemson tigers": "Clemson",

        "coastal carolina": "Coastal Carolina",
        "coastal carolina chanticleers": "Coastal Carolina",

        "colorado": "Colorado",
        "colorado buffaloes": "Colorado",

        "colorado state": "Colorado State",
        "colorado st": "Colorado State",
        "colorado st.": "Colorado State",
        "colorado state rams": "Colorado State",

        "connecticut": "Connecticut",
        "uconn": "Connecticut",
        "uconn huskies": "Connecticut",
        "connecticut huskies": "Connecticut",

        # D
        "duke": "Duke",
        "duke blue devils": "Duke",

        # E
        "east carolina": "East Carolina",
        "east carolina pirates": "East Carolina",

        "eastern michigan": "Eastern Michigan",
        "east michigan": "Eastern Michigan",
        "eastern michigan eagles": "Eastern Michigan",

        # F
        "florida": "Florida",
        "florida gators": "Florida",

        "florida atlantic": "Florida Atlantic",
        "fla. atlantic": "Florida Atlantic",
        "florida atlantic owls": "Florida Atlantic",

        "florida international": "Florida International",
        "fla. international": "Florida International",
        "florida intl": "Florida International",
        "florida international panthers": "Florida International",

        "florida state": "Florida State",
        "florida st": "Florida State",
        "florida st.": "Florida State",
        "florida state seminoles": "Florida State",

        "fresno state": "Fresno State",
        "fresno st": "Fresno State",
        "fresno st.": "Fresno State",
        "fresno state bulldogs": "Fresno State",

        # G
        "georgia": "Georgia",
        "georgia bulldogs": "Georgia",

        "georgia southern": "Georgia Southern",
        "georgia southern eagles": "Georgia Southern",

        "georgia state": "Georgia State",
        "georgia state panthers": "Georgia State",

        "georgia tech": "Georgia Tech",
        "georgia tech yellow jackets": "Georgia Tech",

        # H
        "hawaii": "Hawaii",
        "hawai'i": "Hawaii",
        "hawaii rainbow warriors": "Hawaii",
        "hawai'i rainbow warriors": "Hawaii",

        "houston": "Houston",
        "houston cougars": "Houston",

        # I
        "illinois": "Illinois",
        "illinois fighting illini": "Illinois",

        "indiana": "Indiana",
        "indiana hoosiers": "Indiana",

        "iowa": "Iowa",
        "iowa hawkeyes": "Iowa",

        "iowa state": "Iowa State",
        "iowa st": "Iowa State",
        "iowa st.": "Iowa State",
        "iowa state cyclones": "Iowa State",

        # J
        "jacksonville state": "Jacksonville State",
        "jacksonville st": "Jacksonville State",
        "jacksonville st.": "Jacksonville State",
        "jacksonville state gamecocks": "Jacksonville State",

        "james madison": "James Madison",
        "james madison dukes": "James Madison",

        # K
        "kansas": "Kansas",
        "kansas jayhawks": "Kansas",

        "kansas state": "Kansas State",
        "kansas st": "Kansas State",
        "kansas st.": "Kansas State",
        "kansas state wildcats": "Kansas State",

        "kent state": "Kent State",
        "kent st": "Kent State",
        "kent st.": "Kent State",
        "kent state golden flashes": "Kent State",

        "kentucky": "Kentucky",
        "kentucky wildcats": "Kentucky",

        "kennesaw state": "Kennesaw State",
        "kennesaw st": "Kennesaw State",
        "kennesaw st.": "Kennesaw State",
        "kennesaw state owls": "Kennesaw State",

        # L
        "liberty": "Liberty",
        "liberty flames": "Liberty",

        "louisiana": "Louisiana",
        "louisiana-lafayette": "Louisiana",
        "la lafayette": "Louisiana",
        "louisiana ragin' cajuns": "Louisiana",
        "louisiana lafayette": "Louisiana",
        "ul lafayette": "Louisiana",
        "louisiana ragin cajuns": "Louisiana",

        "louisiana monroe": "Louisiana Monroe",
        "ul monroe": "Louisiana Monroe",
        "louisiana-monroe": "Louisiana Monroe",
        "louisiana monroe(ulm)": "Louisiana Monroe",
        "ul monroe warhawks": "Louisiana Monroe",
        "louisiana monroe warhawks": "Louisiana Monroe",
        "la monroe": "Louisiana Monroe",
        "ulm": "Louisiana Monroe",

        "louisiana tech": "Louisiana Tech",
        "louisiana tech bulldogs": "Louisiana Tech",
        "la tech": "Louisiana Tech",

        "louisville": "Louisville",
        "louisville cardinals": "Louisville",

        "lsu": "LSU",
        "lsu tigers": "LSU",

        # M
        "marshall": "Marshall",
        "marshall thundering herd": "Marshall",

        "maryland": "Maryland",
        "maryland terrapins": "Maryland",

        "massachusetts": "Massachusetts",
        "umass": "Massachusetts",
        "massachusetts minutemen": "Massachusetts",

        "memphis": "Memphis",
        "memphis tigers": "Memphis",

        "miami (fl)": "Miami (FL)",
        "miami-florida": "Miami (FL)",
        "miami": "Miami (FL)",
        "miami hurricanes": "Miami (FL)",

        "miami (oh)": "Miami (OH)",
        "miami-ohio": "Miami (OH)",
        "miami (ohio)": "Miami (OH)",
        "miami oh": "Miami (OH)",
        "miami (oh) redhawks": "Miami (OH)",
        "miami oh redhawks": "Miami (OH)",

        "michigan": "Michigan",
        "michigan wolverines": "Michigan",

        "michigan state": "Michigan State",
        "michigan st": "Michigan State",
        "michigan st.": "Michigan State",
        "michigan state spartans": "Michigan State",

        "middle tennessee": "Middle Tennessee",
        "middle tenn st": "Middle Tennessee",
        "middle tennessee state": "Middle Tennessee",
        "middle tennessee blue raiders": "Middle Tennessee",

        "minnesota": "Minnesota",
        "minnesota golden gophers": "Minnesota",

        "mississippi": "Ole Miss",
        "ole miss": "Ole Miss",
        "ole miss rebels": "Ole Miss",

        "mississippi state": "Mississippi State",
        "miss state": "Mississippi State",
        "miss st": "Mississippi State",
        "mississippi st": "Mississippi State",
        "mississippi state bulldogs": "Mississippi State",

        "missouri": "Missouri",
        "missouri tigers": "Missouri",

        # N
        "navy": "Navy",
        "navy midshipmen": "Navy",

        "nc state": "NC State",
        "north carolina state": "NC State",
        "n.c. state": "NC State",
        "north carolina st": "NC State",
        "nc state wolfpack": "NC State",

        "nebraska": "Nebraska",
        "nebraska cornhuskers": "Nebraska",

        "nevada": "Nevada",
        "nevada wolf pack": "Nevada",

        "new mexico": "New Mexico",
        "new mexico lobos": "New Mexico",

        "new mexico state": "New Mexico State",
        "new mexico st": "New Mexico State",
        "new mexico st.": "New Mexico State",
        "new mexico state aggies": "New Mexico State",

        "north carolina": "North Carolina",
        "north carolina tar heels": "North Carolina",

        "north texas": "North Texas",
        "north texas mean green": "North Texas",

        "northern illinois": "Northern Illinois",
        "northern ill": "Northern Illinois",
        "northern illinois huskies": "Northern Illinois",

        "northwestern": "Northwestern",
        "northwestern wildcats": "Northwestern",

        "notre dame": "Notre Dame",
        "notre dame fighting irish": "Notre Dame",

        # O
        "ohio": "Ohio",
        "ohio bobcats": "Ohio",

        "ohio state": "Ohio State",
        "ohio st": "Ohio State",
        "ohio st.": "Ohio State",
        "ohio state buckeyes": "Ohio State",

        "oklahoma": "Oklahoma",
        "oklahoma sooners": "Oklahoma",

        "oklahoma state": "Oklahoma State",
        "oklahoma st": "Oklahoma State",
        "oklahoma st.": "Oklahoma State",
        "oklahoma state cowboys": "Oklahoma State",

        "old dominion": "Old Dominion",
        "old dominion monarchs": "Old Dominion",

        "oregon": "Oregon",
        "oregon ducks": "Oregon",

        "oregon state": "Oregon State",
        "oregon st": "Oregon State",
        "oregon st.": "Oregon State",
        "oregon state beavers": "Oregon State",

        # P
        "penn state": "Penn State",
        "penn st": "Penn State",
        "penn st.": "Penn State",
        "penn state nittany lions": "Penn State",

        "pittsburgh": "Pittsburgh",
        "pitt": "Pittsburgh",
        "pittsburgh panthers": "Pittsburgh",

        "purdue": "Purdue",
        "purdue boilermakers": "Purdue",

        # R
        "rice": "Rice",
        "rice owls": "Rice",

        "rutgers": "Rutgers",
        "rutgers scarlet knights": "Rutgers",

        # S
        "sam houston": "Sam Houston",
        "sam houston state": "Sam Houston",
        "sam houston st": "Sam Houston",
        "sam houston bearkats": "Sam Houston",
        "sam houston st.": "Sam Houston",

        "san diego state": "San Diego State",
        "san diego st": "San Diego State",
        "san diego st.": "San Diego State",
        "san diego state aztecs": "San Diego State",

        "san jose state": "San Jose State",
        "san jose st": "San Jose State",
        "san josé state": "San Jose State",
        "san jose st.": "San Jose State",
        "san jose state spartans": "San Jose State",
        "san josé state spartans": "San Jose State",

        "smu": "SMU",
        "southern methodist": "SMU",
        "smu mustangs": "SMU",

        "south alabama": "South Alabama",
        "south alabama jaguars": "South Alabama",

        "south carolina": "South Carolina",
        "south carolina gamecocks": "South Carolina",

        "south florida": "South Florida",
        "usf": "South Florida",
        "south florida bulls": "South Florida",

        "southern california": "USC",
        "usc": "USC",
        "southern cal": "USC",
        "usc trojans": "USC",

        "southern miss": "Southern Miss",
        "southern mississippi": "Southern Miss",
        "southern miss golden eagles": "Southern Miss",

        "stanford": "Stanford",
        "stanford cardinal": "Stanford",

        "syracuse": "Syracuse",
        "syracuse orange": "Syracuse",

        # T
        "tcu": "TCU",
        "texas christian": "TCU",
        "tcu horned frogs": "TCU",

        "temple": "Temple",
        "temple owls": "Temple",

        "tennessee": "Tennessee",
        "tennessee volunteers": "Tennessee",

        "texas": "Texas",
        "texas longhorns": "Texas",

        "texas a&m": "Texas A&M",
        "texas a&amp;m": "Texas A&M",
        "texas am": "Texas A&M",
        "texas aggies": "Texas A&M",
        "texas a&m aggies": "Texas A&M",

        "texas state": "Texas State",
        "texas st": "Texas State",
        "texas st.": "Texas State",
        "texas state bobcats": "Texas State",

        "texas tech": "Texas Tech",
        "texas tech red raiders": "Texas Tech",

        "toledo": "Toledo",
        "toledo rockets": "Toledo",

        "troy": "Troy",
        "troy trojans": "Troy",

        "tulane": "Tulane",
        "tulane green wave": "Tulane",

        "tulsa": "Tulsa",
        "tulsa golden hurricane": "Tulsa",

        # U
        "uab": "UAB",
        "alabama-birmingham": "UAB",
        "alabama birmingham": "UAB",
        "uab blazers": "UAB",

        "ucla": "UCLA",
        "ucla bruins": "UCLA",

        "unlv": "UNLV",
        "nevada-las vegas": "UNLV",
        "nevada las vegas": "UNLV",
        "unlv rebels": "UNLV",

        "utah": "Utah",
        "utah utes": "Utah",

        "utah state": "Utah State",
        "utah st": "Utah State",
        "utah st.": "Utah State",
        "utah state aggies": "Utah State",

        "utep": "UTEP",
        "texas-el paso": "UTEP",
        "texas el paso": "UTEP",
        "utep miners": "UTEP",

        "utsa": "UTSA",
        "texas-san antonio": "UTSA",
        "texas san antonio": "UTSA",
        "utsa roadrunners": "UTSA",

        # V
        "vanderbilt": "Vanderbilt",
        "vandy": "Vanderbilt",
        "vanderbilt commodores": "Vanderbilt",

        "virginia": "Virginia",
        "virginia cavaliers": "Virginia",
        "uva": "Virginia",

        "virginia tech": "Virginia Tech",
        "virginia tech hokies": "Virginia Tech",
        "va tech": "Virginia Tech",
        "vt": "Virginia Tech",

        # W
        "wake forest": "Wake Forest",
        "wake forest demon deacons": "Wake Forest",

        "washington": "Washington",
        "washington huskies": "Washington",

        "washington state": "Washington State",
        "washington st": "Washington State",
        "washington st.": "Washington State",
        "wazzu": "Washington State",
        "wash state": "Washington State",
        "washington state cougars": "Washington State",

        "west virginia": "West Virginia",
        "west virginia mountaineers": "West Virginia",
        "wvu": "West Virginia",

        "western kentucky": "Western Kentucky",
        "w kentucky": "Western Kentucky",
        "west kentucky": "Western Kentucky",
        "western kentucky hilltoppers": "Western Kentucky",

        "western michigan": "Western Michigan",
        "w michigan": "Western Michigan",
        "western michigan broncos": "Western Michigan",

        "wisconsin": "Wisconsin",
        "wisconsin badgers": "Wisconsin",

        "wyoming": "Wyoming",
        "wyoming cowboys": "Wyoming",
    }

    # Return the standardized name if found, otherwise return the original
    for pattern, standard_name in name_mapping.items():
        if team_name == pattern:
            return standard_name

    # If not found in mapping, return the original with first letters capitalized
    return team_name.title()