import datetime
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import date

def browser_startup_sequence():
    # start browser
    base_url = "https://www.google.com/maps/"
    path = r'Google_Maps_Scraper/chromedriver'
    service = Service(executable_path=r'Google_Maps_Scraper/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    options.add_argument("--lang=en_US");
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def scroll_to_bottom(webdriver):
    try:
        webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        pass

def extract_channel_insights(webdriver, input_url):
    webdriver.get(input_url)
    for i in range(10):
        scroll_to_bottom(driver)
        time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    channel_title = soup.find("h2", {"data-e2e":"user-title"}).text
    user_posts_list = soup.find("div", {"data-e2e":"user-post-item-list"})
    user_posts = user_posts_list.select('div[class*="DivItemContainerV2"]')
    channel_title_lst, video_title_lst, video_url_lst, video_view_lst = ([] for i in range(4))
    for post in user_posts:
        print(post)
        #title
        video_title = post.find("div", {"data-e2e":"user-post-item-desc"}).find("a")["title"]
        #url
        video_url = post.find("div", {"data-e2e":"user-post-item"}).find("a")["href"]
        #viewcount
        video_views = post.find("strong", {"data-e2e":"video-views"}).text
        #append to list
        channel_title_lst.append(channel_title)
        video_title_lst.append(video_title)
        video_url_lst.append(video_url)
        video_view_lst.append(video_views)
    insights_df = pd.DataFrame({"Channel_Title":channel_title_lst,
                                "Video_Title": video_title_lst,
                                "Video_Views":video_view_lst,
                                "URL":video_url_lst})
    return insights_df

driver = browser_startup_sequence()
INPUT_URL = ["https://www.tiktok.com/@cheatsheets",
             "https://www.tiktok.com/@mtholfsen",
             "https://www.tiktok.com/@informatikmentor",
             "https://www.tiktok.com/@tiffintech",
             "https://www.tiktok.com/@exceltips00"]
TODAY = date.today()
driver.get(INPUT_URL[0])
time.sleep(30)
result_df_concat = pd.DataFrame()
for url in INPUT_URL:
    result_df = extract_channel_insights(driver, url)
    result_df_concat = pd.concat([result_df_concat, result_df], ignore_index=True)
for index,row in result_df_concat.iterrows():
    views = row["Video_Views"]
    if "K" in views:
        views = views.replace("K", "00").replace(".","")
    elif "M" in views:
        views = views.replace("M", "000000").replace(".","")
    result_df_concat.loc[index,"Video_Views"] = views
result_df_concat["Video_Views"] = result_df_concat["Video_Views"].astype("int")
result_df_concat = result_df_concat.sort_values(by="Video_Views", ascending=False)
result_df_concat.to_excel(f"Tik_Tok_Insights_{TODAY}.xlsx")
print("Scraping finished")
