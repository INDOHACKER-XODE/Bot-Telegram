import requests
from bs4 import BeautifulSoup as Bs

class twDown:
	def __init__(self,url):
		self.lnk=url
		self.req=requests.Session()
		self.req.headers.update({'referer':'http://twittervideodownloader.com','user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'})
		self.u='http://twittervideodownloader.com{}'

	def response(self):
		bs1=Bs(self.req.get(self.u.format('')).text,'html.parser')
		token=bs1.find('input',{'name':'csrfmiddlewaretoken'})
		res=self.req.post(self.u.format('/download'),data={'tweet':self.lnk,
			'csrfmiddlewaretoken':token['value']})
		bs2=Bs(res.text,'html.parser')
		linku=bs2.find('a',{'class':'expanded button small float-right'})

		return linku['href']