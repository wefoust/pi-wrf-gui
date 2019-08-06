#Importing modules 
import sys
from importlist import *
import requests

#Set Color Scheme and Font
gui_color=color_scheme(1)                                            # 1=default
LARGE_FONT = ("Verdana", 12)

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        messagebox.showwarning("Warning", "No Network Connection Detected Cannot Run Simulation")
        return False

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=gui_color[0])
        screenwidth=self.winfo_screenwidth()                         #get the current screen width
        screenheight=self.winfo_screenheight()                       #current height of screen
        subprocess.call('convert /pi-wrf/WRF_System/lib/dark_hurricane_bg.jpg -resize {}x{}\! /pi-wrf/Output/dark_hurricane_bg.gif'\
                        .format(screenwidth,screenheight),
                        shell=True)
        photo=tk.PhotoImage(file="/pi-wrf/WRF_System/lib/dark_hurricane_bg.gif")
        bg_label_test=tk.Label(self,image=photo)
        bg_label_test.image=photo
        bg_label_test.place(x=0,y=0,relwidth=1,relheight=1)

        frame1_topbanner=tk.Frame(self)
        frame1_topbanner.pack(side=tk.TOP,fill=tk.X)
        
        topbanner = tk.Label(frame1_topbanner,
                             bg=gui_color[1],
                             font=("Arial Bold",40),
                             text="Welcome to the Raspberry Pi-WRF Demo")
        topbanner.pack(fill=tk.X)
        
        from Pages.page_one   import PageOne
        btn_1 = tk.Button(self,
                          text="Run Forecast",
                          font=("Arial Bold",40),
                          borderwidth=5,bg=gui_color[2],
                          activebackground=gui_color[3],
                          width=20,
                          command=lambda : [controller.show_frame(PageOne),check_internet()])
        btn_1.pack(pady=(250,25))
        
        btn_2 = tk.Button(self,
                          text="Run Archived Simulation",
                          font=("Arial Bold",40),
                          borderwidth=5,
                          bg=gui_color[2],
                          activebackground=gui_color[3],
                          width=20)
        btn_2.pack()
