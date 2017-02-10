from pytube import YouTube
import tkinter
import re

class Downloader():

	def print_status(progress, file_size, start):

	    progress_percent = (progress/file_size) * 100
	    progress_percent_str = str(progress_percent)

	    if progress_percent < 10:	  
	    	print('Progress - >', progress_percent_str[:4], '%')	    	
	    elif progress_percent > 10 and progress_percent < 100:	    	
	    	print('Progress - >', progress_percent_str[:5], '%')	    	
	    else:	    	    
	    	print('Progress - >', progress_percent_str[:6], '%')

	def download_video(video_link):
		if re.search('youtube', video_link):
			yt = YouTube(video_link)
			video = yt.get('mp4', '720p')
			print('loading...')
			video.download(path='C:\dw', on_progress=Downloader.print_status)
		else:
			print('Invalid URL')