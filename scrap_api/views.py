from bs4 import BeautifulSoup
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def reddit_scrap(request):
    headers = {'User-Agent': 'Mozilla/5.0'}
    red_url = "https://www.reddit.com/r/popular/"
    red_page = requests.get(red_url, headers=headers)
    soup = BeautifulSoup(red_page.text, 'html.parser')
    a_tag = soup.find_all('a', class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    json = []
    for x in a_tag:
        base_reddit_url = 'www.reddit.com'
        trending_topic = {"link": base_reddit_url + x['href'], "title": x.string}
        json.append(trending_topic)
    return Response(json, status=status.HTTP_200_OK)
    