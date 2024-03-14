import elevenlabs
import time

elevenlabs.set_api_key("sua-chave-de-api")

speech = "Áudio teste"
voiceId = "Rachel" 

audio = elevenlabs.generate(
    text = speech,
    voice = voiceId
)

hora = time.strftime("%Y%m%d-%H%M%S")
fileName = "./audios_elevenlabs/" + 'a' + ".mp3"
print( fileName)
elevenlabs.save(audio=audio,  
                filename=fileName
        )