import requests
import data_extracting_funcs as dex
from bs4 import BeautifulSoup

g = open("C:\\Users\\yaoki\\Downloads\\4620 python\\gol.gg\\game\\stats\\44337\\page-game\\index.html", "r", encoding = "latin-1")
f = open("lol_champ.txt", "a")
gol_file = g.read()

# World Champioinships 2022 T1 vs DRX Game
soup = BeautifulSoup(gol_file, 'html.parser')

# team, bans, picks
win_info = []
lost_info = []

# get losing team name
lost = soup.find('div', class_ = 'red-line-header')
#lost2 = lost.find('a')
#print(lost2.text)
print(lost.text.split())
#print(lost[0].text.split())
#lost_info.append((lost[0].text.split())[0])
exit()
both = list(soup.find_all('div', class_ = 'col-10'))
gold = soup.find_all('table', class_ = 'small_table')
#print(gold[0].text.split())
dmg = gold[1].text.split()
#print(dmg)
kda_cs = soup.find_all('tr')
#print(kda_cs[32].text.split())
# runes: kda_cs = soup.find_all('tr'); print(kda_cs[1].text.split())
#breakpoint()
# get losing team bans and picks
l_bans = dex.get_bans_picks(str(both[0]))
l_picks = dex.get_bans_picks(str(both[1]))
lost_info.append(l_bans)
lost_info.append(l_picks)

# get losing team gold distribution
lost_info.append(dex.get_lose_gold(gold[0].text.split()))

# get losing team dmg distribution
lost_info.append(dex.get_lose_dmg(dmg))

# get losing team kda and cs
kda, cs = dex.get_kda_cs(kda_cs, 32)
lost_info.append(kda)
lost_info.append(cs)

# get winning team name
win = soup.find_all('div', class_ = 'blue-line-header')
win_info.append((win[0].text.split())[0])

# get winning team bans and picks
w_bans = dex.get_bans_picks(str(both[2]))
w_picks = dex.get_bans_picks(str(both[3]))
win_info.append(w_bans)
win_info.append(w_picks)

# get winning team gold distribution
win_info.append(dex.get_win_gold(gold[0].text.split()))

# get winning team dmg distribution
win_info.append(dex.get_win_dmg(dmg))

# get winning team kda and cs
kda, cs = dex.get_kda_cs(kda_cs, 1)
win_info.append(kda)
win_info.append(cs)

print(lost_info)
print(win_info)
#breakpoint()


f.close()
g.close()
