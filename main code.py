#first window
#welcome class is my first window with "welcome to China" and the button with text and a picture of panda,
# funtion secondmap in calss welcome() is to destory the first windwow and create a new window, which is the map window-main window.

#second window
#map calss is the main window, which contains a text" Travel to China" and a Chinese map. There is also a menu bar on the top, named"Find".
                #When you click there, if will have "Weather" and ¡±hotels" to choose for search.
#function coor is to detect the mouse click, which will detect the mouse lick on x,y on the image, and if x, y on the certain region that I made, it will come out a image of the city you click.
#funtion of Shanghai, Beijng,Haerbin,Hangzhou, Shenzhen,Yuannan,Tibet, Xinjiang, Chengdu, is to make a third window and which will be link with the next calss info calss.
#function weather is to make a new window and it will be relate with "Weaterh Class"
#funtion hotel is to make a new window that you can search the hotels dependon which city you type in.

#Third window
#the class info defines the form of city information. which has a city picture, a menubar and the desctription of the city,which will be read from a text file.
#the def food, is to make a new window, based on city info, which is related with food class.
#The class of food window, contains a text as the titile from the city, a pciture of the local food, as well as the a desctription of the food which is read from the the other text files.

#Back the the map window, on the find menu, there is a search weathr and search food.
#the weather class, i import a file which called IMPORT, this file is i wrote, I find a webste called openweather map, they have own API,but i cnanot use it, as it does not give you funtions.
#Instead it return s a lsit of dictionaries. Threrefore, I have to use request, I learn it how to read from the wesite. it return with the unicode. I write to soem codes to convert unicode to ASCII
#Then Tkinter still do not support unicode. Then I write a funtion on IMPORT file and to improt the weather file, then on my main code, it is working now.
#so on the weather windwo, there is an entry box, you can just type the city, it will use the funtion I wrote on the IMPROT file,
#to reutrn the weahter desctription, temperature, pressure and other information.

#the funtion cityweather, is to sepreate the code i wrote on the IMPORT file and insert to the message box. and it will be updated, when you click the search box.

#for the hotel class ,I find an API on Tripadvisor, it will return the a number of hotels' information with price , adress and other information,as a list of dictionaries.
#However, I only need the name of the hotels, so i write my own codes to return the name of the hotels.
#On this class, I contain a entry box, a search button as well as a list box which contains the name of the hotels.

#the function trip is to import the funtion that from the API file and insert to the list box that made on the hotel class.



from Tkinter import*
from PIL import Image, ImageTk
from IMPORT import cityweather
from API import getHotels

#first window with welcome pic and the button, which drivce into the second window.
class welcome():
    def __init__(self,root):
        #create canvas
        self.c=Canvas(root,width=860,height=250,bg="old lace" )#"misty rose"
        self.c.pack(expand=YES, fill=BOTH)
        #insert the welcome TO chINA image.
        self.image=Image.open("p2.gif")
        self.photo=ImageTk.PhotoImage(self.image)
        self.c.create_image(0,0,image=self.photo,anchor=NW)
        #insert the image
        self.photo2=PhotoImage(file="panda.gif")
        #combine image and text on the same button
        self.b=Button(self.c,text="click here",fg="#FFCC99",bg="#99CC99",font="Times 35 italic bold",image=self.photo2,
                      compound="left",relief=RAISED,command=self.secondmap) 
        self.button=self.c.create_window(300,130,anchor=NW,window=self.b)
        
        
#to destory the first windwow and create a new window, which is the map window-main window.
    def secondmap(self):
        root.destroy()
        master=Tk()
        master.geometry("900x800")
        master.title("Chinese Map")
        
        app=map(master)
        master.mainloop()
        


class map():
    
    def __init__(self,master):
    #Here is to make the menu bar   
        self.menubar=Menu(master)
        master.config(menu=self.menubar)
        find=Menu(self.menubar, tearoff=0)
        find.add_command(label="Weather",command=self.weather)
        find.add_command(label="Hotel",command=self.hotel)
        self.menubar.add_cascade(label="Find",menu=find)
   #make the cavas and text     
        self.c=Canvas(master,width=900,height=800,bg="linen")
    #insert chinese map
        self.photo=ImageTk.PhotoImage(file="chinamap.gif")
        self.c.create_image(430,420,image=self.photo)
    #insert text
        self.c.create_text(150,10,anchor=NW,fill="darkblue",font="Times 70 italic bold",
                           text="Travel to China")
        self.c.pack(expand=YES, fill=BOTH)
        
    #Here is te detected click on the image of map
        self.c.bind("<Button-1>",self.coor)
        
          

#I have use this code to find the coordinates of on the each city's region on the map
   # def coor(self,a):
    #    print a.x,a.y


#function coor is to detect the mouse click, which will detect the mouse lick on x,y on the image, and if x, y on the certain region that I made, it will come out a image of the city you click.
    def coor(self,a):
        #Shnaghai
        if 636<= a.x <=668 and 456 <= a.y <=471:
            self.shanghai1=PhotoImage(file="shanghai1.gif")
            self.shab=Button(self.c,image=self.shanghai1,width=120, height=120, command=self.Shanghai)
            self.shab.place(x=750,y=385,anchor=NW)
                
        #Beijing
        if 554 <= a.x <=585 and 350 <= a.y <=370:
            self.beijing1=PhotoImage(file="beijing1.gif")
            self.bjb=Button(self.c,image=self.beijing1,width=120, height=120,command=self.Beijing)
            self.bjb.place(x=750,y=260,anchor=NW)

        #Hangzhou
        if 624 <= a.x <=670 and 477 <= a.y <=516:
            self.hangzhou1=PhotoImage(file="hangzhou1.gif")
            self.hzb=Button(self.c,image=self.hangzhou1,width=120, height=120,command=self.Hangzhou)
            self.hzb.place(x=750,y=515,anchor=NW)

        #Shenzhen
        if 538 <= a.x <=601 and 564 <= a.y <=601:
            self.shenzhen1=PhotoImage(file="shenzhen1.gif")
            self.szb=Button(self.c,image=self.shenzhen1,width=120, height=120,command=self.Shenzhen)
            self.szb.place(x=560,y=630,anchor=NW)

        #Chengdu
        if 385 <= a.x <=468 and 463 <= a.y <=513:
            self.chengdu1=PhotoImage(file="chengdu1.gif")
            self.hzb=Button(self.c,image=self.chengdu1,width=120, height=120,command=self.Chengdu)
            self.hzb.place(x=350,y=630,anchor=NW)

        #Yunnan
        if 378<= a.x <=447 and 527 <= a.y <=597:
            self.yunnan1=PhotoImage(file="yunnan1.gif")
            self.yunnanb=Button(self.c,image=self.yunnan1,width=120, height=120,command=self.Yunnan)
            self.yunnanb.place(x=180,y=600,anchor=NW)

        #Haerbin
        if 646 <= a.x <=724 and 211 <= a.y <=287 :
            self.haerbin1=PhotoImage(file="harbin1.gif")
            self.haerbinb=Button(self.c,image=self.haerbin1,width=120, height=120,command=self.Haerbin)
            self.haerbinb.place(x=750,y=130,anchor=NW)

        #Tibet
        if 178 <= a.x <=325 and 432 <= a.y <=512:
            self.tibet1=PhotoImage(file="tibet1.gif")
            self.tibetb=Button(self.c,image=self.tibet1,width=120, height=120,command=self.Tibet)
            self.tibetb.place(x=20,y=470,anchor=NW)

        #Xinjiang
        if 176 <= a.x <=279 and 279 <= a.y <=369:
            self.xinjiang1=PhotoImage(file="xinjiang1.gif")
            self.xinjiangb=Button(self.c,image=self.xinjiang1,width=120, height=120, command=self.Xinjiang)
            self.xinjiangb.place(x=20,y=185,anchor=NW)
        

   ############funciton that make a third window and which will be link with the next calss info calss.
    def Shanghai(self):
        shanghai=Toplevel()
        shanghai.title("Shanghai")
        shanghaiinfo=info(shanghai,"Shanghai","shanghai2.gif","shanghai.txt","shanghaifood1.gif","shanghai2.txt")
    
    def Beijing(self):
        beijing=Toplevel()
        beijinginfo=info(beijing,"Beijing","beijing2.gif","beijing.txt","beijingfood1.gif","beijing2.txt")

    def Hangzhou(self):
        hangzhou=Toplevel()
        hangzhouinfo=info(hangzhou,"Hangzhou","hangzhou2.gif","hangzhou.txt","hangzhoufood1.gif","hangzhou2.txt")
        
    def Shenzhen(self):
        shenzhen=Toplevel()
        shenzheninfo=info(shenzhen,"Shenzhen","shenzhen2.gif","shenzhen.txt","shenzhenfood1.gif","shenzhen2.txt")

    def Chengdu(self):
        chengdu=Toplevel()
        chengduinfo=info(chengdu,"Chengdu","chengdu2.gif","chengdu.txt","chengdufood1.gif","chengdu2.txt")

    def Yunnan(self):
        yunnan=Toplevel()
        yunnaninfo=info(yunnan,"Yunnan","yunnan2.gif","yunan.txt","yunnanfood1.gif","yunnan2.txt")

    def Haerbin(self):
        haerbin=Toplevel()
        haerbininfo=info(haerbin,"Harbin","harbin2.gif","haerbin.txt","harbinfood1.gif","harbin2.txt")

    def Tibet(self):
        tibet=Toplevel()
        tibetinfo=info(tibet,"Lasa","lasa2.gif","tibet.txt","lasafood1.gif","lasa2.txt")
        
    def Xinjiang(self):
        xinjiang=Toplevel()
        xinjianginfo=info(xinjiang,"Xinjiang","xinjiang2.gif","xinjiang.txt","xinjiangfood1.gif","xinjiang2.txt")

#####  it is the fuction to make a new window for weather 
    def weather(self):
        searchweather=Toplevel()
        weatherwindow=weather(searchweather)

#####  it is the fuction to make a new window for hotels        
    def hotel(self):
        searchhotel=Toplevel()
        hotelwindow=hotel(searchhotel)


#the third window has a city picture, a menubar and the desctription of the city,which will be read from a text file.
class info():
    def __init__(self, base,city,pic1,txt,foodpic,txt2):
        self.city=city
        
        #name title
        base.title(self.city)
        base.geometry("700x640")
        self.c=Canvas(base,width=700,height=700,bg="alice blue")

        #make the munu bar
        self.menubar=Menu(base)
        base.config(menu=self.menubar)
        find=Menu(self.menubar, tearoff=0)
        find.add_command(label="food",command=lambda: self.foodintro(self.city,foodpic,txt2))
        self.menubar.add_cascade(label="menu",menu=find)

        #insert the picture
        self.photo1=PhotoImage(file=pic1)
        self.c.create_image(85,120,anchor=NW,image=self.photo1)
        self.c.create_text(350,50,fill="darkblue",font="Times 70 italic bold",
                           text=city)

        #read the text file
        self.f=open(txt)
        self.line=self.f.read()
        self.c.create_text(350,520,font="Times 15 italic ",text=self.line)
        self.c.pack(expand=YES, fill=BOTH)
        
        base.mainloop()

#click the menu bar to create another window
    def foodintro(self,city,foodpic,txt2):
        foodwin=Toplevel()
        food1=food(foodwin,city,foodpic,txt2)
        
#####The class of food window, contains a text as the titile from the city, a pciture of the local food, as well as the a desctription of the food which is read from the the other text files.
        
class food():
    def __init__(self, base,city,foodpic,txt2):#pic1,txt):
        base.title(city)
        base.geometry("700x640")
        self.c=Canvas(base,width=700,height=700,bg="MistyRose2")

        self.photo1=PhotoImage(file=foodpic)
        self.c.create_image(85,120,anchor=NW,image=self.photo1)
        self.c.create_text(350,50,fill="darkblue",font="Times 70 italic bold",
                           text=city)
        self.f=open(txt2)
        self.line=self.f.read()
        self.c.create_text(350,520,font="Times 15 italic ",text=self.line)
 
        self.c.pack(expand=YES, fill=BOTH)
        
        base.mainloop()

        
############### I import a file which called IMPORT, this file is i wrote, I find a webste called openweather map, they have own API,
        ########but i cnanot use it, as it does not give you funtions.
#Instead it return s a lsit of dictionaries. Threrefore, I have to use request, I learn it how to read from the wesite. it return with the unicode.
        #########I write to soem codes to convert unicode to ASCII
#Then Tkinter still do not support unicode. Then I write a funtion on IMPORT file and to improt the weather file, then on my main code, it is working now.
#so on the weather window, there is an entry box, you can just type the city, it will use the funtion I wrote on the IMPROT file,
#to reutrn the weahter desctription, temperature, pressure and other information.       
class weather():
    def __init__(self,main):
        main.title("Search Weather")

        #make a canvas 
        self.c=Canvas(main,width=600,height=600,bg="sky blue")
        self.c.pack(expand=YES, fill=BOTH)
        #create text on the canvas
        self.c.create_text(93,30,anchor=NW, fill="black",font="Times 45 italic bold",text="Search Weather")
        self.c.pack(expand=YES, fill=BOTH)

        #main search box
        self.c.create_text(170,135,anchor=NW, fill="black",font="Times 18 italic bold",text="Please enter a city name:")
        self.searchbox=Text(self.c,width=21,height=1,bg="white",font="10")
        self.c.create_window(170,170,anchor=NW,window=self.searchbox)
        self.b=Button(self.c,text="Search",command=self.cityweather)
        self.button=self.c.create_window(398,175,anchor=NW,window=self.b)

##        #cityname
##        self.c.create_text(85,240,anchor=NW, fill="black",font="Times 12 italic bold",text="City name:")
##        self.citybox=Text(self.c,width=20,height=2,bg="white")
##        self.c.create_window(85,260,anchor=NW,window=self.citybox)

        #weather description
        self.c.create_text(70,240,anchor=NW, fill="black",font="Times 14 italic bold",text="Weather description:")
        self.desbox=Text(self.c,width=18,height=1,bg="white",font="8")
        self.c.create_window(70,260,anchor=NW,window=self.desbox)

        #temp
        self.c.create_text(340,240,anchor=NW, fill="black",font="Times 14 italic bold",text="Temperature:")
        self.tempbox=Text(self.c,width=18,height=1,bg="white",font="8")
        self.c.create_window(340,260,anchor=NW,window=self.tempbox)

        #pressure
        self.c.create_text(70,330,anchor=NW, fill="black",font="Times 14 italic bold",text="Pressure:")
        self.prebox=Text(self.c,width=18,height=1,bg="white",font="8")
        self.c.create_window(70,350,anchor=NW,window=self.prebox)

        #humidity
        self.c.create_text(340,330,anchor=NW, fill="black",font="Times 14 italic bold",text="Humidity:")
        self.humbox=Text(self.c,width=18,height=1,bg="white",font="8")
        self.c.create_window(340,350,anchor=NW,window=self.humbox)
        
        #temp_min
        self.c.create_text(70,430,anchor=NW, fill="black",font="Times 14 italic bold",text="Mini Temperature:")
        self.minbox=Text(self.c,width=18,height=1,bg="white",font="8")
        self.c.create_window(70,450,anchor=NW,window=self.minbox)
        
        #temp_max
        self.c.create_text(340,430,anchor=NW, fill="black",font="Times 14 italic bold",text="Max Temperature:")
        self.maxbox=Text(self.c,width=18,height=1,bg="white",font="8")
        self.c.create_window(340,450,anchor=NW,window=self.maxbox)
        
        main.mainloop()


############to sepreate the code i wrote on the IMPORT file and insert to the message box.
        ###and it will be updated, when you click the search box.     
    def cityweather(self):
        
    ######## before you type, delte the info in messages boxes
        self.desbox.delete("1.0",END)
        self.tempbox.delete("1.0",END)
        self.prebox.delete("1.0",END)
        self.humbox.delete("1.0",END)
        self.minbox.delete("1.0",END)
        self.maxbox.delete("1.0",END)
        self.cityname=self.searchbox.get("1.0","end-1c")
        self.cityweather=cityweather(self.cityname)
      #  self.citybox.insert(END,self.cityname)
      
    ###### insert the message form the IMPORT file
        self.desbox.insert(END,self.cityweather[0])
        self.tempbox.insert(END,self.cityweather[1])
        self.prebox.insert(END,self.cityweather[2])
        self.humbox.insert(END,self.cityweather[3])
        self.minbox.insert(END,self.cityweather[4])
        self.maxbox.insert(END,self.cityweather[5])
    # delete the key words on the box
        self.searchbox.delete("1.0",END)

        

##########I find an API on Tripadvisor, it will return the a number of hotels' information with price , adress and other information,as a list of dictionaries.
#However, I only need the name of the hotels, so i write my own codes to return the name of the hotels.
#On this class, I contain a entry box, a search button as well as a list box which contains the name of the hotels.
class hotel():
    def __init__(self,main):
        main.title("Search for Hotels")
        
    ###create canvas
        self.c=Canvas(main,width=600,height=600,bg="papaya whip")
        self.c.pack(expand=YES, fill=BOTH)
        self.c.create_text(93,30,anchor=NW, fill="black",font="Times 45 italic bold",text="Search for Hotels")
        self.c.pack(expand=YES, fill=BOTH)
        self.c.create_text(173,140,anchor=NW, fill="black",font="Times 18 italic bold",text="Please enter a city name:")
        self.searchbox=Text(self.c,width=21,height=1,bg="white",font="8")
        self.c.create_window(172,175,anchor=NW,window=self.searchbox)
        self.b=Button(self.c,text="Search",command=self.trip)
        self.button=self.c.create_window(398,175,anchor=NW,window=self.b)

    # create list boxes
        self.l1=Listbox(self.c,width=44,height=14,font="3")     
        self.c.create_window(80,230,anchor=NW,window=self.l1)
        main.mainloop()

        
    #####to import the funtion that from the API file and insert to the list box that made on the hotel class.    
    def trip(self):
        self.l1.delete(0,END)
        self.cityname=self.searchbox.get("1.0","end-1c")
        hotels=getHotels(self.cityname)
        if hotels:
            for i in hotels:
                self.l1.insert(END,"* "+i)
        else:
            a="Sorry, I can not find it.\n Please enter another city."
            self.l1.insert(END, a)
            
        self.searchbox.delete("1.0",END)

        
root=Tk()
#root.geometry=("861x121")
root.title("Welcome")
fp=welcome(root)
root.mainloop()
