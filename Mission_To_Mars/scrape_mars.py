#!/usr/bin/env python
# coding: utf-8

#pip install lxml

# Dependencies
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # In[5]:
    # # URL of page to be scraped
    # #driver = webdriver.Chrome("C:/Users/vasu0/Downloads/chromedriver_win32/chromedriver.exe")
    # #driver = webdriver.Chrome()
    # #driver.get('https://redplanetscience.com/')

    redPlanetHTML = browser.html
    redPlanetSoup = bs(redPlanetHTML, 'html.parser')
    
    results = redPlanetSoup.find_all('div', class_='content_title')
    # loop over results to get data
    for result in results:
        title = result.text
        break
    
    newsResults = redPlanetSoup.find_all('div', class_='article_teaser_body')
    for newsResult in newsResults:
        news = newsResult.text
        break
    print (title)
    print (news)
    
    browser.quit()

# Mars Space Image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    
    marsImgHTML = browser.html
    marsImgSoup = bs(marsImgHTML, 'html.parser')
    marsImgs = marsImgSoup.find_all('div', class_='floating_text_area')
    
    for marsImg in marsImgs:
        link = marsImg.find('a')
        href = link['href']
        break
    
    featured_image_url = 'https://spaceimages-mars.com/' + href
    print (featured_image_url)
    
    browser.quit()

# Mars Facts
    facts_url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(facts_url)
    tables
    
    df = tables[1]
    df.head()
    
    html_table = df.to_html()
    html_table
    
    html_table.replace('\n', '')
    
    df.to_html('table.html')

# Mars Hemispheres

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = 'https://marshemispheres.com'
    browser.visit(url)
    
    marsHemisHTML = browser.html
    marsHemisSoup = bs(marsHemisHTML, 'html.parser')
    
    hemisDict = {"hemiTitle":[],"img_url":[]}
    
    marsHemis = marsHemisSoup.find_all('div', class_='item')

    for marsHemi in marsHemis:
        link = marsHemi.find('a')
        href = link['href']
        hemi = href.split('.')[0]
        hemi_full_h3 = marsHemi.find('h3')
        hemi_full = hemi_full_h3.text
        hemi_name = hemi_full.split('Hemi')[0]
        hemi_name = hemi_name.lower()
        hemi_name = hemi_name.rstrip()
        hemisphere = hemi + ' Hemisphere'
        url_end = 'images/' + hemi_name + '_enhanced-full.jpg'
        hemisphere_url = 'https://marshemispheres.com/' + url_end
        hemisDict["hemiTitle"].append(hemisphere)
        hemisDict["img_url"].append(hemisphere_url)
        
    print (hemisDict)

    browser.quit()

    marsDict = {}

    print ("Featured Image")
    print (featured_image_url)

    marsDict = {
        "featured_img": featured_image_url,
        "news": news,
        "news_title": title
    }

    marsDict["hemisphere"] = hemisDict

    print (marsDict)
    return marsDict
    #print (marsDict["hemisphere"])

#if __name__ == "__main__":
#    # If running as script, print scraped data
#    print(scrape())







