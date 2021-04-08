import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import pickle
import numpy as np

class graph:
    def showgraph(self):

        style.use("ggplot")
        fig=plt.figure()
        ax1=fig.add_subplot(1,1,1)
        def animate(i):
            pullData=open("twitter-out.txt","r").read()
            lines=pullData.split('\n')
            xar=[]
            yar=[]
            x=0
            y=0
            filename="tweets"
            infile = open(filename, 'rb')
            new_dict = pickle.load(infile)
            infile.close()
            for tweet in new_dict:
                 x+=1
                 if tweet['sentiment']=="positive":
                     y=y+1
                 elif tweet['sentiment']=="negative":
                     y=y-1
                 xar.append(x)
                 yar.append(y)
            ax1.clear()
            ax1.plot(xar,yar)
        ani=animation.FuncAnimation(fig,animate,interval=1000)
        plt.show()

class pie:
    def __init__(self, title, pos, neg, neut):
        labels = 'Positive', 'Negative', 'Neutral'
        sizes = [pos, neg, neut]
        colors = ['green', 'red', 'yellow']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()



class twopie:
    def __init__(self,p1,n1,nu1,p2,n2,nu2):
        labels = 'Positive', 'Negative', 'Neutral'
        colors = ['green', 'red', 'yellow']
        data1 = np.array([p1, n1, nu1])
        data2 = np.array([p2, n2, nu2])

        # create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2)

        ax1.pie(data1, labels=labels, colors=colors, autopct='%1.1f%%')
        ax2.pie(data2, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.show()

#g=graph()
#g.showgraph()
