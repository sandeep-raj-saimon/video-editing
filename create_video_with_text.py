from moviepy.editor import ImageClip, TextClip, AudioFileClip, CompositeVideoClip
import os
import numpy as np


def animate_text(get_frame, t):
    """ Function to animate the text. Adjust the np.sin value for different animations. """
    frame_width, frame_height = get_frame(t).shape[:2]
    # Calculate position at time 't'
    # These values adjust the speed and starting position of the animation
    x = int((frame_width / 2) * (np.sin(t) + 1))
    y = int(frame_height * 0.9)  # Position the text at 90% of the height
    return x, y

# File paths
image_path = 'output/1.jpg'
audio_path = 'ElevenLabs AI Voice Male Indian.mp3'
output_video_path = 'sample_text.mp4'

# Load the audio clip
audio_clip = AudioFileClip(audio_path)

# Load the image clip and set its duration to match the audio
image_clip = ImageClip(image_path).set_duration(audio_clip.duration)

# Hindi text
hindi_text = "आपका दिन शुभ हो".encode('utf-8')  # Replace with your text in Hindi
# hindi_text= "dasda"
# # Create a text clip with Hindi text (customize as needed)
# # Specify the path to a font that supports Hindi characters
text_clip = TextClip(hindi_text, fontsize=30, color='white', font='font3.ttf')\
    .set_position('center').set_duration(audio_clip.duration)

# Overlay the text on the image
video_clip = CompositeVideoClip([image_clip, text_clip])

# Set the audio of the composite clip as the audio file
final_clip = video_clip.set_audio(audio_clip)

# Write the result to a file
final_clip.write_videofile(output_video_path, fps=24, codec='libx264')