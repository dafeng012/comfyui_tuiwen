import json
import os
import re
import time
import asyncio
import edge_tts
import numpy as np

texts = """
与此同时，地球之外的宇宙之中。
一个半透明的强大灵魂，茫然的漂泊着。
与此同时，地球之外的宇宙之中。
一个半透明的强大灵魂，
与此同时，地球之外的宇宙之中。
一个半透明的强大灵魂信息，
与此同时，地球之外的宇宙之中。
"""

novel_name = "guihua"
voice = "zh-CN-XiaoxiaoNeural"
audio_path = "F:\ComfyUI\output"

class guihua:
    
    async def text_to_audio(self, voice, text, audio_folder):
        file = f"{novel_name}_{len(os.listdir(audio_folder))}.mp3"
        audio_path = os.path.join(audio_folder, file)
        await edge_tts_text_to_audio(voice, text, audio_path)

async def edge_tts_text_to_audio(voice, text, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

def create_audio_folders(novel_name, num_folders, audio_path):
    audio_folders = [os.path.join(audio_path, f"{novel_name}_{i}") for i in range(num_folders)]
    for folder in audio_folders:
        os.makedirs(folder, exist_ok=True)
    return audio_folders

async def generate_audio_files(texts, novel_name, voice, audio_path):
    des = guihua()
    sentences = re.split(r"\n", texts.strip())
    audio_folders = create_audio_folders(novel_name, len(sentences), audio_path)
    for i, sentence in enumerate(sentences):
        segments = sentence.split("，")
        for segment in segments:
            segment = segment.strip()
            if segment:
                await des.text_to_audio(voice, segment, audio_folders[i])

asyncio.run(generate_audio_files(texts, novel_name, voice, audio_path))
