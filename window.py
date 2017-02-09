import tkinter
from tkinter import *
from tkinter import messagebox
from downloader import Downloader

def download_video():
	video_link = E1.get()
	msg=messagebox.showinfo('Download', 'Loading...')
	Downloader.download_video(video_link)
	msg_success=messagebox.showinfo('Download', 'Check your download on C:/dw')

root = tkinter.Tk()
root.geometry("350x100")

L1 = Label(root, text="Insert the YouTube link video here: ")
L1.pack( side = LEFT)

E1 = Entry(root, bd =5)
E1.pack(side = RIGHT)

B = Button(root, text ="Download", command = download_video)
B.place(x=155,y=70)
root.mainloop()
