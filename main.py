import subprocess
import sys
import shutil
from datetime import datetime

def check_vram():
    try:
        result = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.free", "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        lines = result.strip().split('\n')
        if not lines:
            print("Error: No GPU detected.")
            sys.exit(1)
        free_vram_mib = int(lines[0])
        if free_vram_mib < 20 * 1024:
            print(f"There isn't enough free vram. (Free: {free_vram_mib / 1024:.2f}GB)")
            sys.exit(1)
    except Exception as e:
        print(f"Error checking VRAM: {e}")
        sys.exit(1)

check_vram()

import db
from git import push
from rss import getTitles
from ai import genPrompt, stableDiffusion, stableVideoDiffusion,longStableDiffusionVideo, genMusic,combineVideoAndMusic
from htmlHelper import updataeHeadlines

db.initDb()
now = datetime.now()
timestamp = now.strftime('%Y%m%d%H%M%S')
generatedTime = now.strftime('%B %d, %Y at %I:%M %p')
shutil.copy('website/paint.png', f'website/old/{timestamp}.png')
shutil.copy('website/generated.mp4', f'website/old/{timestamp}.mp4')    

feedName, titles = getTitles(timestamp)

prompt = genPrompt(titles)

stableDiffusion(prompt)
longStableDiffusionVideo("website/paint.png", "tmp/generated.mp4", 7)
genMusic(prompt, "tmp/music.wav")
combineVideoAndMusic("tmp/generated.mp4", "tmp/music.wav", "website/generated.mp4")
updataeHeadlines(timestamp, feedName, generatedTime)
push()
