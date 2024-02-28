from moviepy.editor import ImageClip, TextClip, AudioFileClip, CompositeVideoClip
from generateImage import generateImage
import os

devotion_data = ['शुभ मंगलवार','जय बजरंगबली','जय हनुमान','आपका दिन शुभ हो','आपका दिन मंगलमय हो','ॐ हं हनुमते नमः','जय श्री राम']
good_morning_data = ['सुप्रभात','Good Morning','गुड मॉर्निंग','आपका दिन शुभ हो']
suvichar_data = ['यही जगत की रीत है', 'यही जगत की नीत', 'मन के हारे हार है', 'मन के जीते जीत']

def get_paths(paths):
    final_paths = []
    files = os.listdir(paths)

    i = 1
    for i in range(len(files)):
        file = f"{i}.jpg"
        if (file != '.DS_Store'):
            final_paths.append(f"{i}.jpg")
    return final_paths

def get_audio_paths(paths):
    final_paths = []
    i = 0
    for root,dir,files in os.walk(paths):
       for fname in files:
          if (i == 8):
            break
          
          if (fname != '.DS_Store'):
            final_paths.append(os.path.join(root, fname))
            i+=1
    return final_paths

def resize_func(t):
    if t < 4:
        return 1 + 0.2*t  # Zoom-in.
    elif 4 <= t <= 6:
        return 1 + 0.2*4  # Stay.
    else: # 6 < t
        return 1 + 0.2*(10-t)
    
def create_video(directory, resize=False):
    print('directory is', directory)
    if directory == 'Devotion':
        data = devotion_data
    elif directory == 'GoodMorning':
        data = good_morning_data
    else:
        data = suvichar_data

    image_paths = get_paths(f"Prod/{directory}Images")
    audio_paths = get_audio_paths(f"Prod/{directory}Audio")
    print(audio_paths, image_paths)
    for i in range(4):
        audio_path = audio_paths[i]
        image_path = f"Prod/Suvichar/Images/{image_paths[i]}"
        print(image_path)
        hindi_text = data[i]
        print("here", audio_path, image_path)
        image_path = generateImage(image_path, hindi_text, output_path = directory, iteration = i)
        audio_clip = AudioFileClip(audio_path).set_duration(5)
        # Load the image clip and set its duration to match the audio

        if (resize == True):
            image_clip = ImageClip(image_path).resize(resize_func).set_duration(audio_clip.duration).set_position(('center', 'center'))
        else:
            image_clip = ImageClip(image_path).set_duration(audio_clip.duration).set_position(('center', 'center'))
        # # Create a text clip with Hindi text (customize as needed)
        # # Specify the path to a font that supports Hindi characters
        # text_clip = TextClip(hindi_text, fontsize=70, color="black", font="Nirmala", stroke_color="blue")\
        #     .set_position('center').set_duration(audio_clip.duration)

        # Overlay the text on the image
        video_clip = CompositeVideoClip([image_clip])

        # Set the audio of the composite clip as the audio file
        # final_clip = video_clip.set_audio(audio_clip)
        final_clip = video_clip
        # Write the result to a file
        final_clip.write_videofile(directory + f"{i}.mp4", fps=24, codec='libx264')

# main()