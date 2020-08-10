import requests, random, os, sys

class Croper:
	def __init__(self,key):
		self.head={'X-Api-Key': key}

	def cropbg(self, imgfile, bg_color=None):
		req=requests.post('https://api.remove.bg/v1.0/removebg',
			files={'image_file': open(imgfile, 'rb')},
			data={'size': 'auto', 'bg_color':bg_color},
			headers=self.head,
			)

		if req.status_code == requests.codes.ok:
			with open('hasil-rmbg.png', 'wb') as out:
				out.write(req.content)
		else:
			return f"Error: {response.status_code} {response.text}"

	def cropbgurl(self, imgurl, bg_color=None):
		req=requests.post('https://api.remove.bg/v1.0/removebg',
			data={'image_url':imgurl, 'size': 'auto', 'bg_color':bg_color},
			headers=self.head,
			)

		if req.status_code == requests.codes.ok:
			with open('hasil-rmbg.png', 'wb') as out:
				out.write(req.content)
		else:
			return f"Error: {response.status_code} {response.text}"
