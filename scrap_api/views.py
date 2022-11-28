from bs4 import BeautifulSoup
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from selenium.webdriver.firefox.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@api_view(['GET'])
def reddit_scrap(request):
    headers = {'User-Agent': 'Mozilla/5.0'}
    red_url = "https://www.reddit.com/r/popular/"
    red_page = requests.get(red_url, headers=headers)
    soup = BeautifulSoup(red_page.text, 'html.parser')
    a_tag = soup.find_all('a', class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    json = []
    for x in a_tag:
        base_reddit_url = 'https://www.reddit.com'
        trending_topic = {"link": base_reddit_url + x['href'], "title": x.string}
        json.append(trending_topic)
    return Response(json, status=status.HTTP_200_OK)


@api_view(['GET'])
def twitter_scrap(request):
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(service=Service('./geckodriver'), options=opts)
    twitter_url = "https://twitter.com/explore/tabs/trending"
    driver.get(twitter_url)
    json = []
    try:
        main_div = WebDriverWait(driver , 15).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='trend']"))
        )
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        soup = BeautifulSoup(driver.page_source, 'lxml')
        driver.quit()
        trending_topics = soup.find_all('div', class_="css-901oao r-1nao33i r-37j5jr r-a023e6 r-b88u0q r-rjixqe r-1bymd8e r-bcqeeo r-qvutc0")
        for x in trending_topics:
            titles = x.find("span", recursive=False)
            link = titles.text[1:] if titles.text.startswith('#') else titles.text
            obj = {"title": titles.text, "link": f"https://twitter.com/search?q={link}&src=trend_click&vertical=trends"}
            json.append(obj)
    except:
        driver.quit()
    driver.quit()
    return Response(json, status=status.HTTP_200_OK)