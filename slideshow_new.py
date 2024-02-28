import os
from moviepy.editor import *
from PIL import Image

def new_slideshow(directory):
    # directory = 'Devotion'

    padding = 2
    i = 0
    video_clips = []

    for root,dir,files in os.walk(directory):
        for fname in files:
            if (i == 2):
                break
            if (fname == '.DS_Store'):
                pass
            else:
                video_clip = VideoFileClip(os.path.join(root, fname))
                video_clips.append(video_clip)

    video_fx_list = [video_clips[0]]

    idx = video_clips[0].duration - padding
    for video in video_clips[1:]:
        video_fx_list.append(video.set_start(idx).crossfadein(padding))
        idx += video.duration - padding

    final_video = CompositeVideoClip(video_fx_list)
    if directory == 'Devotion':
        audio_path = 'Prod/Devotion/Audio/8e7a49be-2fb1-4f1a-abf3-45b0aa425b40 copy 2.mp3'
    elif directory == 'GoodMorning':
        audio_path = 'Prod/GoodMorning/Audio/2c97672d-802e-47e4-956b-1e763084fe7f_1.mp3'
    else:
        audio_path = 'Prod/Suvichar/Audio/Achyutam Keshavam Ringtone _ Bhakti Ringtone _ Beautiful Flute Ringtone _ Viral Ringtone_ Amar Beatz (mp3cut.net).mp3'

    audio_clip = AudioFileClip(audio_path)
    print(audio_clip.duration, final_video.duration)
    audio_clip = audio_clip.set_duration(min(audio_clip.duration, final_video.duration))
    final_video.audio = audio_clip
    # final_video.set_audio(audio_clip)
    final_video.write_videofile(f"{directory}slideshow_new.mp4", fps=15, codec='libx264')

# new_slideshow(directory)