import facebook
import requests 
import urllib3
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd 


# token needs to be refreshed every two hours.
token = "EAAnznRNVKZAkBANq54ebSXuosd3KatIT8goyVBZARoOXND5h4R8AEeb54TFQXn47yopZBaWbpMs02OcggaIXZBBwzc5rtbd7pxz42bimTnsgDZBgdkXv8sT0yyXOg0v3pZAi312tExihGdN2uJ1HxDQZADzgqrChly5nMLc9WZAdV646ZCAznTfo7qMw3WSvCKIePkZADyZB6mPFQZDZD"

def pullLikes():
    graph = facebook.GraphAPI(token)
    likes = graph.get_object('me', fields='likes')
    count = 0
    
    # count the number of sets , may be wrong terminology, not used to dicts.
    for key in likes['likes']['data']:
        count += 1
    
    # create a new list with all the names of the things you've liked
    nameList = list()
    for i in range(count):
        nameList.append(likes['likes']['data'][i]['name'])
        # add the names of each thing liked to the list
    
    return nameList 

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
    makeWordCloud(pullLikes())

if __name__ == '__main__':
	main()