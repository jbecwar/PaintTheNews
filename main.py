import shutil
from datetime import datetime

from git import push
from rss import getTitles
from ai import genPrompt, stableDiffusion

timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
shutil.copy('website/paint.png', f'website/old/{timestamp}.png')

titles = getTitles()

print(titles)

prompt = genPrompt(titles)

stableDiffusion(prompt)



#push()