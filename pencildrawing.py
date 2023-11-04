import streamlit as st
import numpy as np
from PIL import Image
import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img, output_size):
    inp_img_resized = inp_img.resize(output_size) 
    img_gray = cv2.cvtColor(np.array(inp_img_resized), cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("Pencil Drawing")
st.write("This App help convert your photos to realistic Pencil Drawings")

file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])

if file_image is None:
    st.write("You haven't uploaded any image file")

else:
    input_img = Image.open(file_image)
    input_size = (400, 400)  # Set the input image size (width, height)
    output_size = (400, 400)  # Set the output image size (width, height)
    drawing = pencilsketch(input_img, output_size)
    st.write("**Input Photo**")
    st.image(input_img.resize(input_size), use_column_width=True)
    st.write("**Output Pencil Sketch**")
    st.image(drawing, use_column_width=True)
   
st.write("App by Aswathi Vijayan")