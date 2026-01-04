import requests

url = "https://www.onlinekhabar.com/smtm/home/fear-and-greed"

r = requests.get(url=url)
if r.status_code == 200:
    
   data = r.json()['response']
   print(type(data))
   final_data = data
   for i in final_data:
    print(i['status'], i['message'])
   

