
from textblob import  TextBlob
def sentimental(text):
    return TextBlob(text).sentiment.polarity

def getsentiment(text):
    score = sentimental(text)
#    print(score)
    if score<=-0.9:
        return 1
    score+=1
    score*=5
    return round(score)

#print(getsentiment("it is bad design but good function"))

#range -1 to 1
# -1 is negative
# 1 is positive
