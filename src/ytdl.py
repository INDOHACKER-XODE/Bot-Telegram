import youtube_dl

class Ytdl:
	def __init__(self,url):
		self.u=url

	def response(self):
		ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
		with ydl:
			result = ydl.extract_info(
				self.u,
				download=False # We just want to extract the info
				)

		if 'entries' in result:
			video = result['entries'][0]
		else:
			video = result

		url=[]
		for vid in video['formats']:
			url.append(vid['url'])
		num=len(url)
		res=url[num-1]
		print(res)
		return res
