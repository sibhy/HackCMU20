import facebook
import requests 
import urllib3
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd 
import timeline
from tkinter import *
from tkinter import simpledialog


def askForToken():
    root = Tk()
    token = simpledialog.askstring("input string" , "Enter API Access Token")
    button = Button(root, text = "popup", command = askForToken)
    button.pack()
    root.geometry("0x0")
    root.mainloop()
    return token

# token needs to be refreshed every two hours.
# token = "EAAnznRNVKZAkBAKHfJPxkUyXPovCMay9gGes7fGDDlNcxeZBhMsuZCyUZBLkL9ApuKfh4TKDGeYt9vpYmhq2frPsJxNHjZBD1lIjoVLWstHqDYIOPZBtVfWLQTJo1G3sl9ZBSq1s8hl11A1XMop7bJX22GHr06m4OtRBhlFB4UqJODgTIvx4xJE6CpNP3LPmalqXO2Ooltt2xZAVzzYcVWVuS1X8yASed65piC09TzGpLwZDZD"

def pullLikes(token):
    graph = facebook.GraphAPI(token)
    likes = graph.get_object('me', fields='likes')
    count = 0
    # count the number of sets , may be wrong terminology, not used to dicts.
    for key in likes['likes']['data']:
        count += 1
    
    # create a new list with all the names of the things you've liked
    nameList = list()
    nameListFull = list()
    dates = list()
    for i in range(count):
        nameListFull.append(likes['likes']['data'][i]['name'])
        if len(likes['likes']['data'][i]) == 3: 
            dates.append(likes['likes']['data'][i]['created_time'][:10])
            nameList.append(likes['likes']['data'][i]['name'])
        # add the names of each thing liked to the list
    
    return (nameListFull, nameList, dates)

def makeWordCloud(listy):
    #convert list to string and generate
    unique_string=(" ").join(listy)
    wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    plt.close()
    return 

def main():
    nameListFull, nameList, dates = pullLikes(askForToken())
    makeWordCloud(nameListFull)
    if len(nameList) > 12:
        size = len(nameList) // 2
        timeline.makeTimeLine(nameList[:size], dates[:size])
        timeline.makeTimeLine(nameList[size:], dates[size:])
    else: 
        timeline.makeTimeLine(nameList, dates)


if __name__ == '__main__':
	main()
