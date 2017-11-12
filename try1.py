from Tkinter import*
from PIL import Image, ImageTk

class info():
    def __init__(self, base,city,pic1):
        base.title(city)
        base.geometry("700x640")
        self.c=Canvas(base,width=700,height=700,bg="pink")
        self.photo1=PhotoImage(file="bg1.gif")
        self.c.create_image(0,0,anchor=NW,image=self.photo1)
        self.photo2=PhotoImage(file="beijing1.gif")
        self.c.create_image(70,70,anchor=NW,image=self.photo2)
        self.c.create_text(350,50,fill="darkblue",font="Times 70 italic bold",
                           text="Shang Hai")
        self.f=open("shanghai.txt")
        self.line=self.f.read()
        self.c.create_text(40,400,anchor=NW,fill="darkblue",font="Times 8 italic bold",
                           text=self.line)
 #       self.c.create_text(20,400,anchor=NW,font="Times 20",text= "shanghai,is a renowned international metropolis drawing more and more attention\n from all over the world.\n Situated on the estuary of Yangtze River, it serves as the most influential economic, \n financial, international trade, and cultural center in East China.\n Also it is a popular travel destination\n for visitors to sense the pulsating development of the country.")
        self.c.pack()

base=Tk()
app=info(base,"shanghai","shanghai1.gif")
base.mainloop()

