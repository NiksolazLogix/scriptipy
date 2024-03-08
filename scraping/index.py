import requests
from bs4 import BeautifulSoup

"""
# SET URL
url = "https://www.w3schools.com/html/html5_serversentevents.asp"

# GET HTML
res = requests.get(url)

# PARSE HTML
soup = BeautifulSoup(res.text, "html.parser") 

# GET TAG
spots = soup.find_all("a", attrs={"target": "_top"})

# GET TEXT
spot_lists = []
for spot in spots:
    spot_list = []
    spot_list.append(spot.text)
    spot_lists.append(spot_list)

# CREATE DATAFRAME
import pandas as pd
df = pd.DataFrame()
df["SPOT"] = spot_lists
df.head()

# SAVE CSV
df.to_csv("W3Schools.csv", index=False)
"""
def get_scraping(url, options):
    # GET HTML
    res = requests.get(url)

    # PARSE HTML
    soup = BeautifulSoup(res.text, options["method"]) 

    # GET TAG
    lists = soup.find_all(options["tag"], attrs=options["attr"])

    # GET TEXT
    res_lists = []
    for lista in lists:
        res_lista = []
        res_lista.append(lista.text)
        for dat in options["append_data_list"]:
            res_lista.append(lista.get(dat))
        res_lists.append(res_lista)


    # CREATE DATAFRAME
    import pandas as pd
    df = pd.DataFrame()
    df[options["name_column"]] = res_lists

    # SAVE CSV
    df.to_csv(options["name_csv"], index=options["index_csv"])

# SET URL
url = "https://www.w3schools.com/html/html5_serversentevents.asp"
options = {
    "method": "html.parser",
    "tag": "a",
    "attr": {
        "target": "_top",
        "href": True,
    },
    "append_data_list": ["href"],
    "name_csv": "W3Schools.csv",
    "name_column": "Elenco Menu",
    "index_csv": True
}
get_scraping(url, options)


