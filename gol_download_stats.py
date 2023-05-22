import requests
import os
import os.path

for file in os.listdir("."):
    if not os.path.exists(file + "/page-fullstats/index.html"):
        temp = requests.get("https://gol.gg/game/stats/%s/page-fullstats/"%file, 
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)'}
    )
        os.makedirs(file + "/page-fullstats")
        f = open(file + "/page-fullstats/index.html", "w")
        f.write(temp.text)
        f.close()

    if not os.path.exists(file + "/page-game/index.html"):
        temp = requests.get("https://gol.gg/game/stats/%s/page-game/"%file, 
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)'}
    )
        os.makedirs(file + "/page-game")
        f = open(file + "/page-game/index.html", "w")
        f.write(temp.text)
        f.close()

# goes and downloads each stats page for the
# games i have already downloaded based off game id
# to add new games, make directory for it then run this script

