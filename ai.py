from diffusers import StableDiffusion3Pipeline
import torch

def genPrompt(titles):
    prompt = "abstract emotional painting with brush strokes " + (" ".join(titles))
    return prompt

def stableDiffusion(prompt):
    pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
    pipe.enable_model_cpu_offload()
    image = pipe(prompt).images[0]
    image.save("website/paint.png")
    print("Image saved to paint.png")
    return
