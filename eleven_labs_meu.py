


from elevenlabs import play, save
from elevenlabs.client import ElevenLabs
import time



client = ElevenLabs(api_key="")

audio = client.generate(
  text= 'teste voz 1, 2, 3',
  voice="Rachel",
  model="eleven_multilingual_v2"
)

# Converta o gerador em bytes concatenando-o
audio_bytes = b"".join(audio)

#play(audio_bytes)
save(audio_bytes, './audios_elevenlabs/teste_grupo' + '.mp3')

def create_voice_for_text_to_voice(x: list):
    for i in x:
        client = ElevenLabs(api_key="f5fd5ed78d745f4ab6ca714fc4546a79")

        audio = client.generate(
        text= x[i],
        voice="Rachel",
        model="eleven_multilingual_v2"
        )

        # Converta o gerador em bytes concatenando-o
        audio_bytes = b"".join(audio)

        #play(audio_bytes)
        save(audio_bytes, './audios_elevenlabs/part_' + str(x.index(i)) + '.mp3')

def list_audio_files(folder_path):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3") or file.endswith(".wav")]
    return audio_files

