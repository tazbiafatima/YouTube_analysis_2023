# YouTube_analysis_2023

## Data Collection

This project aims to create a pipeline classifying YouTube videos on a particular category. 

- The docs directory contains output docs for testing 
- The data directory contains .csv files after the python files have been executed. 

​
8
data_api.py - contains code to create a base dataset of all videos on a particular topic. 
9
-  The method `search_by_keyword` invokes a search to the YouTube Data Api, navigates through page results to create a set of videoIds.
10
- These videoIds are sent to `metadata_extractor` to extract metadata about the video - this is saved as `videos_df` - dataframe
11
- The videoIds from videos_df are sent to the '`statistics_extractor`' method to get likes, views, comments count for data analysis. 
12
- The videoIds from videos_df are sent to the '`comments_extractor`' to invoke Data API to get all comments from a video and creates a comments_df. 
13
​
14

With the above we have a pipeline to get video information using the API 

However, data quota is a challenge in using the API - it gives 10,000 'coins' per key, per day. Different requests have a different cost. 
Comments and Videos call are 1 coin each. Whereas a search is 100 coins - this search_by_keyword will be our biggest expense + challenge in making this realtime. 

To work around this data quota limitation, we will run the recommendations_scraper.py contains a YouTube crawler that does one job only - navigates to a video_url from the videos_df dataset and then find the recommended video from the left panel and goes to it.

It collects video_urls, which are then used by data_api.py to get data for each videos. 

### TO USE THIS DATA COLLECTION METHOD, JUST REPLACE THE KEYWORD in the main function of data_api.py to search by your keyword. 

## CLUSTERING

The datasets are stored in the data directory under the relevant sub-directory of comment, metadata or combined. 
We have implemented two types of clustering - one using just the titles and descriptions of the videos in the clustering_classification.py - all outputs from this are printed in the terminal and second using the titles, descriptions and comments in the YouTube_Analysis_Clustering_2023.ipynb. 

Both clustering first combines using the datasets from previous set, does the data processing, then clustering then either topic modeling or entity extraction. 

### We use k-means clustering with Elbow method to find k 

clustering_classification.py also implements supervised classification to test the precision of the clustering and classifier. 

