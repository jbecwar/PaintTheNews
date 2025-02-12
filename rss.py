import torch
import feedparser
from diffusers import StableDiffusion3Pipeline

def get_rss_titles(url):
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries]

rss_url = 'https://www.reddit.com/r/News/.rss'
titles = get_rss_titles(rss_url)

prompt = "abstract emotional painting with brush strokes " + (" ".join(titles))

print(prompt);

pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16
)
pipe.enable_model_cpu_offload()
image = pipe(prompt).images[0]
image.save("sd3.png")
print("Image saved to sd3.png")