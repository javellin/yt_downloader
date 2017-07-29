import os.path
import time

from pytube import YouTube

links_list = None
if os.path.exists('C:\dw\list_file.txt'):
    list_file = open('C:\dw\list_file.txt', 'r')
    links_list = list_file.read()
else:
    print('File not found. Please create your list_file.txt on C:/dw with the youtube video links.')


def print_status(progress, file_size, start):
    progress_percent = (progress / file_size) * 100
    progress_percent_str = str(progress_percent)

    if progress_percent < 10:
        progress_percent_to_print = 'Progress - >' + progress_percent_str[:4] + '%'
    elif 10 < progress_percent < 100:
        progress_percent_to_print = 'Progress - >' + progress_percent_str[:5] + '%'
    else:
        progress_percent_to_print = 'Progress - >' + progress_percent_str[:6] + '%'

    print(progress_percent_to_print, end='\r')


def is_selected_resolution_valid(__selected_resolution__, __possible_resolutions__):
    for pr in __possible_resolutions__:
        if pr == __selected_resolution__:
            return True
    return False


def already_downloaded(__video__):
    base_path = 'C:\dw\\' + __video__.filename
    return os.path.exists(base_path + '.3gp') or os.path.exists(base_path + '.mp4')


def download_videos(__possible_resolutions__, __yt__):
    selected_resolution = input(
        'Select a resolution: ' + str(__possible_resolutions__) + ' for ' + __yt__.filename + '\n')

    if is_selected_resolution_valid(selected_resolution, __possible_resolutions__):
        video = yt.get(yt.filter('mp4'[-1]), selected_resolution)
        if already_downloaded(video):
            video.filename = input('A file with this name already exists on C:/dw. Insert a new title:\n')

        print('Starting download of: ', video.filename)
        video.download(path='C:\dw', on_progress=print_status)
    else:
        print('You typed an invalid resolution. Try again.')
        download_videos(__possible_resolutions__, __yt__)


if links_list is not None:
    for l in links_list.split(','):
        yt = YouTube(l)

        qualities_list = yt.get_videos()
        possible_resolutions = []

        for q in qualities_list:
            if q.resolution not in possible_resolutions:
                possible_resolutions.append(q.resolution)
            else:
                possible_resolutions.pop(possible_resolutions.index(q.resolution))

        download_videos(possible_resolutions, yt)

        print('\nNext...')
