import tkinter
from tkinter import *
from PIL import ImageTk,Image
import graph
from TwitterClient import *
from graph import *
import pickle

def head():
    headf = Frame(window, bg="red",height=120, width=1000)
    headf.place(x=0,y=0)
    heading = Label(headf, text="Sentimental Analysis",font=('Arial Bold',30))
    heading.place(x=300,y=35)

def nav():
    navf = Frame(window, bg="yellow", height=580, width=180)
    navf.place(x=0,y=120)

    b1=Button(navf,text="Home",width=23,height=9,bg="#b6ddfc",activebackground="#8bcafc",command=generatehomef)
    b1.place(x=2,y=0)
    b2 = Button(navf, text="About",width=23,height=9,bg="#b6ddfc",activebackground="#8bcafc",command=generateaboutf)
    b2.place(x=2,y=145)
    b3 = Button(navf, text="Twitter Sentiment",width=23,height=9,bg="#b6ddfc",activebackground="#8bcafc",command=generatetwitterf)
    b3.place(x=2,y=290)
    b4 = Button(navf, text="Trend Sentiemnt",width=23,height=9,bg="#b6ddfc",activebackground="#8bcafc",command=generatetrendsf)
    b4.place(x=2,y=435)


def generatehomef():
    homef = Frame(window, bg="orange", height=580, width=820)
    homef.place(x=180, y=120)
    Label(homef,text="This is home page").place(x=0,y=0)


def generateaboutf():
    aboutf = Frame(window, bg="pink", height=580, width=820)
    aboutf.place(x=180, y=120)
    Label(aboutf, text="This is About page").place(x=0, y=0)

def generatetwitterf():
    global twitterf
    twitterf = Frame(window, bg="grey", height=580, width=820)
    twitterf.place(x=180, y=120)
    Label(twitterf, text="This is Twitter page").place(x=0, y=0)
    Label(twitterf, text="Twitter Sentiment", font=("Arial", 30)).place(x=230, y=10)
    #photo = PhotoImage(file=r"twitter-icon.png")
    #Label(twitterf, image=photo).place(x=150, y=200)

    global keywordentry
    global tweetsentry

    Label(twitterf, text="Enter Keyword: ", font=("Arial", 18)).place(x=120, y=150)
    keywordentry = tkinter.Entry (twitterf,font=("Arial", 18))
    keywordentry.place(x=380, y=150)

    Label(twitterf, text="Enter No of Tweets: ", font=("Arial", 18)).place(x=120, y=200)
    tweetsentry = tkinter.Entry(twitterf, font=("Arial", 18))
    tweetsentry.place(x=380, y=200)

    B = Button(twitterf, text="Get Tweets", font=("Arial", 18), command=generateObj)
    B.place(x=300, y=280)

def generatetrendsf():
    trendf = Frame(window, bg="green", height=580, width=820)
    trendf.place(x=180, y=120)
    Label(trendf, text="This is Trend page").place(x=0, y=0)


def generateObj():
    name = keywordentry.get()
    number = tweetsentry.get()
    statement=Label(twitterf, text="", font=("Arial", 11))
    if name=="" or number=="":
        statement=Label(twitterf, text="Please Enter All the values    ", font=("Arial", 11)).place(x=300,y=250)
        return

    number=int(number)
    global obj
    obj = twitterObj(name, number)
    statement = Label(twitterf, text="Tweets Successfully Fetched", font=("Arial", 11)).place(x=300,y=250)
    print(obj.ptweets)
    print(obj.ntweets)
    print(obj.otweets)
    filename = 'tweets'
    outfile = open(filename, 'wb')
    pickle.dump(obj.tweets, outfile)
    outfile.close()
    butpos = Button(twitterf, text="Positive Tweets", font=("Arial", 18), command=seepos).place(x=100, y=350)
    butneg = Button(twitterf, text="Negative Tweets", font=("Arial", 18), command=seeneg).place(x=300, y=350)
    butot = Button(twitterf, text="Neutral Tweets", font=("Arial", 18), command=seeneutral).place(x=520, y=350)
    butline = Button(twitterf, text="Line Graph", font=("Arial", 18), command=gengraph).place(x=150, y=450)
    butpie = Button(twitterf, text="Pie Chart", font=("Arial", 18), command=seepie).place(x=500, y=450)


def seepie():
    p=pie(len(obj.ptweets),len(obj.ntweets),len(obj.ntweets))


def gengraph():
    g=graph()
    g.showgraph()

def seepos():
    tempwindow=tkinter.Tk()
    tempwindow.geometry("1000x500")
    scrollbar = Scrollbar(tempwindow)
    mylist = Listbox(tempwindow, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    for x in obj.ptweets:
        str =  x['text']
        str2=""
        for y in str:
            if ord(y) in range(65536):
                str2+=y
        mylist.insert(END, str2)

    mylist.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=mylist.yview)
    #Label(tempwindow, text=str2, font=("Arial", 18)).place(x=0, y=0)
    tempwindow.mainloop()

def seeneg():
    tempwindow=tkinter.Tk()
    tempwindow.geometry("1000x500")
    scrollbar = Scrollbar(tempwindow)
    mylist = Listbox(tempwindow, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    for x in obj.ntweets:
        str =  x['text']
        str2=""
        for y in str:
            if ord(y) in range(65536):
                str2+=y
        mylist.insert(END, str2)

    mylist.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=mylist.yview)
    #Label(tempwindow, text=str2, font=("Arial", 18)).place(x=0, y=0)
    tempwindow.mainloop()

def seeneutral():
    tempwindow=tkinter.Tk()
    tempwindow.geometry("1000x500")
    scrollbar = Scrollbar(tempwindow)
    mylist = Listbox(tempwindow, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    for x in obj.otweets:
        str =  x['text']
        str2=""
        for y in str:
            if ord(y) in range(65536):
                str2+=y
        mylist.insert(END, str2)

    mylist.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=mylist.yview)
    #Label(tempwindow, text=str2, font=("Arial", 18)).place(x=0, y=0)
    tempwindow.mainloop()



window = tkinter.Tk()
window.geometry("1000x700")
head()
nav()


generatehomef()


window.mainloop()