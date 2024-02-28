from moviepy.editor import ImageClip, vfx
import numpy as np

def rotate_image(image_path, duration, fps, output_path):
    """
    Create a video clip from an image that rotates over a specified duration.

    :param image_path: Path to the input image.
    :param duration: Duration of the video clip in seconds.
    :param fps: Frames per second of the output video.
    :param output_path: Path where the output video will be saved.
    """
    # Load the image as a clip
    clip = ImageClip(image_path).set_duration(duration)
    
    # Apply rotation effect
    # The lambda function generates a continuous rotation by calculating the angle for each frame
    rotating_clip = clip.fl_time(lambda t: np.sin(t * 2 * np.pi / duration) * 360, apply_to=['mask', 'video'])
    
    # Set the frames per second
    rotating_clip.fps = fps
    
    # Write the clip to a file
    rotating_clip.write_videofile(output_path, fps=fps)

# Example usage
image_path = 'data/samples/inputs/sample.jpg'  # Update this path
duration = 10  # Duration of the video in seconds
fps = 1  # Frames per second
output_path = 'rotating_video.mp4'  # Update this path

rotate_image(image_path, duration, fps, output_path)
