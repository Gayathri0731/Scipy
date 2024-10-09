# K-means Clustering Algorithm in Scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2 

a = np.random.multivariate_normal([0,6],[[2,1],[1,1.5]],size=200)
b = np.random.multivariate_normal([2,0],[[1,-1],[-1,3]],size=400)
c = np.random.multivariate_normal([6,4],[[5,0],[0,1.2]],size=250)

z = np.concatenate((a,b,c))
np.random.shuffle(z)
plt.scatter(z[:,0],z[:,1])
# plt.show()

k=3

centroids,labels = kmeans2(z,k,minit='points')
print(f'Centroids:{centroids}')
print(f'z:{z}')
print(labels)

cluster_1= z[labels==0]
cluster_2= z[labels==1]
cluster_3= z[labels==2]

plt.scatter(cluster_1[:,0],cluster_1[:,1],label="cluster_1")
plt.scatter(cluster_2[:,0],cluster_2[:,1],label="cluster_2")
plt.scatter(cluster_3[:,0],cluster_3[:,1],label="cluster_3")
plt.scatter(centroids[:,0],centroids[:,1],label="centroids",color="black")
plt.show()