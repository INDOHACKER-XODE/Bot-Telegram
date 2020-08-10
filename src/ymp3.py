import requests,re

def Ymp3(url):
	req=requests.post('https://nuubi.herokuapp.com/ytdl',
		data={'url-yt':url, 'type':'mp3'})
	rgx=re.findall(r'href="(.*)" target="_blank" download', req.text)
	if not rgx:
		return False
	else:
		print(rgx)
		return rgx[0]
