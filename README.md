# Music-Clustering

A simple clustering project that identifies anomaly songs based on two variables, energy and danceability. 

Energy of a song refers to the factors that contribute towards keeping the listener engaged. Some of these factors are volume, beats, general pitch, harmonic rhythm, lyrical progression etc. The higher these values are, the higher is the energy of the song.

Danceability of a song describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.

This script clusters all the songs in the dataset into four different clusters based on the features discussed above and detects anomaly songs that have high energy & low danceability and vice versa. All the results are plotted in high resolution. 

First, it loads a kaggle dataset containing 13 variables pertaining to the top songs from the year 2010 - 2019 ranked by Billboard and extracts their Energy and Danceability values, both ranging between 0 and 100.

After checking for any missing values, it calls the Scikit Learn K-means class and calculates the Within-Cluster-Sum-of-Squares (WCSS) on clusters between 1 and 10. Plotting it helps determine the optimal number of clusters. This process is known as The Elbow Method:

![WCSS](https://user-images.githubusercontent.com/64068083/101480925-5df40a80-397a-11eb-8787-ba5eb1362e42.png)

We can see that beyond the fourth cluster, the fall in the WCSS isn't significant. Hence, we plot the k-means predictions on four clusters:

![K-means clustering](https://user-images.githubusercontent.com/64068083/101481312-f8544e00-397a-11eb-80b9-40e352ac9e0f.png)

Finally, the script plots & prints the names of 10 random anomaly songs on a scatterplot.

![Anomaly_songs2](https://user-images.githubusercontent.com/64068083/101482443-bfb57400-397c-11eb-8370-157710c5fbbd.png)

The text output is as follows:

*The model has been trained and anomalies have been identified. A random number of samples have been extracted from all 600 predictions.*

*Here are a couple of anomaly songs that are low on danceability but high on energy:*

*1) Neon Trees: Everybody Talks*
*2) T.I.: Castle Walls (feat. Christina Aguilera)*
*3) Calvin Harris: Blame*
*4) Little Mix: How Ya Doin'? (feat. Missy Elliott)*
*5) Alessia Cara: Here*

*Here are a couple of anomaly songs that are high on danceability but low on energy:*

*1) Bruno Mars: Treasure*
*2) Nicki Minaj: Anaconda*
*3) Mr. Probz: Waves - Robin Schulz Radio Edit*
*4) Macklemore & Ryan Lewis: Thrift Shop (feat. Wanz)*
*5) Maroon 5: What Lovers Do (feat. SZA)*

*This program took 23.19 seconds to execute.*
