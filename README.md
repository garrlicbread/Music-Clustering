# Music-Clustering

A simple clustering project that identifies anomaly songs based on two variables, energy and danceability. 

Energy of a song refers to the factors that contribute towards keeping the listener engaged. Some of these factors are volume, beats, general pitch, harmonic rhythm, lyrical progression etc. The higher these values are, the higher is the energy of the song.

Danceability of a song describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.

This script clusters all the songs in the dataset and plots the results in high resolution. 

1) It loads a kaggle dataset containing 13 variables of the top songs from the year 2010 - 2019 ranked by Billboard and extracts their Energy and Danceability values. Both range between 0 and 100.

2) After checking for any missing values, it calls the Scikit Learn K-means class and calculates the Within-Cluster-Sum-of-Squares (WCSS) on clusters between 1 and 10. Plotting it helps determine the optimal number of clusters. This process is known as The Elbow Method.

![WCSS3](https://user-images.githubusercontent.com/64068083/101480267-7879b400-3979-11eb-9537-2fb8147d2e78.png)
