import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import time
from tkinter import *
from threading import Thread
from time import*
root =Tk()  
root.title("Junction 1")
root.iconbitmap("traffilight-logo.ico")
root.geometry("300x200")
model=YOLO('yolov8x.pt')




def DC(video,loc,n,area):
    
    video=video
    loc=loc
    n=n
    area=area
    
    


        

    cap=cv2.VideoCapture(video)


    my_file = open("coco.txt", "r")
    data = my_file.read()
    class_list = data.split("\n")
    #print(class_list)
    count=0
    
    
    

    ret,frame = cap.read()
    frame=cv2.resize(frame,(1020,500))

    results=model.predict(frame)
#   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list=[]
    for index,row in px.iterrows():
#        print(row)

        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if "car"or"motorbike"or"bus"or"truck" in c:
            cx=int(x1+x2)//2
            cy=int(y1+y2)//2
            results=cv2.pointPolygonTest(np.array(area,np.int32),((cx,cy)),False)
            if results >= 0:
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2) 
                cv2.circle(frame,(cx,cy),3,(255,0,255),-1)
                cv2.putText(frame,str(c),(x1,y1),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
                list.append([c])
    cv2.polylines(frame,[np.array(area,np.int32)],True,(255,0,0),2)
    k=len(list)
    cv2.putText(frame,str(k),(696,96),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),3)

    cv2.imwrite(f"images/Cam{n}_image.png",frame)
    f=open(loc, "w")
    
    f.write(str(k))
    f.close()
    return k
            
def calctime(c):
    t=2+(c*2)
    return t




area1=[(372,100),(272,93),(133,303),(384,316)]
area2=[(532,89),(457,89),(5,386),(504,399)]
area3=[(372,100),(272,93),(133,303),(384,316)]
area4=[(770,212),(645,209),(275,469),(724,485)]

loc1="C:/count/Cam_1_count.txt"  #file location to write count of vehicles in cam1 
loc2="C:/count/Cam_2_count.tx"   #file location to write count of vehicles in cam2
loc3="C:/count/Cam_3_count.txt"  #file location to write count of vehicles in cam3
loc4="C:/count/Cam_4_count.txt"  #file location to write count of vehicles in cam4

n=[1,2,3,4]




def updateinfoc1():
    cam4_label.config(text=f' ',bg='red')
    root.update()
    c1=DC("Videos/trafficsmall.mp4",loc1,n[0],area1)
    cam1_label.config(text=f'count: {c1}\n time:{calctime(c1)}',bg='green')
    root.update()
    t1=calctime(c1) -5
    while t1: 
        mins, secs = divmod(t1+5, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam1_label.config(text=f'count: {c1}\n time:{timer}',bg='green')
        root.update()
        root.after(1000)
        t1 -= 1
      


    t2=5
    while t2: 
        mins, secs = divmod(t2, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam1_label.config(text=f'count: {c1}\n time:{timer}',bg='yellow')
        root.update()
        root.after(1000)
        t2 -= 1
    
    root.after(1,updateinfoc2)
        
        


def updateinfoc2():

    cam1_label.config(text=f' ',bg='red')
    root.update()
    c2=DC("Videos/cars.mp4",loc2,n[1],area2)
    cam2_label.config(text=f'count: {c2}\n time:{calctime(c2)}',bg='green')
    root.update()
    t1=calctime(c2) -5
    while t1: 
        mins, secs = divmod(t1+5, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam2_label.config(text=f'count: {c2}\n time:{timer}',bg='green')
        root.update()
        root.after(1000)
        t1 -= 1

    t2=5
    while t2: 
        mins, secs = divmod(t2, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam2_label.config(text=f'count: {c2}\n time:{timer}',bg='yellow')
        root.update()
        root.after(1000)
        t2 -= 1
    
    root.after(1,updateinfoc3)
    
    

def updateinfoc3():
    cam2_label.config(text=f' ',bg='red')
    root.update()
    c3=DC("Videos/Traffic1.mp4",loc3,n[2],area3)
    cam3_label.config(text=f'count: {c3}\n time:{calctime(c3)}',bg='green')
    root.update()
    t1=calctime(c3) -5
    while t1: 
        mins, secs = divmod(t1+5, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam3_label.config(text=f'count: {c3}\n time:{timer}',bg='green')
        root.update()
        root.after(1000)
        t1 -= 1

    t2=5
    while t2: 
        mins, secs = divmod(t2, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam3_label.config(text=f'count: {c3}\n time:{timer}',bg='yellow')
        root.update()
        root.after(1000)
        t2 -= 1
    
    root.after(1,updateinfoc4)

def updateinfoc4():
    cam3_label.config(text=f' ',bg='red')
    root.update()

    c4=DC("Videos/trafficsample.mp4",loc4,n[3],area4)
    cam4_label.config(text=f'count: {c4}\n time:{calctime(c4)}',bg='green')
    root.update()
    t1=calctime(c4) -5
    while t1: 
        mins, secs = divmod(t1+5, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam4_label.config(text=f'count: {c4}\n time:{timer}',bg='green')
        root.update()
        root.after(1000)
        t1 -= 1

    t2=5
    while t2: 
        mins, secs = divmod(t2, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        cam4_label.config(text=f'count: {c4}\n time:{timer}',bg='yellow')
        root.update()
        root.after(1000)
        t2 -= 1
    
    root.after(1,updateinfoc1)

def something():
    
    
    cam1_label.config(text=f' ',bg='red')
    
    
    
    cam2_label.config(text=f' ',bg='red')
   
    
    
    cam3_label.config(text=f' ',bg='red')
   
  

    
    cam4_label.config(text=f' ',bg='red')
    
    root.update()

    root.after(1,updateinfoc1)
    

    
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

frame1=LabelFrame(root,text="cam1",)
frame1.grid(row=0,column=0,sticky='nsew')
cam1_label=Label(frame1)
cam1_label.pack(fill=BOTH,expand=True)



frame2=LabelFrame(root,text="cam2")
frame2.grid(row=0,column=1,sticky='nsew')
cam2_label=Label(frame2)
cam2_label.pack(fill=BOTH,expand=True)



frame3=LabelFrame(root,text="cam3")
frame3.grid(row=1,column=0,sticky='nsew')
cam3_label=Label(frame3)
cam3_label.pack(fill=BOTH,expand=True)



frame4=LabelFrame(root,text="cam4")
frame4.grid(row=1,column=1,sticky='nsew')
cam4_label=Label(frame4)
cam4_label.pack(fill=BOTH,expand=True)

my_button=Button(root,text='start',command= something)
my_button.grid(row=2,column=0)

my_button2=Button(root,text='stop',command= root.quit)
my_button2.grid(row=2,column=1)



root.mainloop()
