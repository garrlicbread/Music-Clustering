# Clustering performed with K-Means and Hierarchical algorithms 

# Importing the libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("C:/Users/Sukant Sidnhwani/Desktop/Python/Projects/Music Clustering/Spotify.csv", 
                      encoding = "ISO-8859-1")

X = df.iloc[:, [6, 7]].values

# Checking for missing values 
pd.DataFrame(X).isnull().any()

# A) K - nearest neighbors 

# Using elbow method to find the optimal number of clusters 
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, random_state = 1)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(dpi = 1200)
plt.style.use('dark_background')
plt.plot(range(1, 11), wcss, marker = 'o')
plt.title("The Elbow Method")
plt.xlabel("No. of clusters")
plt.ylabel("WCSS")
plt.show()

# Training the K-means model on the dataset 
kmeans = KMeans(n_clusters = 4)
k_pred = kmeans.fit_predict(X)

# Visualizing the clusters
plt.grid(b = None)
plt.figure(figsize = (10, 10), dpi = 1200)
plt.style.use('dark_background')
plt.scatter(X[k_pred == 0, 0], X[k_pred == 0, 1], s = 15, c = '#cb4335', marker = r'X') # Red: High Danceability, High Energy
plt.scatter(X[k_pred == 1, 0], X[k_pred == 1, 1], s = 15, c = '#e8ec05', marker = r'X') # Yellow: Medium Danceability, Medium Energy
plt.scatter(X[k_pred == 2, 0], X[k_pred == 2, 1], s = 15, c = '#33fff6', marker = r'X') # Cyan: Medium Danceability, High Energy
plt.scatter(X[k_pred == 3, 0], X[k_pred == 3, 1], s = 15, c = '#29e790', marker = r'X') # Green: High Danceability, Medium energy
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 20, c = '#ebebeb', marker = r'X') # White: Center Point
plt.title("K-means Clustering")
plt.xlabel("Energy")
plt.ylabel("Danceability")
plt.show()

# Creating a sample of random predictions
kdf = pd.DataFrame(k_pred)
names = []
samples = kdf.sample(200)
X_demo = [X[index] for index in samples.index]
X_demo = np.array(X_demo, dtype = 'int64')
X_demo_df = pd.DataFrame(X_demo)
sampless = np.array(samples, dtype = 'int32')
sampless = sampless.flatten()
samples = pd.DataFrame(samples)
samples = samples.reset_index(level = 0) 
samples = samples.rename(columns={"index": "Song index", 0: "Cluster"})
for i in samples['Song index']:   
    nam = str(df['artist'][i]), ": ", str(df['title'][i])
    nam = "".join(nam)
    names.append(nam)  
samples['Song'] = names
samples['Energy'] = X_demo_df[0]
samples['Danceability'] = X_demo_df[1]

C2 = samples[samples['Cluster'] != 2].index
C2 = samples.drop(C2)
C2_index = C2[C2['Energy'] <= 80].index
C2 = C2.drop(C2_index)
C2_index = C2[C2['Danceability'] >= 50].index
C2 = C2.drop(C2_index)
if C2.shape[0] > 5:
    C2 = C2.sample(5)
C2_min, C2_max = C2['Danceability'].min(), C2['Energy'].max()
C2_x_list = C2['Energy'].tolist()
C2_y_list = C2['Danceability'].tolist()

C3 = samples[samples['Cluster'] != 3].index
C3 = samples.drop(C3)
C3_index = C3[C3['Danceability'] <= 75].index
C3 = C3.drop(C3_index)
if C3.shape[0] > 5:
    C3 = C3.sample(5)
C3_max, C3_min = C3['Danceability'].max(), C3['Energy'].min()
C3_x_list = C3['Energy'].tolist()
C3_y_list = C3['Danceability'].tolist()

minim = min([C2_min, C3_min])
maxim = max([C2_max, C3_max])

# Plotting anomaly song names
plt.grid(b = None)
plt.figure(figsize = (15, 15), dpi = 1200)
plt.xlim(minim - 5, maxim + 15)
plt.ylim(minim - 5, maxim + 5)
plt.style.use('dark_background')
plt.title("Anomaly detection in Music")
plt.xlabel("Energy")
plt.ylabel("Danceability")
s = plt.scatter(x = C2['Energy'], y = C2['Danceability'], s = 35, c = '#33fff6', marker = r'X') # Cyan: Medium Danceability, High Energy))
plt.scatter(x = C3['Energy'], y = C3['Danceability'], s = 35, c = '#29e790', marker = r'X') # Green: High Danceability, Medium Energy))
for i, text in enumerate(C2['Song']):
    names = plt.annotate(text, xy = (C2_x_list[i] + 0.5, C2_y_list[i] - 0.25))
for i, text in enumerate(C3['Song']):
    names = plt.annotate(text, (C3_x_list[i] + 0.5, C3_y_list[i] - 0.25))
plt.show()

print()
print("The model has been trained and anomalies have been identified. A random number of samples have been extracted from all 600 predictions.\n")
print("Here are a couple of anomaly songs that are low on danceability but high on energy:\n")
for i, text in enumerate(C2['Song']):
    print(i + 1, text)
print()
print("Here are a couple of anomaly songs that are high on danceability but low on energy:\n")
for i, text in enumerate(C3['Song']):
    print(i + 1, text)
  
############################################# B) Hierarchical clustering ####################################################################333

# # It's commented out because K Means works better than hierarchical clustering
# # Plotting a dendrogram to find the optimal number of clusters 

# dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
# plt.title("Dedrogram")
# plt.xlabel("Songs")
# plt.ylabel("Eucledian Distance")
# plt.show()

# # Training the hierachical model on the dataset 
# hc = AgglomerativeClustering(n_clusters = 4, linkage = 'ward', affinity = 'euclidean')
# hc_pred = hc.fit_predict(X)

# # Visualizing the clusters
# plt.scatter(X[hc_pred == 0, 0], X[hc_pred == 0, 1], s = 75, c = 'red') # High Danceability, High Energy
# plt.scatter(X[hc_pred == 1, 0], X[hc_pred == 1, 1], s = 75, c = 'yellow') # Low Danceability, Low Energy
# plt.scatter(X[hc_pred == 2, 0], X[hc_pred == 2, 1], s = 75, c = 'cyan') # Low Danceability, High Energy
# plt.scatter(X[hc_pred == 3, 0], X[hc_pred == 3, 1], s = 75, c = 'green') # High Danceability, Low energy
# plt.title("Hierarchical Clustering")
# plt.xlabel("Energy")
# plt.ylabel("Danceability")
# plt.show()