import easyocr
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

def write_to_txt(file_path, data):
    all_text = ""
    with open(file_path, 'w') as file:
        for entry in data:
            _, text, _ = entry
            # st.write(bounding_box)
            # x_min, y_min, x_max, y_max = bounding_box

            # Adjust the formatting to align text with bounding box coordinates
            # file.write(f"Bounding Box: ({x_min}, {y_min}, {x_max}, {y_max})\n")
            
            # Add spaces to align the text with the bounding box
            # file.write(f"{' ' * x_min}Text: {text}\n")
            
            # file.write(f"Text: {text}\n")
            file.write(f"{text}\n")
            all_text += text + "\n"
    return all_text

def main():
    st.write("Hello world!")
    with st.sidebar:
        st.write("Hello sidebar!")
        f = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        # st.write(img)
    if f is not None:
        # img = np.asarray(bytearray(f.read()), dtype=np.uint8)
        img = np.array(Image.open(f))
        # reader = easyocr.Reader(["en", "hi", "mr"])
        reader = easyocr.Reader(["en"])
        out = reader.readtext(img)
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, width=300)
            
        txt = write_to_txt("out.txt", out)
        with col2:
            st.write("Found text:")
            st.markdown(txt)
        
        # write contents of out to a txt file which matches the format of the input file
        # out = [(bbox, text, prob), ...]
        # bbox = [x1, y1, x2, y2, x3, y3, x4, y4]
        # text = "string"
        # prob = float
        # out = [(bbox, text, prob), ...]
        

if __name__ == "__main__":
    main()
