import csv
import re
import os.path

# functions for individual games
def get_bans_picks(temp):
    bp = []
    for s in temp.split():
        if s.startswith('title'):
            temp1 = s.split()
            bp.append((temp1[0])[7:])
    return bp

def rmv_words(temp):
    for i in range(len(temp)):
        if not temp[i].isalpha():
            return temp[i:]
        
def get_win_gold(temp):
    gold = []
    for i in range(1, 10, 2):
        gold.append(rmv_words(temp[i]))
    return gold

def get_lose_gold(temp):
    gold = []
    for i in range(2, 10, 2):
        gold.append(temp[i])
    return gold

def get_win_dmg(temp):
    dmg = []
    for i in range(2, len(temp), 3):
        dmg.append(rmv_words(temp[i]))
    return dmg

def get_lose_dmg(temp):
    dmg = []
    for i in range(3, len(temp), 3):
        dmg.append(temp[i])
    return dmg

def get_kda_cs(temp, start):
    kda = []
    cs = []
    j = start
    for i in range(0,5):
        length = len(temp[j].text.split())
        kda.append((temp[j].text.split())[length - 2])
        cs.append((temp[j].text.split())[length - 1])
        j += 6

    return kda, cs
        

# functions for all stats
def get_row(index, l):
    first = []
    second = []
    for i in range(index + 1, index + 6, 1):
        first.append(l[i].text)

    for i in range(index + 6, index + 11, 1):
        second.append(l[i].text)

    return first, second

def get_all_stats_headers(l):
    labels = []
    for i in range(0, len(l), 11):
        for j in range(1,6):
            labels.append((l[i].text + "_" + str(j)))
    return labels

def make_dict_of_teams(l, data_start):
    temp_dict = {}
    for i in range(data_start, len(l), 30):
        temp_dict[l[i].text] = l[i + 2].text
    return temp_dict

def put_in_csv(team_dict, row, header):
    folder = 'csv_data\\'
    if os.path.exists(folder + team_dict[row[0]] + '.csv'):
        csvfile = open(folder + team_dict[row[0]] + '.csv', 'a', newline='')
        writer = csv.writer(csvfile)
        writer.writerow(row)
    else:
        csvfile = open(folder + team_dict[row[0]] + '.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerow(row)


        
        
    
