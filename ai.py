import os
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
from diffusers import StableDiffusion3Pipeline
import torch
import moviepy.editor as mpy
from transformers import pipeline
import scipy
import random

def genPrompt(titles):
    prompts = [
        "abstract emotional painting with brush strokes"]
    prompt = random.choice(prompts)
    prompt = prompt + " " + (" ".join(titles))
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
    commonWords = ["trump", "the", "a", "an", "is", "of", "in", "on", "with", "and", "or", "for", "to", "from", "by", "as", "at", "that", "this", "these", "those", "there", "here", "where", "when", "why", "how", "what", "which", "who", "whom", "whose", "whether", "while", "because", "since", "so", "if", "then", "else", "either", "neither", "nor", "not", "but", "however", "although", "though", "even", "just", "only", "also", "still", "already", "yet", "now", "then", "again", "once", "always", "never", "sometimes", "often", "rarely", "seldom", "usually", "generally", "mostly", "almost", "nearly", "quite", "very", "too", "enough", "much", "many", "more", "most", "less", "least", "few", "fewer", "fewest", "little", "less", "least", "lot", "lots", "some", "any", "all", "every", "each", "both", "either", "neither", "none", "no", "other", "another", "such", "same", "different", "own", "self", "each other", "one another", "anything", "everything", "nothing", "something", "anyone", "everyone", "no one", "someone", "anybody", "everybody", "nobody", "somebody", "anything", "everything", "nothing", "something", "anywhere", "everywhere", "nowhere", "somewhere", "anytime", "everytime", "never", "sometimes", "often", "rarely", "seldom", "usually", "generally", "mostly", "almost", "nearly", "quite", "very", "too", "enough", "much", "many", "more", "most", "less", "least", "few", "fewer", "fewest", "little", "less", "least"]
    prompt = " ".join([word for word in prompt.split() if word.lower() not in commonWords])
    return prompt

def stableVideoDiffusion(image, output):
    pipeline = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
    )
    pipeline.enable_model_cpu_offload()

    image = load_image(image)
    
    frames = pipeline(image, decode_chunk_size=8).frames[0]
    export_to_video(frames, output, fps=7)
    return

def extractLastFrame(path):
    import cv2
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
    ret, frame = cap.read()
    cv2.imwrite("tmp/lastFrame.png", frame)
    cap.release()
    return

def combineMpgVideos(videos,output):
    
    clips = [mpy.VideoFileClip(video) for video in videos]
    final_clip = mpy.concatenate_videoclips(clips)
    final_clip.write_videofile(output)
    return

def longStableDiffusionVideo(image,output,runs):
    stableVideoDiffusion(image, "tmp/0.mp4")
    for i in range(runs):
        print(f"Processing run {i}")
        extractLastFrame(f"tmp/{i}.mp4")
        stableVideoDiffusion("tmp/lastFrame.png", f"tmp/{i+1}.mp4")
    combineMpgVideos([f"tmp/{i}.mp4" for i in range(runs+1)], output)
    for i in range(runs+1):
        os.remove(f"tmp/{i}.mp4")
    return

def genMusic(prompt,output):
    synthesiser = pipeline("text-to-audio", "facebook/musicgen-medium")

    music = synthesiser(prompt, forward_params={"do_sample": True})

    scipy.io.wavfile.write(output, rate=music["sampling_rate"], data=music["audio"])
    return

def combineVideoAndMusic(video, music, output):
    video = mpy.VideoFileClip(video)
    music = mpy.AudioFileClip(music)
    video = video.set_audio(music)
    video.write_videofile(output)
    return 
    
