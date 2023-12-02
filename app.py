import streamlit as st
import math

fn = st.radio('function',('sin','cos','tan'))

theta = st.slider('angle[θ]', 0, 360, 180)
radian = math.floor((math.pi/180)*theta*1000)/1000
st.title(str(theta)+'[deg] = '+str(radian)+'[rad]')

if fn == 'sin':
    result = math.floor(math.sin(radian)*100)/100
    st.title('sin'+str(theta)+'°='+str(result))
elif fn == 'cos':
    result = math.floor(math.cos(radian)*100)/100
    st.title('cos'+str(theta)+'°='+str(result))
elif fn == 'tan':
    result = math.floor(math.tan(radian)*100)/100
    st.title('tan'+str(theta)+'°='+str(result))