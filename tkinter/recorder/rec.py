import tkinter
from tkinter import*
import pyscreenrec
root=Tk()
root.geometry("400x600")
root.title("screen recorder")
root.config(bg="#fff")
root.resizable(False,False)
def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)
def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()
def stop_rec():
    rec.stop_recording()
rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="icon .png")
root.iconphoto(False,image_icon)

#background images
image1=PhotoImage(file="yelllow.png")
Label(root,image=image1,bg="#fff").place(x=-2,y=35)

image2=PhotoImage(file="blue.png")
Label(root,image=image2,bg="#fff").place(x=223,y=200)
#heading
lbl=Label(root,text="Screen Recording",bg="#fff",font="arial 15 bold").pack(pady=20)
image3=PhotoImage(file="recording.png")
Label(root,image=image3,bd=0).pack(pady=30)

#entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=18,font="arial 15").place(x=100,y=350)
lb2=Label(root,text="Screen Recording",bg="#fff",font="arial 15 bold").place(x=100,y=300)
Filename.set("")

#button
start=Button(root,text="start",font="arial 22",bd=0,command=start_rec).place(x=140,y=250)

image4=PhotoImage(file="pause.png")
puase=Button(root,image=image4,bd=0,bg="#fff",command=pause_rec).place(x=50,y=450)

image5=PhotoImage(file="resume.png")
resume=Button(root,image=image5,bd=0,bg="#fff",command=resume_rec).place(x=150,y=450)

image6=PhotoImage(file="stop.png")
stop=Button(root,image=image6,bd=0,bg="#fff",command=stop_rec).place(x=250,y=450)

root.mainloop()
