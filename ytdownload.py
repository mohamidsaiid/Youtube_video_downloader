from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    if len(youtubeObject.streams.filter(res="720p")) == 0:
        youtubeObject = youtubeObject.streams.get_highest_resolution()
    else:
        youtubeObject = youtubeObject.streams.get_by_resolution("720p")

    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
