from spotifyapi import *
#plid=spt.selectplaylist(results)
def hi():
        print('')
from tkinter import *
from tkinter import ttk

def displaysongs(chofp):
        sop=displaysop(selectplaylist(chofp))
        text=Text(tk, width=80, height=15)
        text.grid(row=2,column=3)

def chplaylist():
        chofp=v.get()
        displaysongs(chofp)
        

tk=Tk()
tk.title("SPOTIFY PLAYLIST MODIFIER")
tk.configure(background='#161616')
tk.geometry("600x600")
Label(tk,text='Spotify Playlist Editor',background='#161616',fg="#1db954",font=('segoe ui emoji',18)).grid(row=1,column=0)
nop,idop=printall()
Label(tk,text="Select your playlist",background='#161616',fg="#1db954",font=('arial',14)).grid(row=0,column=1)
v=IntVar()
for num, val in enumerate(nop):
        Radiobutton(tk,text=val,padx=20,variable=v,indicatoron=False,command=chplaylist,value=num+1,bg='#161616',borderwidth=0,fg='white',selectcolor="#1db954").grid(row=2,column=0)

tk.mainloop()

'''gap maker
if num<9:gap='  '
        elif num<100:gap=' '
        else:gap=''
        '''