#### Based on the openweathermap's API, I Write my own code here
#### this return with unicode, but I have convereted to the ASCII
### However, it cannot be used directly on the Tkinter,
### So I write another file, called "IMPORT".

import requests
def weather(city):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = city
    url = api_address + city
    json_data = requests.get(url).json()
    r1 = json_data['weather']
    r2 = json_data['main']
    r1=r1[0]
    des=r1.get("description")
    description= des.encode("ascii", "None")

    return [description,str(r2.get("temp"))+" K",str(r2.get("pressure"))+" hpa",str(r2.get("humidity"))+"%",str(r2.get("temp_min"))+" K",str(r2.get("temp_max"))+" K"]
 #   print r1.get("main")
  #  print r1.get("description")
    #print r2.get("temp")
    #print r2.get("pressure")
    #print r2.get("humidity")
    #print r2.get("temp_min")
    #print r2.get("temp_max")
    
#print weather("shanghai")

