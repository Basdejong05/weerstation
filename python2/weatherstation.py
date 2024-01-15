from tkinter import *
import tkintermapview
from PIL import Image, ImageTk


root = Tk()
root.title("Weather Station")
root.minsize(1920, 1080)  # width, height
root.geometry("1920x1080")
root.configure(background= "#FAF9F6")
root.state('zoomed')

#vars
country = "netherlands"
name = "krimpen aan den IJssel"
temp = "19 graden"
feelsliketemp = "32 graden"
weather = "clouds"
weatherdescription = "Fck ton of clouds"
pressure = "10gb"
humidity = "10mg"
windspeed = "10mph"
winddeg = "nortwest"
rain = "10mm in last hour"
clouds = "96 clouds rn"

#tempbox | hier zit temp, feels like temp, weather, weatherdescription, pressure en humidity|
tempbox = Canvas(root, width=890, height=520,highlightthickness=1, highlightbackground="black").place(x=15, y=15)
tijdbox= Label(tempbox, width=20, height=2, text="4:11 PM", highlightthickness=1 , highlightbackground="black").place(x=35, y=35)
tempbox= Label(tempbox, width=20, height=4, text="6 graden", highlightthickness=1 , highlightbackground="black").place(x=735, y=85)
feelsliketempbox= Label(tempbox, width=20, height=4, text="Feels like 8 graden", highlightthickness=1 , highlightbackground="black").place(x=735, y=185)
humiditybox= Label(tempbox, width=20, height=4, text="Humidity: 10mg", highlightthickness=1 , highlightbackground="black").place(x=735, y=285)
pressurebox= Label(tempbox, width=20, height=4, text="Air Pressure: 10gb", highlightthickness=1 , highlightbackground="black").place(x=735, y=385)
weatherdescriptionbox = Label(tempbox, width=20, height=4, text="Sunny", highlightthickness=1 , highlightbackground="black").place(x=385, y=385)
mainimg = Image.open('113.png')
mainimage = mainimg.resize((200 , 200))
mainimagefull = ImageTk.PhotoImage(mainimage)
mainimgscherm = Label(tempbox, image=mainimagefull, width=300, height=300 ).place(x=315, y=50)



#windbox
windbox = Canvas(root, width=280, height=220,highlightthickness=1, highlightbackground="black").place(x=15, y=560)
windrichting = Label(windbox, width=30, height=1, text="South-west", highlightthickness=1 , highlightbackground="black").place(x=45, y=700)
tekstsnelheid = Label(windbox, width=30, height=1, text="12mph", highlightthickness=1 , highlightbackground="black").place(x=45, y=730)
windimg = Image.open('wind.png')
windimage = windimg.resize((100 , 100))
windimagefull = ImageTk.PhotoImage(windimage)
windimgscherm = Label(windbox, image=windimagefull, width=70, ).place(x=120, y=590)


#regenbox
regenbox = Canvas(root, width=280, height=220,highlightthickness=1, highlightbackground="black").place(x=320, y=560)
regentekst = Label(regenbox, width=30, height=1, text="10 mm in last hour", highlightthickness=1 , highlightbackground="black").place(x=350, y=700)
regenimg = Image.open('308.png')
regenimage = regenimg.resize((100,100))
regenfullimage = ImageTk.PhotoImage(regenimage)
regenimgscherm = Label(regenbox, image=regenfullimage, width=70,).place(x=420 , y=590)


#cloudsbox
cloudsbox = Canvas(root, width=280, height=220,highlightthickness=1, highlightbackground="black").place(x=625, y=560)
cloudstotal = Label(cloudsbox, width=30, height=1, text="96 clouds", highlightthickness=1 , highlightbackground="black").place(x=655, y=700)
cloudimg = Image.open('122.png')
cloudsimage = cloudimg.resize((100,100))
cloudfullimage = ImageTk.PhotoImage(cloudsimage)
cloudimgscherm = Label(cloudsbox, image=cloudfullimage ,width=70).place(x=720, y=590)



#minimap 
map_widget = tkintermapview.TkinterMapView(root, width=565, height=720,highlightthickness=1, highlightbackground="black", corner_radius=0)

#plaats
plaatsbox = Canvas(root, width=565, height=30,highlightthickness=1, highlightbackground="black").place(x=935, y=750)
tekstplaats = Label(plaatsbox, width=50, height=1, text="Netherlands, Zuid-Holland, Krimpen aan den IJssel").place(x=1050, y=755)



map_widget.set_position(51.9167, 4.6028)
map_widget.set_zoom(8)
map_widget.place(x=935, y=15)
marker_2 = map_widget.set_marker(51.9167, 4.6028, text="krimpen aan den ijsel")

root.mainloop()