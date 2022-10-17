import heapq
import sys
from pytube import YouTube

DOWNLOAD_FOLDER = "C:\\Users\\BYUK\\Desktop"

link = 'https://www.youtube.com/watch?v=DIY7M5f8fIE'

file = YouTube(link).streams.get_highest_resolution().download()

try:
    YouTube(link).streams.get_highest_resolution().download(filename="test.mp4", output_path= DOWNLOAD_FOLDER)
    YouTube(link).streams.get_highest_resolution().download()
except:
    print("error")
