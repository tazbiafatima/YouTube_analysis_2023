from googleapiclient.discovery import build
import pandas as pd
from datetime import date
import os
import numpy as np
from numpy import nan
import sys

# Arguments that need to be passed to the build function
DEVELOPER_KEY = "AIzaSyBpDGSPpVRtS-qWVI6-qisByu3_PbErgHw"
    #"AIzaSyD4y8XJV48ZYsslvV14QFFKDtc3ysTMMWQ"
    #"AIzaSyA_YBytnNpd_E-hAPb0ZtNAztQHGQeJG2U"
    #"AIzaSyACGb0J5vc-ht2J_i8YnsJ23BXoAA0lfMs"
    #"AIzaSyCZs9O1YSC78QLeUy2VI4E5za6Ft1vI0YM"
    #"AIzaSyDT-pfXF2yJ5tM2rUPYpFhOhPNPL9Ld7oQ"
    #"AIzaSyCouml6h-qe5EOSwET0ovsf5RMODc-NbsM"
    #"AIzaSyBulDTm0bca0Uo4ujTmcEhoEGhBklhLB4Y"
    #"AIzaSyAjXeDoru-OUDAJ1rR-BvWEArhGOrsCQ4s"
    #"AIzaSyDJ8_kexjuBwGRVyWZBLhDiVxRU7ezIVRc"
    #"AIzaSyDvAZhY9aSY7YvWcck5J72DigPfOOmKsO0"
    #"AIzaSyApiBTZgAOVNbRaLB7F2f7reIUoM4x_xZE"
    #"AIzaSyDyIPEbZyXYGnWbpYVw8aelRSWii9PYdXk"


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
all_results = []
videos_df = pd.DataFrame(columns=['videoId', 'publishedDate', 'title', 'videoUrl', 'description', 'channelId', 'channelTitle'])
videoStats_df = pd.DataFrame(columns=['videoId', 'tags', 'viewCount', 'likeCount', 'favoriteCount', 'commentCount'])
comments_df = pd.DataFrame(columns=['videoId', 'new_comment', 'author_name', 'author_id', 'replies'])

quota = 10000

def search_by_keyword(query, max_results, quota):
    # calling the search.list method to
    # retrieve youtube search results
    prevPageToken = None
    iter = 0
    search_response = youtube_object.search().list(q=query, part="id, snippet", maxResults=max_results).execute()
    iter = -1
    while(iter == -1):
        # extracting the results from search response
        result = search_response.get("items", [])
        nextPage = search_response.get("nextPageToken")
        print("next page token is", nextPage)
        #print("Length of search result:", len(result))
        if result:
            all_results.extend(result)
            #print("New length of All results are:", len(all_results))
        if ((nextPage != None) & (quota >= 9900)):
            search_response = youtube_object.search().list(q=query, part="id, snippet", maxResults=max_results, pageToken=nextPage).execute()
            quota = 10000 - 100
        else:
            iter = 0
            break
    print("Out of while loop")
    return all_results

def metadata_extractor(all_results, flag):
    # extracting required info from each result object
    print("ALL_RESULTS ARE:", all_results)
    for result in all_results:
    #video result object
        print("RESULT is:", result)
        print("RESULTS PRINTED")
        print("RESULT ID KIND", result['kind'])
        if flag == '0' and result['id']['kind'] == "youtube#video":
            videoId = result["id"]["videoId"]
        if flag == '1' and result['kind'] == "youtube#video":
            videoId = result['id']
        else:
            continue
        if videoId:
            publishedDate = result['snippet']['publishedAt']
            title = result["snippet"]["title"]
            videoUrl = "https://www.youtube.com/watch?v=" + str(videoId)
            description = result['snippet']['description']  #text from the descriptionbox of each video
            channelId = result["snippet"]["channelId"]
            channelTitle = result["snippet"]["channelTitle"]
            videos_df.loc[len(videos_df.index)] = [videoId, publishedDate, title, videoUrl, description, channelId, channelTitle]

    return videos_df

def statistics_extractor(videos_df, flag):
    all_stats = []
    all_dfs = []
    i = 0
    x = 0
    videoIds = videos_df['videoId']
    videos_df_2 = pd.DataFrame()
    #print()
    while i < len(videoIds):
        j = i + 50  # using these variables as only 50 videoIds can be sent at a time to the api
        video_subset = videoIds[i:j]
        print("The video subset is:", video_subset)
        video_subset = [i.replace('https://www.youtube.com/watch?v=', '') for i in video_subset]
        video_subset = ','.join(video_subset)
        print("VIDEO SUBSET IS:", video_subset)
        stats_response = youtube_object.videos().list(part="id, snippet, statistics", id=video_subset).execute()
        if stats_response:
            print("STATS RESPONSE IS", stats_response)
            stats = stats_response.get("items", [])
            print("STATS ARE: ", stats)
        all_stats.extend(stats)
        print("FLAG IS: ", flag)
        if flag == '1':
            videos_df_temp = metadata_extractor(all_stats, flag)
            print("VIDEOS DF TEMP", videos_df_temp)
            print("X IS:", x)
            #videos_df_2 = pd.DataFrame.combine(videos_df_2, videos_df_temp)
            all_dfs.append(videos_df_temp)
            x = x + 1
        i = j
    print("ALL_DFS is :", all_dfs)
    videos_df_2 = pd.concat(all_dfs)
    for video in all_stats:
        if video['kind'] == "youtube#video":
            videoId = video["id"]
            if 'tags' in video['snippet'].keys():
                tags = video['snippet']['tags']  #get tags for each video
            else:
                tags = None
            if 'viewCount' in video["statistics"].keys():
                viewCount = video["statistics"]["viewCount"] #get number of views for each video
            else:
                viewCount = None
            if 'likeCount' in video['statistics'].keys():
                likeCount = video['statistics']['likeCount'] #get number of likes for each video
            else:
                likeCount = None
            if 'favoriteCount' in video["statistics"].keys():
                favoriteCount = video["statistics"]["favoriteCount"]
            else:
                favoriteCount = None
            if 'commentCount' in video["statistics"].keys():
                commentCount = video["statistics"]["commentCount"] #get number of comments for each video
            else:
                commentCount = None
            videoStats_df.loc[len(videoStats_df.index)] = [videoId, tags, viewCount, likeCount, favoriteCount, commentCount]
    if flag == '1':
        return videos_df_2, videoStats_df
    if flag == '0':
        return videoStats_df

#comment extractor code. We have a list of videoURLs you have to get all comments.
def comments_extractor(videos_df):
    all_comments = []
    i = 0
    videoIds = videos_df['videoId']
    while i < len(videoIds):
        j = i + 50  #using these variables as only 50 videoIds can be sent at a time to the api
        video_subset = videoIds[i:j]
        for video in video_subset:
            try:
                if flag == '1':
                    video = video.replace('https://www.youtube.com/watch?v=', '')
                comments_response = youtube_object.commentThreads().list(part="id, snippet, replies", videoId=video).execute()
            except:
                print("Request failed: Disabled Comments")
            # Handle error here
            if comments_response:
                comments = comments_response.get("items", [])
                all_comments.extend(comments)
        i = j
    for comment in all_comments:
        if comment['kind'] == "youtube#commentThread":
            videoId = comment['snippet']['videoId']
            new_comment = comment['snippet']['topLevelComment']['snippet']['textOriginal']       #comment text
            author_name = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']  #who wrote the comment
            author_id = comment['snippet']['topLevelComment']['snippet']['authorChannelId']['value'] #channel id of the commentor
            replies = []
            if 'replies' in comment['snippet']['topLevelComment'].keys():    #This is to capture reply threads of each comment - not working yet - have to check
                for reply in comment['snippet']['topLevelComment']['replies']['comments']:
                    videoId = reply['snippet']['videoId']
                    new_comment = reply['snippet']['textOriginal']
                    author_name = reply['snippet']['authorDisplayName']
                    author_id = comment['snippet']['authorChannelId']['value']
                    comment_reply = {
                        'videoId' : videoId,
                        'new_comment': new_comment,
                        'author_name': author_name,
                        'author_id': author_id
                    }
                    replies.extend(comment_reply)

            comment = {
                'videoId': videoId,
                'new_comment': new_comment,
                'author_name': author_name,
                'author_id': author_id,
                'replies': replies if replies else None
            }
            comments_df.loc[len(comments_df.index)] = [videoId, new_comment, author_name, author_id, replies]

    return comments_df

if __name__ == '__main__':
    date = date.today()
    flag = sys.argv[1]
    print("The flag is:", flag)
    if flag == '0': #you want to collect video data by search
        #search_keywords = ['Donkey India to USA', 'Donki', 'Serbia India', 'Panama Donki Donkey', 'USA Border Crossing India'] #Functionality to search multiple keywords - raises concerns of Data quota per day per api key
        search_keywords = ['Donki Dunki', 'Donkey India to USA']
        results_dict = {}
        for i in search_keywords:
            #get search results
            keyword_result = search_by_keyword(i, max_results=50, quota=quota)
            #get video info
            videos_df = metadata_extractor(keyword_result, flag)
            # drop duplicates by videoId
            videos_df = videos_df.drop_duplicates(subset='videoId', keep="first")
            #get video stats
            videoStats_df = statistics_extractor(videos_df, flag)
            # drop duplicates by videoId
            videoStats_df = videoStats_df.drop_duplicates(subset='videoId', keep="first")
            #get comments
            comments_df = comments_extractor(videos_df)
            term = str(i)
            term = term.replace(' ', '_')
            #Save to CSV
            videos_df.to_csv(fr'../data/Thesis-Dataset/Videos_Dataframe_{date}_{term}.csv')
            videoStats_df.to_csv(fr'../data/Thesis-Dataset/Videos_Stats_Dataframe_{date}_{term}.csv')
            comments_df.to_csv(fr'../data/Thesis-Dataset/Comments_Dataframe_{date}_{term}.csv')

    if flag == '1': #you want to collect video data of a list of videos
        videos = pd.read_csv(f'../data/Thesis-Dataset/Videos_Df_2023-04-10.csv')
        print("videos is:", videos)
        videos  = videos.dropna()
        #get all metadata and statistics:
        videos_df, videoStats_df = statistics_extractor(videos, flag)
        videos_df = videos_df.drop_duplicates(subset='videoId', keep="first")
        videoStats_df = videoStats_df.drop_duplicates(subset='videoId', keep="first")
        #get all comments for each list
        comments_df = comments_extractor(videos)
        # Save to CSV
        videos_df.to_csv(fr'../data/Thesis-Dataset/Videos_Dataframe_{date}_rec.csv')
        videoStats_df.to_csv(fr'../data/Thesis-Dataset/Videos_Stats_Dataframe_{date}_rec.csv')
        comments_df.to_csv(fr'../data/Thesis-Dataset/Comments_Dataframe_{date}_rec.csv')








