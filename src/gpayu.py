import requests,os,sys
from bs4 import BeautifulSoup as Bs

def Gratis(num,msg):
	req=requests.Session()
	req.headers.update({'Referer':'http://sms.payuterus.biz/alpha',
		'user-agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36',
		'Connection':'keep-alive',
		'Pragma':'no-cache',
		'Cache-Control':'no-cache',
		'Origin':'http://sms.payuterus.biz',
		'Upgrade-Insecure-Requests':'1',
		'Content-Type':'application/x-www-form-urlencoded',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie':'_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1',
		})

	capt=req.get('http://alpha.payuterus.biz/').text
	bs1=Bs(capt,'html.parser')
	cap=(bs1.find('span',{'id':None}).text).split(' ')

	hasilcapt=int(cap[0]) + int(cap[2])
	key=bs1.find('input',{'name':'key'})['value']

	dataq={'nohp':num,
	'pesan':msg,
	'captcha':hasilcapt,
	'key':key,
	}
	res=req.post('http://alpha.payuterus.biz/send.php',data=dataq).text

#	print(res)
	return str(res)

#print(Gratis('082160419103', 'kslskdjsjajksjdjdjsshshdjjdjsjsjsjsj'))
