from bs4 import BeautifulSoup#for getting trends from mobile site because python api is quite useless
import logging
import requests


#Creates Sandy Grey, the logger
logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
logger = logging.getLogger(__name__)

def trendchaser():
	c=1#basically a counting variable, assuming the number of trends is a constant 10
	trends = []#an array for the different trends

	#Downloading and making the datareadable
	r  = requests.get("https://mobile.twitter.com/trends")#get's data from twitters trending page that the api doesn't provide
	page = r.text

	#Let's make some Beautiful Soup
	soup = BeautifulSoup(page)

	while trends < 10:
		
