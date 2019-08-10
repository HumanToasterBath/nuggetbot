from gtts import gTTS
import asyncio
		
async def tts(msgs, disc, rem):
	tts = gTTS(text=msgs.content.lower().replace("!/tts", ""), lang="en")
	tts.save("PlayerData/" + str(msgs.id) + ".wav")
	
	await msgs.channel.send(file=disc.File("PlayerData/{}.wav".format(msgs.id)))
	
	rem.remove("PlayerData/{}.wav".format(msgs.id))
