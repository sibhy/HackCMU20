import facebook
import requests 
import urllib3
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd 
import timeline

# token needs to be refreshed every two hours.
token = "EAAFMBDG68m0BAEnyAIXKDK06TVfyYJHWu2ZBIvwSfASgIZAJtny2LHl5k72aRMRkz5bfgSK3zuJuPbXn3hLVjfIyp15ljB7j8lAnZAi9CCp196REDHO1XampH0YtG6SjeKfu5K1gIZAy1hiAda3wtqkW81dpZCMBRgDBIxOL45SyZCNVqQZBqZC86ZAHeeZClCakZCiNmO8ZCUfPUb1dD5J8kT22ATn7rM0UlDqxp5NLvwl5j3dXqnWbnc3G"

def pullLikes():
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
    nameListFull, nameList, dates = pullLikes()
    makeWordCloud(nameListFull)
    if len(nameList) > 12:
        size = len(nameList) // 2
        timeline.makeTimeLine(nameList[:size], dates[:size])
        timeline.makeTimeLine(nameList[size:], dates[size:])
    else: 
        timeline.makeTimeLine(nameList, dates)


if __name__ == '__main__':
	main()
