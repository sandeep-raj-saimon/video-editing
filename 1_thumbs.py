from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
print(source_path)

clip = VideoFileClip(source_path)
print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)

duration = clip.duration
max_duration = int(duration) + 1

for i in range(max_duration):
    frame = clip.get_frame(i)
    new_image_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    new_image = Image.fromarray(frame)
    new_image.save(new_image_filepath)

for i, frame in enumerate(clip.iter_frames()):
    # frame = clip.get_frame(i)
    new_image_filepath = os.path.join(thumbnail_per_frame_dir, f"{i}.jpg")
    new_image = Image.fromarray(frame)
    new_image.save(new_image_filepath)