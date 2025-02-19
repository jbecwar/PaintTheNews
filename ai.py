from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
from diffusers import StableDiffusion3Pipeline
import torch

def genPrompt(titles):
    prompt = "abstract emotional painting with brush strokes " + (" ".join(titles))
    prompt = removeCommonWords(prompt)
    return prompt

def stableDiffusion(prompt):
    pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
    pipe.enable_model_cpu_offload()
    image = pipe(prompt, height=576, width=1024).images[0]
    image.save("website/paint.png")
    print("Image saved to paint.png")
    return

def removeCommonWords(prompt):
    commonWords = ["the", "a", "an", "is", "of", "in", "on", "with", "and", "or", "for", "to", "from", "by", "as", "at", "that", "this", "these", "those", "there", "here", "where", "when", "why", "how", "what", "which", "who", "whom", "whose", "whether", "while", "because", "since", "so", "if", "then", "else", "either", "neither", "nor", "not", "but", "however", "although", "though", "even", "just", "only", "also", "still", "already", "yet", "now", "then", "again", "once", "always", "never", "sometimes", "often", "rarely", "seldom", "usually", "generally", "mostly", "almost", "nearly", "quite", "very", "too", "enough", "much", "many", "more", "most", "less", "least", "few", "fewer", "fewest", "little", "less", "least", "lot", "lots", "some", "any", "all", "every", "each", "both", "either", "neither", "none", "no", "other", "another", "such", "same", "different", "own", "self", "each other", "one another", "anything", "everything", "nothing", "something", "anyone", "everyone", "no one", "someone", "anybody", "everybody", "nobody", "somebody", "anything", "everything", "nothing", "something", "anywhere", "everywhere", "nowhere", "somewhere", "anytime", "everytime", "never", "sometimes", "often", "rarely", "seldom", "usually", "generally", "mostly", "almost", "nearly", "quite", "very", "too", "enough", "much", "many", "more", "most", "less", "least", "few", "fewer", "fewest", "little", "less", "least"]
    prompt = " ".join([word for word in prompt.split() if word.lower() not in commonWords])
    return prompt

def stableVideoDiffusion():
    pipeline = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
    )
    pipeline.enable_model_cpu_offload()

    image = load_image("website/paint.png")
    
    frames = pipeline(image, decode_chunk_size=8).frames[0]
    export_to_video(frames, "website/generated.mp4", fps=7)
    return