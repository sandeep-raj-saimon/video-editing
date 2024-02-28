from create_video import create_video
from transition import transition
from slideshow_new import new_slideshow
from slideshow_old import old_slideshow
import random

directory = 'Suvichar/'
variations = ["transition", "zoom_in_slideshow", "normal_slideshow"]

# variation = random.choice(variations)
variation = "normal_slideshow"

if (variation == "transition"):
    create_video(directory, resize=True)
    transition(directory)
elif (variation == "zoom_in_slideshow"):            
    create_video(directory, resize=True)
    new_slideshow(directory)
else:
    create_video(directory)
    old_slideshow(directory)
