import pandas as pd 
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import time
import re



def scrape():
    executable_path = {'executable_path': r'C:\Users\rafae\Downloads\chromedriver_win32\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    html = browser.html
    time.sleep(2)

    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(2)

    #slides = soup.select_one('ul.item_list li.slide')
    slides22 = soup.select_one('ul.item_list li.slide')
    time.sleep(2)
    slides = slides22.find("div", class_="content_title").get_text()
    
    #news_title = soup.find_all("div", class_="content_title")
    slides23 = soup.select_one('ul.item_list li.slide') 
    time.sleep(2)
    slides2 = slides23.find("div", class_="article_teaser_body").get_text()

    url2 = 'https://jpl.nasa.gov/images'
    browser.visit(url2)
    slides3 = browser.find_by_id("full_image")
    slides3.click()
    more_info_element = browser.links.find_by_partial_text('more info')
    more_info_element.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    img_soup
    image = img_soup.select_one('figure.lede a img')
    img_url = image.get("src")
    img_url = 'https://jpl.nasa.gov' + img_url
    img_url

    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    time.sleep(3) 
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')
    time.sleep(3)
    tweets=soup3.find_all("span",text=re.compile('InSight sol'))
    time.sleep(3)
    
    latestweather = tweets[0].get_text()
    

    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)
    time.sleep(3)
    tables = pd.read_html(url_facts)
    mars_facts = tables[0]
    time.sleep(1)
    mars_facts = mars_facts.to_html()

    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get featured image URL
    cerberus = soup.select_one('div.downloads a')['href']  

    schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli_url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get featured image URL
    schiaparelli = soup.select_one('div.downloads a')['href']

    syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtis_url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get featured image URL
    syrtis = soup.select_one('div.downloads a')['href']

    valles_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(valles_url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get featured image URL
    valles = soup.select_one('div.downloads a')['href']

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles},
    {"title": "Cerberus Hemisphere", "img_url": cerberus},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis}]

    data = {
        'title' : slides,
        'subtitle': slides2,
        'image' : img_url,
        'weather' : latestweather,
        'table' : mars_facts,
        'imageUrls': hemisphere_image_urls
    }
    browser.quit()
    return data