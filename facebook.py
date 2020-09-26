from facebook import *
import requests 
import urllib3

token = "EAAnznRNVKZAkBADUZA1kIPYIwqZBlZB9ICUBp7Y60wBJ5UnmF1pRxqVeVUAQ70rpr7mCPRyQsbvZBNWwIxmltLpUfzYf4dN9WqE8zxKZBWWGwwxlwZB63ZBexBqmZC2J3rXZCStdz7avIzDE94uIpFFZB7QY0i0XZAICpikorXQBkKK3GJGbH7QjnZCwaVnqn8YZBJLgkZD"
graph = facebook.GraphAPI(access_token = token, version = "v8.0")
post = graph.get_object(id='10159130786118013', fields='message')
print(post['message'])

# token = "EAAnznRNVKZAkBAIPEVYQafxYigXrNNN4i6AgoiQWY7vtstpu3YXglRgjkYTCyyCZCSEECNVCa6b9gZAKZCUZBin8XiztpCyuAnnP7MZBZArZCasA67KZAwhqmsgAb2EnRyhBatguMdvwN0r6Vk9Nl56QBOqpAHgZATc5OInVkD78trjl0YlmauSk9NBZC2S6HjvsA7izGWbxJtQbAZDZD"
# graph = facebook.GraphAPI(access_token=token, version = 2.7)
# events = graph.request(‘/searchq=Poetry&type=event&limit=10000’)

# eventList = events['data']
# eventID = eventList[1]['id']

# event1 = graph.get_object(id=eventid,
#  fields=’attending_count,can_guests_invite,category,cover,declined_count,description,end_time,guest_list_enabled,interested_count,is_canceled,is_page_owned,is_viewer_admin,maybe_count,noreply_count,owner,parent_group,place,ticket_uri,timezone,type,updated_time’)
# attenderscount = event1[‘attending_count’]
# declinerscount = event1[‘declined_count’]
# interestedcount = event1[‘interested_count’]
# maybecount = event1[‘maybe_count’]
# noreplycount = event1[‘noreply_count’]

