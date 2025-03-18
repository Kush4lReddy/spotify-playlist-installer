from googleapiclient.discovery import build
import config


def getLinks(songlist):
    
    youtube = build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY) # Create YouTube API client

    song_links = []

    for index, song in songlist.iterrows():

        search_query = f'{song['Song Name']} by {song['Artists']}'

        # Make a request to the YouTube API
        request = youtube.search().list(
            part="snippet",
            q=search_query,
            maxResults=1  # Only fetch 1 result
        )

        response = request.execute()

        # Extract the first video link
        if "items" in response and len(response["items"]) > 0:
            video_id = response["items"][0]["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            song_links.append(video_url)
            print(video_url)
        else:
            print("No results found.")

    return song_links
