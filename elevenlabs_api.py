import elevenlabs
import time

#elevenlabs.set_api_key("f5fd5ed78d745f4ab6ca714fc4546a79")

speech = "Áudio teste"
voiceId = "Antoni" 

audio = elevenlabs.generate(
    text = speech,
    voice = voiceId
)

hora = time.strftime("%Y%m%d-%H%M%S")
fileName = "./audios_elevenlabs/" + voiceId + "_" + hora + ".mp3"
print( fileName)
elevenlabs.save(audio=audio,  
                filename=fileName
        )