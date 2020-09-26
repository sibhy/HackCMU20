#export PYTHONPATH=/opt/anaconda3/lib/python3.8/site-packages:$PYTHONPATH


import facebook
import json



token = 'EAAFiVzBZCbZBsBAFdgnhhZBjfgDBcd4KN4RvpLEKHaawjLktPeqVAgY2E954wjYb1g5pRKyL9YyfrWXXbao2K5Cj9cWDiNfpD7XjWGDK0hucM6ZCV9biO7k9wPfpruHUdmZCEllFlkZBvNrL0y5vzt2kLsJMktlNSNMbiLzaG0ndVw02CQHEuZCihG8he5ZB4rl2qcfafOxAlzxEs80h76vyP1QKdqpBLccV3gQYELnhrgZDZD'


def main():
	graph = facebook.GraphAPI(token)
	
	fields = ['gender, likes']
	
	profile = graph.get_object('me', fields = fields)
