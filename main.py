import spotify_client
import yt_downloader
import sys
import pandas as pd
import getFromYT

def main():
    if len(sys.argv) < 3:
        print('Error: \nUse command: \npython3 main.py <Spotify_Playlist_Link> <mp4 or mp3>')
        return -1
    
    url = sys.argv[1]
    format = sys.argv[2]
    
    playlist_id = url.split('/playlist/')[1].split('?')[0] # we just need the playlist id.
    playlist = spotify_client.getSongs(playlist_ID=playlist_id)
    
    playlist = pd.DataFrame(playlist) # for better representation

    #now get the links from getFromYT
    song_links = getFromYT.getLinks(songlist=playlist)

    #then pass them as a list to yt_downloader and save stuff to desktop
    yt_downloader.installer(song_links, format)


if __name__ == "__main__":
    main()