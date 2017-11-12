from Tkinter import*
from PIL import Image, ImageTk

#first window with welcome pic and the button, which drivce into the second window.
class welcome():
    def __init__(self,root):
        self.image=Image.open("p2.gif")
        self.photo=ImageTk.PhotoImage(self.image)
        self.wb=Button(root,image=self.photo,command=self.secondmap)
        self.wb.pack()
#		self.label=Label(root, image=self.photo)
#		self.label.pack()
    def secondmap(self):
        root.destroy()
        master=Tk()
        master.geometry("900x800")
        master.title("Chinese Map")
        #master.configure(bg="pink")
        master=map(master)
        master.mainloop()
        


class map():

    
    def __init__(self,master):
            
        #self.frame=Frame(master, width=1500,height=1500, bg="pink")
        #self.frame.pack()
        self.c=Canvas(master,width=900,height=800,bg="white")
        self.image=Image.open("map2.png")
        #self.image.resize( (100,100))
        self.photo=ImageTk.PhotoImage(self.image)
        self.c.create_image(400,370,image=self.photo)
        self.c.pack()
        #self.photo=self.photo.subsample(2,2)
        #self.label=Label(master, image=self.photo)
        #self.label.pack()

        #Shnaghai
        self.shanghai1=PhotoImage(file="shanghai1.gif")
        #self.sanghai1=self.shanghai1.subsample(50,50)
        #self.label2=Label(self.c,image=self.shanghai1)
        #self.label2.pack()
        self.shab=Button(self.c,image=self.shanghai1,width=80, height=80, command=self.Shanghai)
        self.shab.place(x=750,y=300,anchor=CENTER)
        #self.shab.configure(
        
        #Beijing 
        self.beijing1=PhotoImage(file="beijing1.gif")
        self.bjb=Button(self.c,image=self.beijing1,width=80, height=80,command=self.Beijing)
        self.bjb.place(x=750,y=200,anchor=NW)

        #Hangzhou
        self.hangzhou1=PhotoImage(file="hangzhou1.gif")
        self.hzb=Button(self.c,image=self.hangzhou1,width=80, height=80,command=self.Hangzhou)
        self.hzb.place(x=750,y=400,anchor=NW)

        #Shenzhen
        self.shenzhen1=PhotoImage(file="shenzhen1.gif")
        self.szb=Button(self.c,image=self.shenzhen1,width=80, height=80,command=self.Shenzhen)
        self.szb.place(x=550,y=600,anchor=NW)

        #Chengdu
        self.chengdu1=PhotoImage(file="chengdu1.gif")
        self.hzb=Button(self.c,image=self.chengdu1,width=80, height=80,command=self.Chengdu)
        self.hzb.place(x=350,y=600,anchor=NW)

        #Yunnan
        self.yunnan1=PhotoImage(file="yunnan1.gif")
        self.yunnanb=Button(self.c,image=self.yunnan1,width=80, height=80,command=self.Yunnan)
        self.yunnanb.place(x=250,y=550,anchor=NW)

        #Haerbin
        self.haerbin1=PhotoImage(file="haerbin1.gif")
        self.haerbinb=Button(self.c,image=self.haerbin1,width=80, height=80,command=self.Haerbin)
        self.haerbinb.place(x=650,y=100,anchor=NW)

        #Tibet
        self.tibet1=PhotoImage(file="tibet1.gif")
        self.tibetb=Button(self.c,image=self.tibet1,width=80, height=80,command=self.Tibet)
        self.tibetb.place(x=150,y=400,anchor=NW)

        #Xinjiang
        self.xinjiang1=PhotoImage(file="xinjiang1.gif")
        self.xinjiangb=Button(self.c,image=self.xinjiang1,width=80, height=80, command=self.Xinjiang)
        self.xinjiangb.place(x=100,y=220,anchor=NW)
        

        #funciton
    def Shanghai(self):
        shanghai=Toplevel()
    #    shanghai.geometry("600x600")
        shanghai.title("Shanghai")
        shanghaiinfo=info(shanghai,"Shanghai","shanghai1.gif","shanghai.txt")
    
    def Beijing(self):
        beijing=Toplevel()
        beijinginfo=info(beijing,"Beijing","beijing1.gif","beijing.txt")

    def Hangzhou(self):
        hangzhou=Toplevel()
        hangzhouinfo=info(hangzhou,"Hangzhou","hangzhou1.gif","hangzhou.txt")
        
    def Shenzhen(self):
        shenzhen=Toplevel()
        shenzheninfo=info(shenzhen,"Shenzhen","shenzhen1.gif","shenzhen.txt")

    def Chengdu(self):
        chengdu=Toplevel()
        chengduinfo=info(chengdu,"Chengdu","chengdu1.gif","chengdu.txt")

    def Yunnan(self):
        yunnan=Toplevel()
        yunnaninfo=info(yunnan,"Yunnan","yunnan1.gif","yunan.txt")

    def Haerbin(self):
        haerbin=Toplevel()
        haerbininfo=info(haerbin,"Haerbin","haerbin1.gif","haerbin.txt")

    def Tibet(self):
        tibet=Toplevel()
        tibetinfo=info(tibet,"Tibet","tibet1.gif","tibet.txt")
        
    def Xinjiang(self):
        xinjiang=Toplevel()
        xinjianginfo=info(xinjiang,"Xinjiang","xinjiang1.gif","xinjiang.txt")

class info():
    def __init__(self, base,city,pic1,txt):
        base.title(city)
        base.geometry("700x640")
        self.c=Canvas(base,width=700,height=700,bg="lightblue")
        #self.photobg=PhotoImage(file="bg1.gif")
        #self.c.create_image(0,0,anchor=NW,image=self.photobg)
        self.photo1=PhotoImage(file=pic1)
        self.c.create_image(80,120,anchor=NW,image=self.photo1)
        self.c.create_text(350,50,fill="darkblue",font="Times 70 italic bold",
                           text=city)
        self.f=open(txt)
        self.line=self.f.read()
        self.c.create_text(360,520,font="Times 15 italic ",text=self.line)
        self.box1=Entry(self.c,width=10)
        self.c.create_window(600,300,anchor=NW,window=self.box1)
        self.b=Button(self.c,text="Search")
        self.button=self.c.create_window(600,320,anchor=NW,window=self.b)
        self.c.pack(fill=BOTH)
        
        base.mainloop()
        

root=Tk()
root.title("Welcome")
fp=welcome(root)
root.mainloop()
