import os  
 import pyvips  
 import textwrap  
 from PIL import *  
 import pandas as pd  
 from PIL import Image  
 from PIL import ImageFont  
 from PIL import ImageDraw   
 

 # MAKE A FUNCTION  
 
 def bgoutput(filename, text):  
 
   rendered_text, feedback = pyvips.Image.text(text,   
                         font='Mangal', fontfile='Mangal Regular.ttf',   
                         width=900, height=900,   
                         autofit_dpi=True) 
 
   rendered_text = rendered_text.gravity('centre', 1500, 1500)  

   image = rendered_text.new_from_image([0, 0, 0]).bandjoin(rendered_text)  
   image.write_to_file(f'{filename}.png') 
 
 # GENERATE OUTPUT 1   

 text = "परिस्थितियां विपरीत हो तो कुछ लोग टूट जाते हैं, और कुछ लोग रिकॉर्ड तोड़ देते हैं..!!"  
 bgoutput('new', text)  

 # COMBINE OUTPUT 1 WITH BACKGROUND IMAGE  

 img = Image.open('data/samples/inputs/sample.jpg')   
 b1 = Image.open('bg_img.png')  
 img = img.resize((1000,1000))  
 b1.paste(img,(50,50), mask=img)  

 # GENERATE FINAL OUTPUT  

 b1.save("final.png")