import csv
from sklearn.decomposition import PCA
def get_csv(f):
    temp = []
    with open('csv_role/' + f, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                temp.append(row)
    return temp

def get_rel_data_xp_g(db):
    vals = []
    for row in db:
        temp = []
        for i in range(5, len(row) - 2, 1):
            temp.append(int(row[i]))
        vals.append(temp)
    return vals

def get_rel_data_all(db):
    vals = []
    for row in db:
        temp = []
        for i in range(5, len(row), 1):
            temp.append(int(row[i]))
        vals.append(temp)
    pca = PCA(2)
    data = pca.fit_transform(vals)
    return data

def get_truth(db):
    vals = []
    for row in db:
        vals.append(int(row[0]))
    return vals

def acccuracy(labels, truth):
    counter = 0
    t_counter = 0
    for l, t in zip(labels, truth):
        if (l == t):
            t_counter += 1
        counter += 1
    return t_counter / counter
