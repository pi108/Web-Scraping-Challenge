  
# =========================================================
# IMPORT ALL RELEVANT MODULES
# =========================================================


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


# =========================================================
# FUNCTION TO SAVE TO TEXT FILE FOR ANALYSIS
# =========================================================


def savetofile(contents):
    file = open('_temporary.txt',"w",encoding="utf-8")
    file.write(contents)
    file.close()


# =========================================================
# START OF FUNCTION TO SCRAPE ALL RELVANT DATA & IMAGES
# =========================================================


def scrape():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

 
    
# =========================================================
# SECTION TO SCRAPE: 
# LATEST MARS NEWS TITLE & DESCRIPTION PARAGRAPH
# =========================================================

    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)
    time.sleep(3)

    html = browser.html
    soup_01 = BeautifulSoup(html, 'html.parser')

    nasa_mars_news_contents = soup_01.find_all('li', class_='slide')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    nasa_mars_news_title = nasa_mars_news_contents[0].find('div', class_='content_title')
    news_title = nasa_mars_news_title.text.strip()

    nasa_mars_news_paragraph = nasa_mars_news_contents[0].find('div', class_='article_teaser_body')
    news_p = nasa_mars_news_paragraph.text.strip()


# =========================================================
# SECTION TO SCRAPE: 
# FEATURED MARS IMAGE
# =========================================================


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup_02 = BeautifulSoup(html, 'html.parser')

    base_url = 'https://www.jpl.nasa.gov'
    add_on_url = soup_02.find('a',class_='button fancybox')['data-fancybox-href']
    featured_image_url = base_url + add_on_url
       

# =========================================================
# SECTION TO SCRAPE: 
# CURRENT MARS WEATHER
# =========================================================


    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup_03 = BeautifulSoup(html, 'html.parser')

    mars_weather_tweets = soup_03.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')

    # A blank list to hold the tweets
    tweets_list = []
    # Loop through the tweets
    for tweet in mars_weather_tweets:
        # If tweet has the word Sol in it ...
            if 'sol' in (tweet.text):
                # Append the tweet to the list
                tweets_list.append(tweet.text)

    mars_weather = tweets_list[0]
        
    
# =========================================================
# SECTION TO SCRAPE: 
# TABLE WITH FACTS ABOUT MARS
# =========================================================


    url = 'https://space-facts.com/mars/'
    
    tables = pd.read_html(url)

    df_mars = tables[0]

    df_mars = df_mars.rename(columns={0:"Category", 1:"Value"})

    df_mars = df_mars.set_index("Category")

    marsfacts_html = df_mars.to_html()

    
# =========================================================
# SECTION TO SCRAPE: 
# IMAGES OF MARS HEMISPHERES
# =========================================================


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)
    time.sleep(1)
    html = browser.html

    soup_04 = BeautifulSoup(html, 'html.parser')

    mars_hemispheres = soup_04.find_all('div', class_='item')

    url_list = []
    hemisphere_title_list = []

    base_url = 'https://astrogeology.usgs.gov'

    for x in mars_hemispheres:
        url_list.append(base_url + x.find('a')['href'])
        hemisphere_title_list.append(x.find('h3').text.strip())

    reduced_hemisphere_title_list = []

    for x in hemisphere_title_list:
        y = x.split()
        reduced_hemisphere_title_list.append(y)

    for z in reduced_hemisphere_title_list:
        z.remove("Enhanced")

    final_hemisphere_title_list = []

    for z in final_hemisphere_title_list:
        del z

    for z in reduced_hemisphere_title_list:
        if len(z) == 2:
            z = z[0] + " " +z[1] 
        if len(z) == 3:
            z = z[0] + " " +z[1] + " " +z[2] 
        final_hemisphere_title_list.append(z)  

    image_url_list =[]

    for x in url_list:
        browser.visit(x)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        x = base_url+soup.find('img',class_='wide-image')['src']
        image_url_list.append(x)

    hemisphere_image_urls  =[]
    
    for i in hemisphere_image_urls:
        del i

    for x in range(len(final_hemisphere_title_list)):
        hemisphere_image_urls.append({'title':final_hemisphere_title_list[x],'img_url':image_url_list[x]})



# =========================================================
# SECTION TO ASSIGN RESULTS OF ALL SCRAPING ABOVE
# TO A DICTIONARY CALLED "marspage"
# =========================================================
    
    marspage = {}
    marspage["news_title"] = news_title
    marspage["news_p"] = news_p
    marspage["featured_image_url"] = featured_image_url
    marspage["mars_weather"] = mars_weather
    marspage["marsfacts_html"] = marsfacts_html
    marspage["hemisphere_image_urls"] = hemisphere_image_urls


    return marspage


# =========================================================
# END OF FUNCTION TO SCRAPE ALL RELVANT DATA & IMAGES
# =========================================================