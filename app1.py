import streamlit as st
import time
st.image('medi_snap.jpg',width=200)
# some functions are title, code, header, later, caption, markdown

#input widgedswidgets are the user interface components that allows you to bake intereractively directly into your app.
# e.g. checkbox() , sldier buttom, selectbox, radio, time_input()

#title - title of the app
st.title("Welcome! Manoj")

#header 
st.header("Machine learning")

#sub_header
st.subheader("Linear Regression")

# #st.info() - to add infoormation
st.info("Details of the users")

# #how to give warning message
st.warning('cpme one time! samja ki nhi')

# #error message
st.error("Wrong password dala hai bhai")

# #success message
st.success("correct password, kya baat hai bhai")
# write()
st.write("Employee Name")
st.write(range(50))

# st.markdown("# vs code")
# st.markdown("## vs code")
# st.markdown("### vs code")

st.markdown(":moon:")

st.text('i am someone who is best ')

st.caption('how are you bro, i am waIting for you')

st.latex(r''' a+b x^2+c''')

#widgets

#checkbox
st.checkbox('Login')

#button
st.button('press')

#radio

st.radio('pick your denger',['male','female'])

#selectbox
st.selectbox('choose the courese',['ML','cloud','data science','ai'])

#multiselect
st.multiselect('choose the dept',['content','sales','production','hr'])

#selectslider
st.select_slider('Rating',['bad','good','excellent','outstanding','garda udha dela'])
st.select_slider('Rating',[0,1,2,3,4,5,6,7,8,9,10])

st.slider('enter the number',0,100)

#number input
st.number_input('pick a number',0,100)

#text_input
st.text_input('enter your email')

st.date_input('DOB')

st.time_input('what is time')

#text area
st.text_area("welcome to the my new project")
st.file_uploader('upload your file')

st.color_picker('color')

st.progress(90)

#spinner
# with st.spinner('just wait'):
#     time.sleep(3)

# st.balloons()

#sidebar
st.sidebar.title('welcome to quiz')
st.sidebar.text_input('mail address')
st.sidebar.text_input('password')
st.sidebar.button('submit')
st.sidebar.radio('who you are',['student','wroking'])

#data visulaiazation
import pandas as pd
import numpy as np;
st.title('bar chart')
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)
st.title('line chart')
st.line_chart(data)
st.title('area chart')
st.area_chart(data)