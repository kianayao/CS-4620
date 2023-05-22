# making a perfect KDA = 20
# cluster by role, 5 graphs for each role
# compare by D@15 data
# X will be the D@15 data
# Y will be the true labels (region)
# CN = 0   KR = 1   NA = 2   PCS = 3   EUW = 4   VN = 5
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import clustering_funcs as cf

files = ['adc.csv', 'jungle.csv', 'mid.csv', 'support.csv', 'top.csv']
db = []
X = []
Y = []

for f in files:
  db = cf.get_csv(f)
  X = cf.get_rel_data_all(db)
  Y = cf.get_truth(db)

  km = KMeans(n_clusters = 6, init = 'random',
              n_init = 10, max_iter = 300, 
              tol = 1e-04, random_state = 0)

  labels = km.fit_predict(X)
  acc = cf.acccuracy(labels, Y)
  print(acc * 100)
  x = [item[0] for item in X]
  y = [item[1] for item in X]

  np_X = np.array(X)
  
  # plotting the clustering results
  filtered_label0 = np_X[labels == 0]
  filtered_label1 = np_X[labels == 1]
  filtered_label2 = np_X[labels == 2]
  filtered_label3 = np_X[labels == 3]
  filtered_label4 = np_X[labels == 4]
  filtered_label5 = np_X[labels == 5]
  plt.scatter(filtered_label0[:,0], filtered_label0[:,1], c = 'red', label = 'Cluster 1')
  plt.scatter(filtered_label1[:,0], filtered_label1[:,1], c = 'blue', label = 'Cluster 2')
  plt.scatter(filtered_label2[:,0], filtered_label2[:,1], c = 'green', label = 'Cluster 3')
  plt.scatter(filtered_label3[:,0], filtered_label3[:,1], c = 'orange', label = 'Cluster 4')
  plt.scatter(filtered_label4[:,0], filtered_label4[:,1], c = 'black', label = 'Cluster 5')
  plt.scatter(filtered_label5[:,0], filtered_label5[:,1], c = 'pink', label = 'Cluster 6')

  # plot truth clusters
  # plt.scatter(x[0:30] , y[0:30], c = 'red', label ='CN')
  # plt.scatter(x[30:50] , y[30:50], c = 'blue', label = 'EUW')
  # plt.scatter(x[50:84] , y[50:84], c = 'green', label = 'KR')
  # plt.scatter(x[84:102] , y[84:102], c = 'orange', label = 'NA')
  # plt.scatter(x[102:108] , y[102:108], c = 'black', label = 'PCS')
  # plt.scatter(x[108:116] , y[108:116], c = 'pink', label = 'VN')
  
  # plt.xlabel('gd@15')
  # plt.ylabel('xpd@15')
  plt.xlabel('PC1')
  plt.ylabel('PC2')
  plt.title(f)
  plt.legend()
  
  # plot the centroids
  plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
              s = 250, marker = '*',
              c = 'red', edgecolor = 'black',
              label = 'centroids')

  plt.show()

# accuracies
# adc - 9.649122807017543
# jungle - 20.175438596491226
# mid - 16.666666666666664
# sup - 18.421052631578945
# top - 14.035087719298245