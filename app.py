import streamlit as st
from PIL import Image
from barcode_utils import barcode_gen

st.set_page_config(page_title='Barcode generator',layout='centered')
st.title('Barcode Generator')

u_input=st.text_input('Enter the Input to generate')
if st.button('Generate'):
    try:
        buffer=barcode_gen(u_input)
        img=Image.open(buffer)
        st.image(img, caption=f'barcode for {u_input}')
        st.download_button(label='Download Barcode',data=buffer
                           ,file_name="barcode{u_input}.png")    
    except ValueError as e:
        st.error(str(e))
    