import datetime

from gtts import gTTS

mytext = input("Enter your text: ")

audio = gTTS(text=mytext, lang="en", tld="co.uk", slow=False)

now = datetime.datetime.now()
file_name = f"{now.strftime('%Y')}-{now.strftime('%m')}-{now.strftime('%d')}"

audio.save(f"{file_name}.mp3")

