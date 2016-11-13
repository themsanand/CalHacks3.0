from cred import *
from apiclient.discovery import build



def youtube_service():
	return build("youtube", "v3", developerKey=apikey)

def get_video():
	yt = youtube_service()
	response = yt.search().list(part="id").execute()
	from random import random
	return "www.youtube.com/embed/" + \
	response['items'][int(random() * len(response['items']))]['id']['videoId']
