import pandas at pd
import numpy as np
from bs4 import BeautifulSoup
from splinter import Browser


def AllData():
    
    browser = Browser('chrome', executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": Image(browser),
        "weather": Twitter(browser),
        "facts": Facts(),
    


    }

browser.quit()
return data

#NASA Mars News

def News(browser):
browser.visit('https://mars.nasa.gov/news/')
html = browser.html
news = BeautifulSoup(html, 'html.parser')
slide = news.select_one('ul.item_list li.slide')
news_title = slide.find("div", class_='content_title').get_text()
news_paragraph=slide.find('div', class_="article_teaser_body").get_text()
return news_title, news_paragraph


# MARS WEATHER (TWITTER)

def Twitter(browser):
   url2 = 'https://twitter.com/marswxreport?lang=en'
   browser.visit(url2)
   html3 = browser.html
   Weather = BeautifulSoup(html3, 'html.parser')
   Tweet = Weather.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"}) 
   mars_weather = Tweet.find('p', 'tweet-text').get_text()

return mars_weather


#JPL Mars Space Images - Featured Images
def Image (browser):
   browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
   FullImage=browser.find_by_id('full_image')
   FullImage.click()
   browser.is_element_present_by_text('more info')
   MoreInfo = browser.find_link_by_partial_text('more info')
   MoreInfo.click()
   html2=browser.html
   Image=BeautifulSoup(html2, 'html.parser')
   Relative=Image.select_one('figure.lede a img').get("src")
   featured_image_url = f'https://www.jpl.nasa.gov{Relative}'

return featured_image_url


#Mars Facts

def Facts():
   table = pd.read_html('http://space-facts.com/mars/')
   table[0].columns=['Attribute','Value']

return table[0].to_html()



