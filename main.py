import shutil
import db
from datetime import datetime

from git import push
from rss import getTitles
from ai import genPrompt, stableDiffusion, stableVideoDiffusion,longStableDiffusionVideo, genMusic,combineVideoAndMusic

db.initDb()
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
shutil.copy('website/paint.png', f'website/old/{timestamp}.png')
shutil.copy('website/generated.mp4', f'website/old/{timestamp}.mp4')    

titles = getTitles()

print(titles)

prompt = genPrompt(titles)

stableDiffusion(prompt)
longStableDiffusionVideo("website/paint.png", "tmp/generated.mp4", 7)
genMusic(prompt, "tmp/music.wav")
combineVideoAndMusic("tmp/generated.mp4", "tmp/music.wav", "website/generated.mp4")
push()