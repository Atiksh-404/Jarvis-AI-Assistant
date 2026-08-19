import asyncio
import edge_tts

TEXT = "Yes, Boss"
VOICE = "en-US-AndrewMultilingualNeural"

async def main():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save("yesboss.mp3")
    print("yesboss.mp3 created successfully!")

asyncio.run(main())