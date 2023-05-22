import requests
import data_extracting_funcs as dex
from bs4 import BeautifulSoup
import os.path


# make dictionary with regions and teams
list_file = "C:\\Users\\yaoki\Downloads\\4620 python\\s12_team _list.html"
g = open(list_file, "r", encoding = "latin-1")
gol_file = g.read()
soup = BeautifulSoup(gol_file, 'html.parser')
everything = soup.find_all('td')
team_dict = (dex.make_dict_of_teams(everything, 9)).copy()

# get headers for csv
h = open("C:\\Users\\yaoki\\Downloads\\4620 python\\gol.gg\\game\\stats\\44417\\page-fullstats\\index.html", "r", 
         encoding = "latin-1")
header_file = h.read()
soup = BeautifulSoup(header_file, 'html.parser')
everything = soup.find_all('td')
headers = dex.get_all_stats_headers(everything)
headers.insert(0, 'Team')
headers.insert(1, 'Game ID')
headers.insert(2, 'Win/Lose')

for i in range(44337, 44417, 1):
    path = "C:\\Users\\yaoki\\Downloads\\4620 python\\gol.gg\\game\\stats\\" + str(i) + "\\page-fullstats\\index.html"
    if os.path.exists(path):
        g = open("C:\\Users\\yaoki\\Downloads\\4620 python\\gol.gg\\game\\stats\\" + str(i) + "\\page-game\\index.html", "r", 
                 encoding = "latin-1")
        f = open("lol_champ.txt", "a")
        gol_file = g.read()

        # using page_summary
        soup = BeautifulSoup(gol_file, 'html.parser')

        # team, bans, picks
        team1_info = []
        team2_info = []
        # team1 name
        team1 = soup.find('div', class_ = 'blue-line-header')
        team11 = team1.find('a')
        team1_info.append(team11.text)
        # team2 name
        team2 = soup.find('div', class_ = 'red-line-header')
        team22 = team2.find('a')
        team2_info.append(team22.text)
        # game id
        team1_info.append(i)
        team2_info.append(i)
        # win/lose
        team1_info.append((team1.text.split())[-1])
        team2_info.append((team2.text.split())[-1])
        g.close()

        # using all stats
        g = open(path, "r", encoding = "latin-1")
        gol_file = g.read()
        soup = BeautifulSoup(gol_file, 'html.parser')
        everything = soup.find_all('td')

        for j in range(0, len(everything), 11):
            # get arrays into their own columns
            first, second = dex.get_row(j, everything)
            for k, m in zip(first, second):
                team1_info.append(k)
                team2_info.append(m)
        dex.put_in_csv(team_dict, team1_info, headers);
        dex.put_in_csv(team_dict, team2_info, headers);

        g.close()

        # k means clustering: https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1
        # all numerical, all data, apply ^
        # for each cluster, determine dist. of regions in each cluster
        # k = 4, data gets split into 4 parts by seeing how they are similar or different
        # then check what regions got clustered for each of the 4 groups (most are from which region)
        # if clusters are a mixed bag, there are no differences
