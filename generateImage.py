from PIL import Image, ImageDraw, ImageFont
import random
import math
# Load your image
def formatted_text(text):
      max_length = 20
      if len(text) <= max_length:
            return text

      words = text.split(' ')
      lines = []
      current_line = ""

      for word in words:
            if len(current_line) + len(word) + 1 <= max_length:
                  current_line += " " + word if current_line else word
            else:
                  padding = max_length - len(current_line)
                  left_padding = padding // 2
                  right_padding = padding - left_padding
                  print('padding is', padding, max_length)
                  current_line = (" " * left_padding) + current_line + (" " * right_padding)
                  print('current_line is', current_line)
                  lines.append(current_line)
                  current_line = word

      if current_line:
            padding = max_length - len(current_line)
            left_padding = padding // 2
            right_padding = padding - left_padding
            current_line = (" " * left_padding) + current_line + (" " * right_padding)
            lines.append(current_line)
      

      return '\n'.join(lines)

def generateImage(image_path, text, output_path, iteration):        
      image = Image.open(image_path)

      # Prepare to draw on the image
      draw = ImageDraw.Draw(image)

      # Define the font and size
      font_size = 45

      font_path = "Nirmala.ttf"
      font = ImageFont.truetype(font_path, font_size)

      # Calculate text width and height
      text_width = draw.textlength(text[:20], font=font)
      text_height = font_size

      # Calculate position: place text at the bottom center of the image
      image_width, image_height = image.size
      text_x = (image_width - text_width) / 2  # Center the text
      text_y = 200

      # Specify the text color
      text_color = "white"
      stroke_fill_colors = ["red"]
      # Draw the text on the image
      text = formatted_text(text)
      print('text is', text)

      # bbox = draw.textbbox((text_x, text_y), text, font=font)
      # draw.rectangle(bbox, fill="red")
      # draw.text((text_x, text_y), text, fill=(225, 217, 209, 0), font=font)
      draw.text((text_x, text_y), text, fill=(225, 217, 209, 0), font=font, stroke_width=10,
            stroke_fill=random.choice(stroke_fill_colors))

      # Save or display the image
      print(output_path, iteration, "sas")
      image.save('{}{}.jpg'.format(output_path, iteration))
      return (output_path + f"{iteration}.jpg")
      # To display the image directly (in Jupyter Notebook, for example), you can use:
      # image.show()

generateImage(image_path = 's2.jpg', text = 'कुछ पाने के लिए कुछ करना पड़ता है परछाई भी तब साथ आती है जब धूप में खड़ा रहना पड़ता है', output_path = 'output/', iteration = 1)