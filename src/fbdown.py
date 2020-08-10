import requests,re,urllib

def Fbdl(link):
	url=link.replace('https://www.','https://mbasic.').replace('https://m.','https://mbasic.')
	req=requests.get(url)
	ree=re.findall(r'<a href="(.*?)"',req.text)
	for x in ree:
		if "/video_redirect/?src=" in x:
			dl=x.replace("/video_redirect/?src=","")
			hasil=urllib.parse.unquote(dl)
			return hasil