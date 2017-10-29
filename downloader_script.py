import os
import time

from pytube import YouTube

path_url = '/dw/videos/'
path = os.path.join(path_url)

links_list = None
if os.path.exists('C:\dw\list_file.txt'):
	list_file = open('C:\dw\list_file.txt', 'r')
	links_list = list_file.read()
else:
	print('List file not found. Please create your list_file.txt on C:/dw with the youtube video links.')

def post_download(__yt__):
	holy_path = path_url + __yt__.title
	if os.path.exists(os.path.join(holy_path + '.mp4')) and not os.path.exists(os.path.join(holy_path + '.mp3')):
		new_filename = __yt__.title + '.mp3'
		os.rename(os.path.join(path_url, __yt__.title + '.mp4'), os.path.join(path_url, new_filename))	

def on_progress(stream, chunk, file_handle, bytes_remaining):
	filesize = stream.filesize
	actual_byte = filesize - bytes_remaining
	progress_percent = (actual_byte * 100)/filesize
	progress_percent_str = str(progress_percent)
	
	if progress_percent < 10:
		progress_percent_to_print = 'Progress - >' + progress_percent_str[:4] + '%'
	elif 10 < progress_percent < 100:
		progress_percent_to_print = 'Progress - >' + progress_percent_str[:5] + '%'
	else:
		progress_percent_to_print = 'Progress - >' + progress_percent_str[:6] + '%'

	print(progress_percent_to_print, end='\r')

def download_video(__yt__):
	if not os.path.exists(path):
		os.makedirs(path)
		
	if not os.path.exists(os.path.join(path_url + __yt__.title + '.mp3')):
		__yt__.streams.filter(only_audio=True).filter(subtype='mp4').order_by('abr').desc().first().download(path)
		return True
	else:
		return False
	
if links_list is not None:
	for l in links_list.split(','):
		yt = YouTube(l)
		yt.register_on_progress_callback(on_progress)
		
		print('Starting download of', yt.title)
		if download_video(yt):
			post_download(yt)
		else:
			print('Song already downloaded')
		
	total_path = 'C:' + path_url
	print('Check your downloaded songs on: ',  total_path)
		