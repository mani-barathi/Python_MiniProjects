from googleapiclient.discovery import build
#Youtube API key
# please generate you own youtube API key and replace here
KEY=''
# !!! ID OF YOUTUBE CHANNEL !!!!
ID=''

# creating a build object which can make us connect to youtube's API
youtube=build('youtube','v3',developerKey=KEY)

# making a request to youtube's API to fetch all basic details and statistics of the channel
request=youtube.channels().list(part='statistics,contentDetails,snippet',id=ID)
response=request.execute()

#storing name, description, image url of the channel
profile_name=response['items'][0]['snippet']['title']
profile_description=response['items'][0]['snippet']['description']
profile_img_url=response['items'][0]['snippet']['thumbnails']['medium']['url']

# storing all the stats of channel to a dictionary 
data=response['items'][0]['statistics']

# getting the uploads playlist Id which can be used to fetch all the details of each videos
uploads_id=response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# feching all the video iD's and name's in the uploads playlist
uploads=youtube.playlistItems().list(
		playlistId=uploads_id,
		part='contentDetails,snippet'
	).execute()

video_names=[]		# to store video names 
video_ids=[]		# to store video Id's

for item in uploads['items']:	
	video_names.append(item['snippet']['title'])
	video_ids.append(item['contentDetails']['videoId'])

video=dict(zip(video_ids,video_names))

# fetching the data of latest 5 videos
vid_request=youtube.videos().list(
		part='statistics',
		id=','.join(video_ids)			# passsing all the Id's of video to fetch details of all videos at once
	).execute()

statistics=[]		# to store video details as a dictiionaries (list of dictionaries )

# creating a list named statistics which has stats for the 5 recent videos
for item in vid_request['items']:
	statistics.append(item['statistics'])

# print Every data
print(f'Channel Name: {profile_name}')
print(f'Channel Description: {profile_description}')
#print(f'Channel Image Link: {profile_img_url}')

print('\nChannel  Numbers: ')
print(f'	Subscribers: {data["subscriberCount"]}')
print(f'	Views	   : {data["viewCount"]}')
print(f'	Videos     : {data["videoCount"]}')

print('\nLatest Video Stats: ')
for i in range(5):
	print("-----------------------------------------------")
	print(f'{i+1}) {video_names[i]}')
	print(f'	Views    : {statistics[i]["viewCount"]}')	
	print(f'	Like     : {statistics[i]["likeCount"]}')
	print(f'	Dislike  : {statistics[i]["dislikeCount"]}')	
	print(f'	Comments : {statistics[i]["commentCount"]}')

input()	# just to keep the screen alive
