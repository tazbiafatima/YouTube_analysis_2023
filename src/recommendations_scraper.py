import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import date
driver = webdriver.Chrome()

recommended_videos = pd.DataFrame(columns=['videoId'])

#The idea is to start using our base dataset and run this scraper to go find urls to the recommended videos on the right panel of a youtube page.
def get_recommended_videos(videos_df):
    i = 1
    all_links = []
    for url in videos_df['videoUrl']:
        print("The url is:", url)
        i = i + 1 #variables used to act as stopping condition - can discuss the stopping condition for the crawler
        driver.get(url)
        #recommended_videos = driver.find_elements(by=By.CLASS_NAME, value='//*[@id="dismissible"]/div/div[1]/a')
        wait = WebDriverWait(driver, 20)
        try:
            all_videos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="dismissible"]/div/div[1]/a')))
            print("The entire video collection is:", len(all_videos))
        except:
            continue
        links = []
        for video in all_videos:
            #get urls from each <a> anchor tag
            video_link = video.get_attribute('href')
            print("The video is:", video)
            links.append(video_link)
            with open('video_urls.txt', 'a') as out:
                pprint(links, stream=out)
        #stopping condition
        all_links.extend(links)
        if i >= 200:
            break
    print(links)
    print("The length of links is:", len(all_links))
    recommended_videos['videoId'] = all_links

    return recommended_videos

if __name__ == '__main__':
    date = date.today()
    print("we are here")
    videos_set = pd.read_csv(r'../data/Thesis-Dataset/Videos_Dataframe_25022023_2.csv')
    videos_df = get_recommended_videos(videos_set)
    videos_df.to_csv(fr'../data/Thesis-Dataset/Recommended/Videos_Df_{date}.csv')
    print("Call completed")
