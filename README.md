# Music-Clustering

A simple clustering project that identifies anomaly songs based on two variables, energy and danceability. 

Energy of a song refers to the factors that contribute towards keeping the listener engaged. Some of these factors are volume, beats, general pitch, harmonic rhythm, lyrical progression etc. The higher these values are, the higher is the energy of the song.

Danceability of a song describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.

This script clusters all the songs in the dataset based on the features discussed above and detects anomaly songs that have high energy & low danceability and vice versa. All the results are plotted in high resolution. 

First, it loads a kaggle dataset containing 13 variables pertaining to the top songs from the year 2010 - 2019 ranked by Billboard and extracts their Energy and Danceability values, both ranging between 0 and 100.

After checking for any missing values, it calls the Scikit Learn K-means class and calculates the Within-Cluster-Sum-of-Squares (WCSS) on clusters between 1 and 10. Plotting it helps determine the optimal number of clusters. This process is known as The Elbow Method:


![WCSS](https://user-images.githubusercontent.com/64068083/101480925-5df40a80-397a-11eb-8787-ba5eb1362e42.png)


We can see that beyond the fourth cluster, the fall in the WCSS isn't significant. Hence, we plot the k-means predictions on four clusters. The white points indicate cluster centers:


![K-means clustering](https://user-images.githubusercontent.com/64068083/101481312-f8544e00-397a-11eb-80b9-40e352ac9e0f.png)


Finally, the script plots & prints the names of 10 random anomaly songs on a scatterplot. View [output.md](output.md) to see the printed output.


![Anomaly_songs2](https://user-images.githubusercontent.com/64068083/101482443-bfb57400-397c-11eb-8370-157710c5fbbd.png)


Notes and bugs:

1) A random state has been set when calling the clustering class so that the predicted clusters align with what we want to plot. This does not affect the random songs extracted.
2) If the songs to be plotted are too similar in energy or danceability, the text overlaps. This can't be avoided but increasing the dpi of the plot helps to increase the distance between the texts.
3) Another clustering technique called Hierarchical clustering can be performed but has been commented out. In practice, K-means performs better.
4) Dataset: https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year
