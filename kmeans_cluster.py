import numpy as np
import random as rd
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.cluster import KMeans

file_name = loadmat(' #name of your matlab file') 
x = file_name['X']
print(x.shape)
plt.scatter(x[:,0],x[:,1])
plt.show()

q = [2,3,4]
for k in q:
  itterations = 100
  centroid_of_cluster = np.empty([2,0]) #random value of centroid
  # print(centroid_of_cluster.shape)
  for i in range(k):
    a = rd.randint(0 , 599)
    centroid_of_cluster = np.c_[centroid_of_cluster , x[a]]
  # print(centroid_of_cluster)
  centroid_of_cluster = centroid_of_cluster.transpose() 
  # print(centroid_of_cluster)
  # print(x)

  final_distance = np.empty([600,0])
  for i in range(itterations):
    final_distance = np.array([[ np.linalg.norm(i -j) for j in centroid_of_cluster] for i in x])
    c=np.argmin(final_distance, axis=1)+1
    #print(c)

    updated_centroid={}
    for p in range(k):
        updated_centroid[p+1]=np.empty([2,0])
    for i in range(600):
        updated_centroid[c[i]]=np.c_[updated_centroid[c[i]],x[i]]
        
    for p in range(k):
        updated_centroid[p+1]=updated_centroid[p+1].T
        centroid_of_cluster[p,:]=np.mean(Y[p+1],axis=0)


  color=['red','blue','green','yellow']
  print('The plot for k equals to ' +str(k) + ' is as follows:')
  for i in range(k):
      plt.scatter(updated_centroid[i+1][:,0],updated_centroid[i+1][:,1],c=color[i])
  plt.scatter(centroid_of_cluster.T[0,:],centroid_of_cluster.T[1,:], marker="x" ,c='black')
  plt.show()
# q=[2,3,4]
for n_clusters in q:
  kmeans = KMeans(n_clusters=n_clusters, random_state=0,max_iter=1000).fit(x)
  y_pred = KMeans(n_clusters=n_clusters, random_state=100).fit_predict(x)
  centroid = kmeans.cluster_centers_
  print('The plot for k equals to ' +str(n_clusters) + ' is as follows:')
  plt.scatter(x[:, 0], x[:, 1], c=y_pred)
  plt.scatter(centroid[:,0], centroid[:,1], marker="x" ,c='black')
  plt.show()

