import streamlit as st                       
from PIL import Image, ImageFilter
import os                                                                

#create a folder images
if not os.path.exists('images'):
    os.makedirs('images')

def save_image(image):
    img=Image.open(image)
    img.save(f'images/{image.name}.png')

st.title('Image Processing App')

upload=st.file_uploader(
    label='Upload your image',
    type=['png','jpg','jpeg']

)
if upload is not None:
    save_image(upload)
    st.image(
        upload,
        caption='Uploaded Image',
        use_column_width=True
    ) 

    filter=['contour','emboss','edge_enhance','blur']                                                                                                