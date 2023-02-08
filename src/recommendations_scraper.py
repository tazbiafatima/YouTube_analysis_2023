import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()

#The idea is to start using our base dataset and run this scraper to go find urls to the recommended videos on the right panel of a youtbe page.
def get_recommended_videos(videos_df):
    i = 1
    for url in videos_df['videoUrl']:
        i = i + 1 #variables used to act as stopping condition - can discuss the stopping condition for the crawler
        driver.get(url)
        #recommended_videos = driver.find_elements(by=By.CLASS_NAME, value='//*[@id="dismissible"]/div/div[1]/a')
        wait = WebDriverWait(driver, 20)
        try:
            all_videos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="dismissible"]/div/div[1]/a')))
        except:
            continue
        links = []
        for video in all_videos:
            #get urls from each <a> anchor tag
            video_link = video.get_attribute('href')
            links.append(video_link)
            with open('video_urls.txt', 'w') as out:
                pprint(links, stream=out)
        #stopping condition
        if i > 2:
            break
    print(links)

if __name__ == '__main__':
    print("we are here")
    videos_df = pd.read_csv(r'/Users/tabziasmac/Downloads/Thesis-Dataset/Videos_Dataframe_1.csv')
    get_recommended_videos(videos_df)
    print("Call completed")
