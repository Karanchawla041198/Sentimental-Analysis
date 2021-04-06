import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import pickle

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
    def __init__(self, pos, neg, neut):
        labels = 'Positive', 'Negative', 'Neutral'
        sizes = [pos, neg, neut]
        colors = ['green', 'red', 'yellow']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

#g=graph()
#g.showgraph()