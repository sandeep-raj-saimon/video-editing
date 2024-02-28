import os
from moviepy.editor import *
from PIL import Image
import cv2

def old_slideshow(directory):
    padding = 2

    video_clips = [VideoFileClip(f"{directory}/0.mp4"), VideoFileClip(f"{directory}/1.mp4"), VideoFileClip(f"{directory}/2.mp4"), VideoFileClip(f"{directory}/3.mp4")]

    video_fx_list = [video_clips[0]]

    idx = video_clips[0].duration - padding
    for video in video_clips[1:]:
        video_fx_list.append(video.set_start(idx).crossfadein(padding))
        idx += video.duration - padding

    final_video = CompositeVideoClip(video_fx_list)

    audio_path = 'Prod/Suvichar/Audio/ElevenLabs Male Indian Voice (2) copy 2.mp3'
    # if directory == 'Devotion/':
    #     audio_path = 'Prod/Devotion/Audio/8e7a49be-2fb1-4f1a-abf3-45b0aa425b40 copy 2.mp3'
    # elif directory == 'GoodMorning':
    #     audio_path = 'Prod/GoodMorning/Audio/2c97672d-802e-47e4-956b-1e763084fe7f_1.mp3'
    # else:
    #     audio_path = 'Prod/Suvichar/Audio/Achyutam Keshavam Ringtone _ Bhakti Ringtone _ Beautiful Flute Ringtone _ Viral Ringtone_ Amar Beatz (mp3cut.net).mp3'

    audio_clip = AudioFileClip(audio_path)
    audio_clip = audio_clip.set_duration(min(audio_clip.duration, final_video.duration))
    final_video.audio = audio_clip
    final_video.write_videofile(f"{directory}slideshow_old.mp4", fps=24, codec='libx264')