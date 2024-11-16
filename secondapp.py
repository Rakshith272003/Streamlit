import streamlit as st
import numpy as np
import time

progress_bar = st.sidebar.progress(0)
status_text= st.sidebar.empty()

last_rows = np.random.randn(1,1)
chart=st.line_chart(last_rows)

for i in range(1,101):
    new_rows=last_rows[-1:] + np.random.randn(5,1)
    status_text.text("%i%% complete"%i)
    progress_bar.progress(i)
    chart.add_rows(new_rows)
    time.sleep(0.5)
    
progress_bar.empty()
st.button('Re-run')