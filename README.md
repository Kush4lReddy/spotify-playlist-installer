# 🎵 Spotify Playlist to YouTube MP3/MP4 Downloader

This Python script extracts songs from a **Spotify playlist**, searches for them on **YouTube**, and downloads them as either **MP3** (audio) or **MP4** (video). 

## Process
- Extracts **all song names and artists** from a given Spotify playlist.
- Searches **YouTube** for the best matching video.
- Downloads **MP3 (audio)** or **MP4 (video)** formats.
- Uses **Spotify API** and **YouTube API** for data retrieval.

---

## Installation

### 1 Clone the Repository**
```sh
git clone https://github.com/your-username/spotify-to-youtube-downloader.git
cd spotify-to-youtube-downloader

```
### 2 Set Up a Virtual Environment (Optional but Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

### 3 Install Dependencies

```sh
pip install -r requirements.txt
```

### 4 Set Up API Keys

#### Spotify API:
- Sign up on Spotify Developer
- Create an app and get Client ID & Client Secret.
- Add a Redirect URI (http://localhost:8888/callback).
#### YouTube API:
- Get a key from Google Cloud Console
- Enable YouTube Data API v3.

#### Update the Keys on the config.py

## Usage
### Run the Script
```sh
python3 main.py <Spotify_Playlist_Link> <mp3 or mp4>
```


### Structure of the Directory
```sh
spotify-to-youtube-downloader/
│── spotify_client.py        # Handles Spotify API authentication & fetching songs
│── getFromYT.py             # Searches YouTube for matching videos
│── yt_downloader.py         # Downloads videos as MP3/MP4
│── main.py                  # Main execution script
│── requirements.txt         # Dependencies list
│── .env                     # Stores API keys (excluded in .gitignore)
│── test_main.py             # Unit tests
│── README.md                # Documentation (this file)
```
