from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')


this_dir = os.listdir(thumbnail_dir)
# filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]
# clip = ImageSequenceClip(filepaths, fps=1)
# clip.write_videofile(output_video)

directory =  {}

for root,dir,files in os.walk(thumbnail_per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        
        if key != None:
            directory[key] = filepath

    
new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)

clip = ImageSequenceClip(new_paths, fps=10)
clip.write_videofile(output_video)