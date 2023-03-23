# YouTube_analysis_2023

This project aims to create a pipeline classifying YouTube videos on a particular category. 

The docs directory contains output docs for testing 
The data directory contains .csv files after the python files have been executed. 

data_api.py - contains code to create a base dataset of all videos on a particular topic. 
The method search_by_keyword invokes a search to the YouTube Data Api, navigates through page results to create a set of videoIds.
These videoIds are sent to metadata_extractor to extract metadata about the video - this is saved as videos_df - dataframe
The videoIds from videos_df are sent to the 'statistics_extractor' method to get likes, views, comments count for data analysis. 
The videoIds from videos_df are sent to the 'comments_extractor' to invoke Data API to get all comments from a video and creates a comments_df. 

With the above we have a pipeline to get video information using the API 
However, data quota is a challenge in using the API - it gives 10,000 'coins' per key, per day. Different requests have a different cost. 
Comments and Videos call are 1 coin each. Whereas a search is 100 coins - this search_by_keyword will be our biggest expense + challenge in making this realtime. 
I've applied for extra api quota but haven't gotten a response yet. 

The recommendations_scraper.py contains a YouTube crawler that does one job only - navigates to a video_url from the videos_df dataset and then find the recommended video from the left panel and goes to it.
Kind of like an endless loop. 
All it collects is video_urls. 

The initial idea for the pipeline was to use this list of video_urls and feed it back to data_api to get the metadata, statistics and comments from the API - since it's a cleaner code and faster result. 

However, due to the limitation of the api quota, I'm considering just scraping all the metadata and comments from each video. We have to determine the stopping condition here and how to access more historical bideos like those in 2019-2020-2021

If we use the api to search we can sort by date abd get older results. 

Next Steps: 
Continue to work on the data-collection pipeline - towards making it real-time 
Use existing dataset from api and keep collecting from api to perform the classification. 

For the classifier - more than comments - it looks like "Description" text is more appropriate. A combination of both might help.
The comments can be used to analyse the engagement on the video though. 

There are some explicit results showing up when collecting data from the api - Have to add functionality to filter for this before adding to the dataframe.

