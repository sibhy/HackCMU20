import facebook
import requests 
import urllib3
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd 
import timeline

# token needs to be refreshed every two hours.
token = "EAAFiVzBZCbZBsBAO52IFdZAFYNgur18SVHrUKEw8yVZBJyIPq7L76VMAlGCNraJEJJz2DgQczTX1cr0exDuWo05lNC8ZBhi9x5FuOGZCwNqPqVR3CfC9LxHEZCbKJtccPzCT5NoGUoaLZAJ290Ey6MsSOWUnZCf5voflknA9uOMA53MV4YILWhZCn7dCZCSMI9yyj2DSrYncBkUlAZDZD"

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
        nameList.append(likes['likes']['data'][i]['name'])
        if len(likes['likes']['data'][i]) == 3: 
            dates.append(likes['likes']['data'][i]['created_time'][:10])
            nameList.append(likes['likes']['data'][i]['name'])
        # add the names of each thing liked to the list
    
    return (nameList, dates)

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
    timeline.makeTimeLine(nameList[:5], dates[:5])
    timeline.makeTimeLine(nameList[5:], dates[5:])


if __name__ == '__main__':
	main()
