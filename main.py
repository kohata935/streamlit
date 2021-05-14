import streamlit as st
import time

st.title('streamlit超入門')

#--- プログレスバー
st.write('プログレスバーの表示')
'Start!'

latest_iter = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iter.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Finished!'