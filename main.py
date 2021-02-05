import streamlit as st
import time
st.title("Blood Cell Identification using Faster R-CNN ")
st.markdown('#### Detection of White Blood Cell and Red Blood Cell is very useful for various '
            'medical applications, like counting of WBC, disease diagnosis, etc . '
            'Manually looking at the sample via a microscope is a tedious process.'
            ' And this is where Deep Learning models play such a vital role.'
            )

# st.markdown('#### Manually looking at the sample via a microscope is a tedious process.'
#             ' And this is where Deep Learning models play such a vital role.')
st.markdown('#### They can classify and detect the blood cells from microscopic images with impressive precision.')
st.markdown('#### We will be using Faster R-CNN algorithm for detection of the cells')

st.markdown('#### The predicted output from the model should like this image')
st.text('')
st.text('')

from PIL import Image

image = Image.open('example.jpg')

st.image(image, caption='Predicted output', use_column_width=True)
#
st.markdown('### \n\n\n ### Select from the below image or upload a image for testing')
# st.image([image,image], caption=['testing','tt'],width=336)

col1, col2 = st.beta_columns(2)
# def fun():
#     st.image(image, caption='Result', use_column_width=True)
a=None
with col1:

    st.header("Image 1")
    st.image(Image.open('1.jpg'), caption='Predicted output', use_column_width=True)
    if st.button('Select this image ', key=1):
        a=1
with col2:
    st.header("Image 2")
    st.image(Image.open('2.jpg'), caption='Predicted output', use_column_width=True)
    if st.button('Select this image ',key=2):
        a=2

import removing
import copying_image
import test_frcnn
if a==1:

    removing.remove_image()
    copying_image.copying_image("1.jpg")
    test_frcnn.main_function()
    st.image(Image.open('./results/0.png'), caption='Result', use_column_width=True)

if a==2:
    # st.image(Image.open('0.jpg'), caption='Result 2', use_column_width=True)
    removing.remove_image()
    copying_image.copying_image("2.jpg")
    test_frcnn.main_function()
    st.image(Image.open('./results/0.png'), caption='Result', use_column_width=True)

st.markdown('### \n\n\n')

uploaded_file = st.file_uploader("Upload an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    removing.remove_image()
    image.save("./test/image.jpg")


    # copying_image.copying_image("image.jpg")
    test_frcnn.main_function()
    st.image(Image.open('./results/0.png'), caption='Result of Uploaded image', use_column_width=True)

# st.file_uploader("Upload a file")




# quit()
#
# my_bar = st.progress(0)
#
# if st.button('Select this image to select'):
#     for percent_complete in range(100):
#         time.sleep(0.01)
#         my_bar.progress(percent_complete + 1)
#     # with st.spinner('Wait for it...'):
#     #     time.sleep(5)
#     # st.success('Done!')
#
#     st.image(image, caption='Result', use_column_width=True)
#     # st.write('Why hello there')

# else:
#     st.write('Goodbye')
#
# with st.spinner('Wait for it...'):
#      time.sleep(5)
# st.success('Done!')


# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)
# st.file_uploader("Choose a file")