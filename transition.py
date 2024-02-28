from moviepy.editor import VideoFileClip, CompositeVideoClip, clips_array, AudioFileClip
from moviepy.video.fx.all import crop
import os


def slide_in_slide_out(input_path1, input_path2, output_path, directory):
    if directory == 'Devotion':
        audio_path = 'Prod/Devotion/Audio/2f4cde3e-eb4d-4ea7-8425-9a75d2e74149.mp3'
    elif directory == 'GoodMorning':
        audio_path = 'Prod/GoodMorning/Audio/2c97672d-802e-47e4-956b-1e763084fe7f_1.mp3'
    else:
        audio_path = 'Prod/Suvichar/Audio/Achyutam Keshavam Ringtone _ Bhakti Ringtone _ Beautiful Flute Ringtone _ Viral Ringtone_ Amar Beatz (mp3cut.net).mp3'
    
    """
    Creates a video where the first clip slides in, stays for a while, and then the second clip slides out.

    Args:
    - input_path1 (str): Path to the first input video file.
    - input_path2 (str): Path to the second input video file.
    - output_path (str): Path where the output video will be saved.
    - slide_duration (int): Duration of the slide-in and slide-out effects in seconds.
    - final_duration (int): Duration in seconds for which each video stays fully visible before starting the slide-out.
    """
    # Load the video clips
    clip1 = VideoFileClip(input_path1)
    clip2 = VideoFileClip(input_path2)

    slide_duration = 1
    final_duration = 5
    # Set the initial position for slide-in and slide-out
    clip1_start_position = lambda t: ('center' if t < slide_duration else 'center', -clip1.size[1] + (clip1.size[1]/slide_duration)*t if t < slide_duration else 0)
    clip2_end_position = lambda t: ('center', 0 if t < final_duration else -(clip2.size[1]/slide_duration)*(t-final_duration))

    # Create composite clips with the specified animations
    sliding_clip1 = CompositeVideoClip([clip1.set_position(clip1_start_position)], size=clip1.size)
    sliding_clip2 = CompositeVideoClip([clip2.set_position(clip1_start_position)], size=clip2.size)

    # Set the duration for the sliding clips
    sliding_clip1 = sliding_clip1.set_duration(slide_duration + final_duration)
    sliding_clip2 = sliding_clip2.set_start(slide_duration + final_duration - 1).set_duration(slide_duration + final_duration)

    # Combine the clips
    final_clip = CompositeVideoClip([sliding_clip1, sliding_clip2], size=clip1.size)

    audio_clip = AudioFileClip(audio_path)
    audio_clip.duration = min(audio_clip.duration, final_clip.duration)
    final_clip.audio = audio_clip
    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264')

def transition(directory):
    input_video1 = f"{directory}/0.mp4"
    input_video2 = f"{directory}/1.mp4"
    output_video = f"{directory}/transition.mp4"
    slide_in_slide_out(input_video1, input_video2, output_video, directory)

# transition('Devotion')