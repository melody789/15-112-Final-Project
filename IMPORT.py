#since unicode from weather.py cannot directly import to TKinter,
#I wirte a functiona , which will return a list
#then use this file to my main code.


from weather import weather

def cityweather(city):
    a=weather(city)
    return a

#print cityweather("shanghai")


