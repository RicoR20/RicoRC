#Rico Rachmad Maulana
#210322607316
import streamlit as st

#Header
st.header('Rico RC :sparkles:')
st.subheader('Plot')

c1, c2, c3, c4 = st.columns(4)

with c1:
  x = st.number_input('a',value=0)
with c2:
  operator = st.selectbox(
    'operator',
    ('+','-','x',':'), key='k1')
with c3:
  y = st.number_input('b',value=0)
with c4:
  if(operator=='+'):
    st.write('Hasil')
    st.write('= ',x+y)
  elif(operator=='-'):
    st.write('Hasil')
    st.write('= ',x-y)
  elif(operator=='*'):
    st.write('Hasil')
    st.write('= ',x*y)
  elif(operator=='/'):
    st.write('Hasil')
    st.write('= ',x/y)
  
st.caption('Copyright © Rico Rachmad Maulana 2024')
