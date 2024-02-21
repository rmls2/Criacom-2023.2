import streamlit as st
import time

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

time.sleep(3)
# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

time.sleep(3)
# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")
time.sleep(3)
# Clear all those elements:
placeholder.empty()