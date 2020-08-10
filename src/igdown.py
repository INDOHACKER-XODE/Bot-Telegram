from bs4 import BeautifulSoup as BS
import requests,re

class Igdl:
	def __init__(self,url):
		self.link=url

	def response(self):
		reg=requests.get(self.link)
		bs1=BS(reg.text,'html.parser')
		for i in bs1.find_all('meta'):
		    if i.get('property') == 'og:video:secure_url':
		        return i.get('content')