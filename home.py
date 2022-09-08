from tkinter import *
from functions import *
import tksheet
####################
# LOADING DASHBOARD#
####################

#window
dashboardWindow = Tk()  
dashboardWindow.geometry('800x650')  
dashboardWindow.title('TPEATLA')
dashboardWindow.config(bg="#f07167")




def incident():
    sheet = tksheet.Sheet(dashboardWindow)

    sheet.place(x=60,y=100)

    sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(1)])



    # table enable choices listed below:

    sheet.enable_bindings(("single_select",

                        "row_select",

                        "column_width_resize",

                        "arrowkeys",

                        "right_click_popup_menu",

                        "rc_select",

                        "rc_insert_row",

                        "rc_delete_row",

                        "copy",

                        "cut",

                        "paste",

                        "delete",

                        "undo",

                        "edit_cell"))

def dashboard():
    # Incidents Pane
    sum = getnumber("incidents")
    pane1=Button(dashboardWindow,text=f"{sum}   Incidents",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    # Culprits Pane
    sum = getnumber("culprits")
    pane2=Button(dashboardWindow,text=f"{sum}    Culprits",font=("",25),bg="#f07167")
    pane2.place(x=150,y=400)
    #Active Cameras
    sum = getnumber("cameras")
    pane3=Button(dashboardWindow,text=f"{sum} Active Cameras",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane3.place(x=1,y=450)
    #Connected lights
    sum=getnumber("lights")
    pane4=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane4.place(x=1,y=450)

    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)
    pane1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
    pane1.place(x=1,y=450)










##########
#TOP MENU#
##########

EntryTitle = Label(dashboardWindow,text="TPEATLA DASHBOARD",font=("Courier",30),fg="#fed9b7",bg="#f07167")
EntryTitle.pack(anchor="center")
#########
#Buttons#
#########
btn1=Button(dashboardWindow,text="Dashboard",font=("georgia",15),bg="#f07167" ,command=dashboard)
btn1.place(x=1,y=50)

btn2=Button(dashboardWindow,text="Traffic Feed",font=("georgia",15),bg="#f07167" ,command=traffic)
btn2.place(x=115,y=50)

btn3=Button(dashboardWindow,text="Camera Feed",font=("georgia",15),bg="#f07167" ,command=camera)
btn3.place(x=238,y=50)

btn4=Button(dashboardWindow,text="Incidents",font=("georgia",15),bg="#f07167" ,command=incident)
btn4.place(x=375,y=50)

btn5=Button(dashboardWindow,text="Culprit",font=("georgia",15),bg="#f07167" ,command=culprit)
btn5.place(x=470,y=50)

btn6=Button(dashboardWindow,text="Report",font=("georgia",15),bg="#f07167" ,command=report) 
btn6.place(x=570,y=50)

btn7=Button(dashboardWindow,text="Logout",font=("georgia",15),bg="#f07167" ,command=logout)
btn7.place(x=670,y=50)

# EntryTitle = Label(dashboardWindow,text="TPEATLA DASHBOARD",font=("Courier",20),fg="#fed9b7",bg="#f07167")
# EntryTitle.pack(anchor="center")


# newer = Canvas(Frame,XView=34,YView=46)


# Dashboard = Button(dashboardWindow, text="Dashboard", command=take_logs).grid(row=4, column=0)  
# Incidents = Button(dashboardWindow, text="Incidents", command=take_logs).grid(row=4, column=1)  
# Culprit = Button(dashboardWindow, text="Culprit", command=take_logs).grid(row=4, column=2)  
# LightsFeed = Button(dashboardWindow, text="LightsFeed", command=take_logs).grid(row=4, column=3)  
# CameraFeed = Button(dashboardWindow, text="Camera Feed", command=take_logs).grid(row=4, column=4)  
# Report = Button(dashboardWindow, text="Report", command=take_logs).grid(row=4, column=5)  
# LogOut = Button(dashboardWindow, text="Logout", command=take_logs).grid(row=4, column=6)  



dashboardWindow.mainloop()