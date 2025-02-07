import streamlit as st
import torch
from transformers import pipeline
from diffusers import StableDiffusionPipeline

text_generator = None
image_generator = None

def load_text_generator():
    """Load and cache the text generation pipeline (GPT-Neo)."""
    global text_generator
    if text_generator is None:
        st.info("🔄 Loading text generator (GPT-Neo)...")
        text_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M", device=-1)
    return text_generator

def load_image_generator():
    """Load and cache the Stable Diffusion pipeline for image generation."""
    global image_generator
    if image_generator is None:
        st.info("🎨 Loading image generator (Stable Diffusion)...")
        device = "cpu"
        image_generator = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", 
            torch_dtype=torch.float32,
            safety_checker=None
        ).to(device)
    return image_generator
