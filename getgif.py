import json
import requests

def generate_request(src, title=None, start=0, duration=0):
    req = {"fetchUrl": src,
        "noMd5" : "true",
        "cut": {"start": start,
            "duration": duration
        }
    }
    if title:
    	req['title'] = title
    return json.dumps(req)

def _get_clip_from_video(id=None, start=1, end=1, type="gif"):
	"""
	Usually you don't specify the video id, but it's better to specify the start
	and end point of the clip.
	return type can be gif, mp4, webm
	"""
	url = "http://api.gfycat.com/v1/gfycats"
	src = "www.youtube.com/embed/"
	if id:
		src += id
	else:
		import getvideo
		src = getvideo.get_video()
	data = generate_request(src, start=start, duration=end - start)
	response = requests.post(url, data=data)
	if response.ok:
		gfyname = response.json()['gfyname'] + "." + type
		if type == "gif":
			return "http://thumbs.gfycat.com/" + gfyname, gfyname
		return "http://zippy.gfycat.com/" + gfyname, gfyname

def get_clip_from_video(id=None, start=1, end=1, type="gif"):
	url, filename = _get_clip_from_video()
	try_times = 4
	while try_times > 0 and not url:
		url = _get_clip_from_video(id=id, start=start, end=end)
	if not url:
		raise Exception("Can't get a video at this time.")
	import urllib
	file = urllib.URLopener()
	file.retrieve(url, "tmp/" + filename)
	return "tmp/" + filename
