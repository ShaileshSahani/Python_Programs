from gtts import gTTS
import playsound
txt = gTTS("hello there good day to you")
txt.save("new.mp3")
playsound.playsound("new.mp3")

