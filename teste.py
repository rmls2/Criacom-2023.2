""" import streamlit as st
import time

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

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


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


 """


from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="f5fd5ed78d745f4ab6ca714fc4546a79"
)

audio = client.generate(
  text="vocês estão preparados para amanhã? Graças a deus acabou essa porra!.",
  voice="Rachel",
  model="eleven_multilingual_v2"
)

# Converta o gerador em bytes concatenando-o
audio_bytes = b"".join(audio)

#play(audio_bytes)
save(audio_bytes, './audios_elevenlabs/teste_grupo.mp3')

