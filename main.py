import requests
import json

rurl = input("Enter url for shortening :\n")
url = f'https://api.shrtco.de/v2/shorten?url={rurl}'

response = requests.get(url)
content = json.loads(response.text)

if(content['ok'] == True):
	short = content['result']['short_link']
	
	printable = f'''
			Shortened Url --> https://{short}
	'''
	print(printable)
	with open("shortened_url.txt","w") as file:
		file.write(short)
		file.close()
elif(content['error_code'] == 1):
	print('Url Not Found')

else:
	print('Try Again')
