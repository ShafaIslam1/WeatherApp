from tkinter import*
from PIL import ImageTk,Image
import w
import requests
class MyWeather:
    def __init__(self,root):
       self.root=root
       self.root.title("MY WEATHER APPLICATION")
       self.root.geometry("350x400+450+100")
       self.root.config(bg="white")
       self.var_search=StringVar()
       self.search_icon=Image.open("C:\\Users\\ASUS\\Downloads\\search3.png")
       self.search_icon=self.search_icon.resize((30,26),Image.ANTIALIAS)
       self.search_icon=ImageTk.PhotoImage(self.search_icon)

       title=Label(self.root,text="Weather App",font=("times new roman",30,"bold"),bg="steel blue",fg="white",padx=5).place(x=0,y=0,
                                                                                            relwidth=1,height=60)
       lbl_city=Label(self.root,text="City Name",font=("times new roman",15,"bold"),bg="#033958",fg="white",anchor="w",padx=5).place(x=0,y=60,
                                                                                            relwidth=1,height=50)
       lbl_city=Entry(self.root,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="steel blue",fg="white").place(x=100,y=68,width=200,height=30)

       btn_search=Button(self.root,image=self.search_icon,bg="#033958",activebackground="#033958",bd=0,command=self.get_weather).place(x=310,y=68,width=30,height=30)
       #footer
       lbl_footer=Label(self.root,text="Developed By Shafa",font=("times new roman",12,"bold"),bg="steel blue",pady=5,fg="white").pack(side=BOTTOM,fill=X)

       #####content

       self.lbl_city=Label(self.root,font=("times new roman",15,"bold"),bg="white",fg="green")
       self.lbl_city.place(x=0,y=110, relwidth=1,height=20)

       self.lbl_icon=Label(self.root,font=("times new roman",15,"bold"),bg="white")
       self.lbl_icon.place(x=0,y=135, relwidth=1,height=100)

       self.lbl_temp=Label(self.root,font=("times new roman",15,"bold"),bg="white",fg="orange")
       self.lbl_temp.place(x=0,y=240, relwidth=1,height=20)

       self.lbl_wind=Label(self.root,font=("times new roman",15,"bold"),bg="white",fg="#033958")
       self.lbl_wind.place(x=0,y=265, relwidth=1,height=20)

       self.lbl_error=Label(self.root,font=("times new roman",15,"bold"),bg="white",fg="red")
       self.lbl_error.place(x=0,y=285, relwidth=1,height=20)
       
    
    def get_weather(self):
       api_key=w.api_key
       complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"

       #city_name,country_name,icon,temp_c,temp_f,wind
       if self.var_search.get()=="":
           self.lbl_error.config(text="City Name Required")
           self.lbl_city.config(text="")
           self.lbl_icon.config(image="")
           self.lbl_temp.config(text="")
           self.lbl_wind.config(text="")
        
       else:
           result=requests.get(complete_url)

            



           if result:
               json=result.json()
               city_name=json["name"]
               country=json["sys"]["country"]
               icon=json["weather"][0]["icon"]
               temp_c=json["main"]["temp"]-273.15
               temp_f=(json["main"]["temp"]-273.15)*9/5+32
               wind=json["weather"][0]["main"]
               self.lbl_city.config(text=city_name+" , "+country)
              ##new icon
               self.search_icon2=Image.open(f"icons/{icon}.png")
               self.search_icon2=self.search_icon2.resize((100,100),Image.ANTIALIAS)
               self.search_icon2=ImageTk.PhotoImage(self.search_icon2)

               self.lbl_icon.config(image=self.search_icon2)

           ###error

               self.lbl_error.config(text="")


               deg=u"\N{DEGREE SIGN}"
               self.lbl_temp.config(text=str(round(temp_c))+deg+"C | "+str(round(temp_f,2))+deg+"f ")
               self.lbl_wind.config(text=wind)

               print(city_name,country,icon,temp_c,temp_f,wind)


           else:
               self.lbl_city.config(text="")
               self.lbl_icon.config(image="")
               self.lbl_error.config(text="Invalid City Name")
               self.lbl_temp.config(text="")
               self.lbl_wind.config(text="")






root=Tk()
Obj=MyWeather(root)
root.mainloop()

