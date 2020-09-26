import facebook
import requests 
import urllib3
import json



token = "EAAnznRNVKZAkBAGvNuZB52CioeXKDUwOJUf4wFDxjMHwhWD8gWm6eIEpdVIiOmZAWVgOMgQ4LRiIoL3JAKQIPrRLfzLBV5DcRdlYp4iQ6ZANnqhXZBZC0kbn4sgYyEb3SerwxCll1N6LMaJ6MvAgqdEbyb75FkmeOqgRqg7KW2NMeP8uEnaEXKh9U9ZCrNxbtZAsD69CqBkcnZAZCZC2HqHQ2jMZBQCKmfMiBZCAZAtjpIyAlOLAZDZD"


def main():
	graph = facebook.GraphAPI(token)
	#fields = ['first_name', 'location{location}','email','link']
	profile = graph.get_object('me',fields='first_name,location,link,email')	
	#return desired fields
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()