import os
import yt_dlp


def installer(links, format):

    desktop_path = os.path.join(os.environ['HOME'], 'Desktop')
    saveTo_mp3 = 'YT_Audio_Folder'
    saveTo_mp3_path = os.path.join(desktop_path, saveTo_mp3)
    os.makedirs(saveTo_mp3_path, exist_ok=True)

    saveTo_mp4 = 'YT_Video_Folder'
    saveTo_mp4_path = os.path.join(desktop_path, saveTo_mp4)
    os.makedirs(saveTo_mp4_path, exist_ok=True)

    for link in links:
        if not link:
            print('link is empty, try again')
            return

        try:
            ydl_opts = {} # 'yt-dlp' options

            if format == "mp4":
                ydl_opts = {
                    "format": "bestvideo+bestaudio",
                    "outtmpl": os.path.join(saveTo_mp4_path, "%(title)s.%(ext)s"),
                    "merge_output_format": "mp4"  # Ensures final file is MP4
                }
            elif format == "mp3":
                ydl_opts = {
                    "format": "bestaudio",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192"
                    }],
                    "outtmpl": os.path.join(saveTo_mp3_path, "%(title)s.%(ext)s"),
                }
            else:
                print("Error: Invalid format. Use 'mp4' or 'mp3'.")
                return
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print(f"Download complete! Saved to {saveTo_mp3_path if format == 'mp3' else saveTo_mp4_path}")

        
        except Exception as e:
            print(f'Error during download: {e}')
            return -1
    return 0