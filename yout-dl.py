from pytube import YouTube

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

youtube_video_url = input("Please enter an URL: ")

if is_valid_url(youtube_video_url):
    try:
    
        yt_obj = YouTube(youtube_video_url)
 
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        print('Video Downloaded In Progress...')
        # download the highest quality video
        filters.get_highest_resolution().download()
        print('Video Downloaded Successfully')
    except Exception as e:
        print(e)
else:
    print('is not URL')