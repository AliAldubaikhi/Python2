import urllib.request
import json
from urllib.error import  URLError
import re

def decode_results(data):
        print("======= Results =========")
        if ( data['cod']== '404'):
                print(data['message'])
                return
        print("Humidity ",data['main']['humidity'])
        print("Temp ",data['main']['temp'])
        print("Temp Max ",data['main']['temp_max'])
        print("Temp Min ",data['main']['temp_min'])
        print("Pressure ",data['main']['pressure'])
        print("Wind speed ",data['wind']['speed'])
        print("Wind from  ",data['wind']['deg'])
        print("Sky ",data['weather'][0]['main'])
        print("Description ",data['weather'][0]['description'])
        print("Sunrise ",data['sys']['sunrise'])
        print("Country ",data['sys']['country'])
        

def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)
			data = json.loads(content_string)
			decode_results(data)
			
			
			if result:
				title = result.group("title")
				print(title)

			result = regexp_keywords.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				print(keywords)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")
		
print("Enter city ")
city = input()

crawler_backlog = {}

seed = "http://api.openweathermap.org/data/2.5/weather?q="+city

crawler_backlog[seed]=0

visit_url(seed, "www.openweathermap.org")
